import json
import idgenerator
import os
import time
from threading import Lock


def _storage_path(filename):
    return os.path.join(os.path.dirname(__file__), filename)


def _read_json_file(path, default_value):
    if not os.path.exists(path):
        return default_value

    try:
        with open(path, 'r') as file:
            content = file.read().strip()
        if not content:
            return default_value
        return json.loads(content)
    except json.JSONDecodeError:
        print(f"WARNING: Ignoring invalid JSON in {path}")
        return default_value


def _write_json_file(path, payload):
    temp_path = f"{path}.tmp"
    with open(temp_path, 'w') as file:
        file.write(payload)
    os.replace(temp_path, path)

class Patient(object):
    """Description of class Patient"""
    def __init__(self, name, patient_id=None):
        self.name = name
        if patient_id is None:
            id_gen = idgenerator.AlphaNumericIDGenerator()
            self.id = id_gen.get_id()
        else:
            self.id = patient_id


class PatientEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class Experiment(object):
    def __init__(self, name, id=None):
        self.name = name
        if id is None:
            id_gen = idgenerator.AlphaNumericIDGenerator()
            self.id = id_gen.get_id()
        else:
            self.id = id


class ExperimentEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class DataPoint(object):
    def __init__(self, patient_id, experiment_id, data):
        id_gen = idgenerator.AlphaNumericIDGenerator()
        self.id = id_gen.get_id()
        self.patient_id = patient_id
        self.experiment_id = experiment_id
        self.data = data


class DataPointEncoder(json.JSONEncoder):
    def default(self, obj):
        return obj.__dict__


class DataStorage(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DataStorage, cls).__new__(cls)
            cls.instance.experiments = {}
            cls.instance.patients = {}
            cls.instance.data = []
            cls.instance.loaded = False
            cls.instance.dirty = False
            cls.instance.pending_since_save = 0
            cls.instance.last_save_time = 0.0
            cls.instance.save_lock = Lock()
            cls.instance.autosave_count = 250
            cls.instance.autosave_interval = 3.0
        return cls.instance

    def add_patient(self, obj):
        self.patients[obj.id] = obj

    def get_patient(self, id):
        if id in self.patients:
            return self.patients[id]
        else:
            return None

    def add_experiment(self, obj):
        self.experiments[obj.id] = obj

    def get_experiment(self, id):
        if id in self.experiments:
            return self.experiments[id]
        else:
            return None

    def add_data(self, obj):
        with self.save_lock:
            self.data.append(obj)
            self.dirty = True
            self.pending_since_save += 1

    def _write_files_locked(self):
        print(f"DEBUG: Saving files to: {os.getcwd()}")
        print(f"DEBUG: Data items to save: {len(self.data)}")
        _write_json_file(_storage_path('patients.json'), json.dumps(self.patients, cls=PatientEncoder))
        _write_json_file(_storage_path('experiments.json'), json.dumps(self.experiments, cls=ExperimentEncoder))
        _write_json_file(_storage_path('data.json'), json.dumps(self.data, cls=DataPointEncoder))
        self.last_save_time = time.time()
        self.pending_since_save = 0
        self.dirty = False
        print("DEBUG: Files saved successfully")

    def store_data(self):
        with self.save_lock:
            self._write_files_locked()

    def flush_if_needed(self, force=False):
        with self.save_lock:
            if not self.dirty:
                return False

            now = time.time()
            should_save = (
                force
                or self.pending_since_save >= self.autosave_count
                or (self.last_save_time > 0 and now - self.last_save_time >= self.autosave_interval)
            )

            if not should_save:
                return False

            self._write_files_locked()
            return True

    def load_data(self):
        with self.save_lock:
            if self.loaded:
                return

            patient_file = _storage_path('patients.json')
            patient_data = _read_json_file(patient_file, {})
            for val in patient_data.values():
                obj = Patient(val['name'], val['id'])
                self.patients[val['id']] = obj

            experiment_file = _storage_path('experiments.json')
            experiment_data = _read_json_file(experiment_file, {})
            for val in experiment_data.values():
                obj = Experiment(val['name'], val['id'])
                self.experiments[val['id']] = obj

            data_file = _storage_path('data.json')
            data_points = _read_json_file(data_file, [])
            for val in data_points:
                obj = DataPoint(val['patient_id'], val['experiment_id'], val['data'])
                obj.id = val['id']
                self.data.append(obj)

            self.loaded = True
            self.pending_since_save = 0
            self.dirty = False
