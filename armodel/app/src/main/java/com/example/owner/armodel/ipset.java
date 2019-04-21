package com.example.owner.armodel;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class ipset extends AppCompatActivity implements View.OnClickListener {
EditText ip;
Button bt1;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ipset);
        ip =(EditText)findViewById(R.id.editText);
        bt1 =(Button)findViewById(R.id.button);
        bt1.setOnClickListener(this);
    }

    @Override
    public void onClick(View view) {
        final String editText=ip.getText().toString();
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("ip",editText);
        ed.commit();
        Intent i=new Intent(getApplicationContext(),login.class);
        startActivity(i);

    }
}
