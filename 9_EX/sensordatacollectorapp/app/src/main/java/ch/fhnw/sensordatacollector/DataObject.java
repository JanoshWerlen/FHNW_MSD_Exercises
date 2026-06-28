package ch.fhnw.sensordatacollector;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Locale;

public class DataObject {

    /**
     * some comment about this varaible.
     */
    private Long id;

    private String device;
    private Integer experimentId;
    private Integer patientId;
    private String sensorId;
    private List<Float> data;
    private Long timestamp;
    private String friendlyTimeStamp;
    private Integer accuracy;
    private int sensorType;

    public int getSensorType() {
        return sensorType;
    }

    public void setSensorType(int sensorType) {
        this.sensorType = sensorType;
    }

    public Integer getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(Integer accuracy) {
        this.accuracy = accuracy;
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDevice() {
        return device;
    }

    public void setDevice(String device) {
        this.device = device;
    }

    public String getSensorId() {
        return sensorId;
    }

    public void setSensorId(String sensorId) {
        this.sensorId = sensorId;
    }

    public List<Float> getData() {
        return data;
    }

    public void setData(List<Float> data) {
        this.data = data;
    }

    public Long getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(Long timestamp) {
        this.timestamp = timestamp;
        // SensorEvent.timestamp is nanoseconds since boot; convert to wall-clock milliseconds
        long eventMillis = System.currentTimeMillis() + (timestamp - System.nanoTime()) / 1_000_000L;
        friendlyTimeStamp = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss.SSS", Locale.getDefault())
                .format(new Date(eventMillis));
    }

    public String getFriendlyTimeStamp() {
        return friendlyTimeStamp;
    }

    public Integer getExperimentId() {
        return experimentId;
    }

    public void setExperimentId(Integer experimentId) {
        this.experimentId = experimentId;
    }

    public Integer getPatientId() {
        return patientId;
    }

    public void setPatientId(Integer patientId) {
        this.patientId = patientId;
    }
}
