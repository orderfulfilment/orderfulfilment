package com.example.owner.armodel;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class login extends AppCompatActivity implements View.OnClickListener {
    EditText ed1,ed2;
    Button b1;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        ed1=(EditText)findViewById(R.id.ed_uname);
        ed2=(EditText)findViewById(R.id.ed_pwd);
        b1=(Button)findViewById(R.id.btn_login);
        b1.setOnClickListener(this);


   }

    @Override
    public void onClick(View view) {
        if(view==b1)
        {



            final String uname = ed1.getText().toString();
            final String pwd = ed2.getText().toString();

            SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
            String uid = sh.getString("uid", "");
            String hu = sh.getString("ip", "");
            String url = "http://" + hu + ":5000/andlogin";

            RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
            StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                    new Response.Listener<String>() {
                        @Override
                        public void onResponse(String response) {

                            try {
                                JSONObject jsonObj = new JSONObject(response);
                                if (jsonObj.getString("status").equalsIgnoreCase("Ok")) {
                                    String uid = jsonObj.getString("uid");
                                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                                    SharedPreferences.Editor ed = sh.edit();
                                    ed.putString("userid", uid);

                                    ed.commit();


                                    Toast.makeText(getApplicationContext(), "login successfully", Toast.LENGTH_LONG).show();


                          Intent i=new Intent(getApplicationContext(),Home.class);
                             startActivity(i);
                                }


                                // }
                                else {
                                    Toast.makeText(getApplicationContext(), "Invalid username or password", Toast.LENGTH_LONG).show();
                                }

                            } catch (Exception e) {
                                Toast.makeText(getApplicationContext(), "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                    },
                    new Response.ErrorListener() {
                        @Override
                        public void onErrorResponse(VolleyError error) {
                            // error
                            Toast.makeText(getApplicationContext(), "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                        }
                    }
            ) {
                @Override
                protected Map<String, String> getParams() {
                    SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                    Map<String, String> params = new HashMap<String, String>();


                    params.put("username", uname);
                    params.put("password", pwd);
//                params.put("mac",maclis);

                    return params;
                }
            };

            int MY_SOCKET_TIMEOUT_MS = 100000;

            postRequest.setRetryPolicy(new DefaultRetryPolicy(
                    MY_SOCKET_TIMEOUT_MS,
                    DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                    DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
            requestQueue.add(postRequest);

        }
    }
}
