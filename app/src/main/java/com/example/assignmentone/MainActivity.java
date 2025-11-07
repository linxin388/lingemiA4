package com.example.assignmentone;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageButton;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Facilities button click
        ImageButton btnFacilities = findViewById(R.id.btnFacilities);
        btnFacilities.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Facilities clicked", Toast.LENGTH_SHORT).show();
            }
        });

        // Events button click
        ImageButton btnEvents = findViewById(R.id.btnEvents);
        btnEvents.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Events clicked", Toast.LENGTH_SHORT).show();
            }
        });

        // Clubs button click
        ImageButton btnClubs = findViewById(R.id.btnClubs);
        btnClubs.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Clubs clicked", Toast.LENGTH_SHORT).show();
            }
        });

        // Support button click
        ImageButton btnSupport = findViewById(R.id.btnSupport);
        btnSupport.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(MainActivity.this, "Support clicked", Toast.LENGTH_SHORT).show();
            }
        });
    }
}