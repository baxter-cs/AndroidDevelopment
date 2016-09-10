package org.baxter_academy.sampleacceleromiter;

import android.app.Activity;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.content.SharedPreferences;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;
import android.location.LocationManager;
import android.provider.Settings;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.SeekBar;
import android.widget.TextView;

public class MainActivity extends AppCompatActivity implements SensorEventListener{
    //defines info for future sensor calls
    private SensorManager senSensorManager;
    private Sensor senAccelerometer;
    //just variables for sensor info
    private long lastUpdate = 0;
    private float last_x, last_y, last_z;
    private static final int SHAKE_THRESHOLD = 600;
    public int PROGRESS = 175;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        //Defines sensor info
        senSensorManager = (SensorManager) getSystemService(Context.SENSOR_SERVICE);
        senAccelerometer = senSensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER);
        senSensorManager.registerListener(this, senAccelerometer , SensorManager.SENSOR_DELAY_NORMAL);
        SeekBar mySeekBar = (SeekBar) findViewById(R.id.seekBar);
        //sets SeekBar Progress to last user input
        SharedPreferences sp = getSharedPreferences("SBProgress", Activity.MODE_PRIVATE);
        if (sp.getInt("SBProgress", -1) <= -1){
        }else {
            PROGRESS = sp.getInt("SBProgress", -1);
        }
        mySeekBar.setProgress(PROGRESS);
        //checks if location servises are enabled
        String locationProviders = Settings.Secure.getString(getContentResolver(), Settings.Secure.LOCATION_PROVIDERS_ALLOWED);
        if (locationProviders == null || locationProviders.equals("")) {
            // notify user with alert dialog
            AlertDialog.Builder dialog = new AlertDialog.Builder(this);
            dialog.setMessage(this.getResources().getString(R.string.gps_network_not_enabled));
            dialog.setPositiveButton(this.getResources().getString(R.string.open_location_settings), new DialogInterface.OnClickListener() {
                @Override
                public void onClick(DialogInterface paramDialogInterface, int paramInt) {
                    // TODO Auto-generated method stub
                    startActivity(new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS));
                    //get gps
                }
            });
            dialog.setNegativeButton(this.getString(R.string.Cancel), new DialogInterface.OnClickListener() {

                @Override
                public void onClick(DialogInterface paramDialogInterface, int paramInt) {
                    // TODO Auto-generated method stub

                }
            });
            dialog.show();
        }
        mySeekBar.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
            @Override
            public void onProgressChanged(SeekBar seekBar, int progress, boolean fromUser) {
                //updates sensor sensitivity and saves user input
                PROGRESS = progress;
                SharedPreferences sp = getSharedPreferences("SBProgress", Activity.MODE_PRIVATE);
                SharedPreferences.Editor editor = sp.edit();
                editor.putInt("SBProgress", progress);
                editor.commit();
            }
            //ignore these next two functions, they are for other uses of the SeekBar
            @Override
            public void onStartTrackingTouch(SeekBar seekBar) {

            }

            @Override
            public void onStopTrackingTouch(SeekBar seekBar) {

            }
        });
    }

    @Override
    public void onSensorChanged(SensorEvent sensorEvent) {
        Sensor mySensor = sensorEvent.sensor;

        if (mySensor.getType() == Sensor.TYPE_ACCELEROMETER) {  //Checks X, Y, and Z axis of accelerometer
            float x = sensorEvent.values[0];
            float y = sensorEvent.values[1];
            float z = sensorEvent.values[2];

            long curTime = System.currentTimeMillis(); //gets current time

            if ((curTime - lastUpdate) > 100) { //Checks when the last sensor check was
                long diffTime = (curTime - lastUpdate);
                lastUpdate = curTime;   //Updates Last sensor check for looping
                float speed = Math.abs(x + y + z - last_x - last_y - last_z)/ diffTime * (PROGRESS*PROGRESS);   //gets speed (PROGRESS*PROGGRESS) is to change snesitivity

                if (speed > SHAKE_THRESHOLD) {  //checks speed to movment threshold if else statement updates display text
                    TextView changingText = (TextView) findViewById(R.id.textView);
                    changingText.setText(getString(R.string.Active));
                } else {
                    TextView changingText = (TextView) findViewById(R.id.textView);
                    changingText.setText(getString(R.string.Not_Active));
                }
                //Updates sensor values
                last_x = x;
                last_y = y;
                last_z = z;
            }
        }
    }
    //FROM HERE DOWN IS JUST SENSOR REQUIREMENTS
    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }
    protected void onPause() {
        super.onPause();
        senSensorManager.unregisterListener(this);
    }
    protected void onResume() {
        super.onResume();
        senSensorManager.registerListener(this, senAccelerometer, SensorManager.SENSOR_DELAY_NORMAL);
    }

}
