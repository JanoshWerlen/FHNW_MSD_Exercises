import unittest
import json

from app import app


class FlaskTests(unittest.TestCase):

    # ---------------------------------
    # Setup Flask test client
    # ---------------------------------

    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    # ---------------------------------
    # Test index route
    # ---------------------------------

    def test_index(self):

        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data)

        self.assertEqual(data['name'], 'David')

    # ---------------------------------
    # Test patient creation
    # ---------------------------------

    def test_create_patient(self):

        response = self.client.post(
            '/patient',
            json={
                "name": "Max"
            }
        )

        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Test patient creation with missing body
    # ---------------------------------

    def test_patient_missing_body(self):

        response = self.client.post(
            '/patient'
        )

        self.assertNotEqual(response.status_code, 200)

    # ---------------------------------
    # Test experiment creation
    # ---------------------------------

    def test_create_experiment(self):

        response = self.client.post(
            '/experiment',
            json={
                "name": "Experiment A"
            }
        )

        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Test experiment missing name
    # ---------------------------------

    def test_experiment_missing_name(self):

        response = self.client.post(
            '/experiment',
            json={}
        )

        self.assertNotEqual(response.status_code, 200)

    # ---------------------------------
    # Test upload endpoint
    # ---------------------------------

    def test_upload_data(self):

        response = self.client.post(
            '/upload',
            json={
                "patientId": "1",
                "experimentId": "2",
                "value": 42
            }
        )

        self.assertEqual(response.status_code, 200)

    # ---------------------------------
    # Test upload missing patientId
    # ---------------------------------

    def test_upload_missing_patient_id(self):

        response = self.client.post(
            '/upload',
            json={
                "experimentId": "2"
            }
        )

        self.assertNotEqual(response.status_code, 200)

    # ---------------------------------
    # Test unknown patient
    # ---------------------------------

    def test_get_unknown_patient(self):

        response = self.client.get(
            '/patient?id=999999'
        )

        self.assertEqual(response.status_code, 404)

    # ---------------------------------
    # Test unknown experiment
    # ---------------------------------

    def test_get_unknown_experiment(self):

        response = self.client.get(
            '/experiment?id=999999'
        )

        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()