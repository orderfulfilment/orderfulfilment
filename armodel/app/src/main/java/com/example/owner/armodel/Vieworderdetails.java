package com.example.owner.armodel;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Vieworderdetails extends AppCompatActivity implements View.OnClickListener {


    ListView lv;
    Button bt2;

    String [] product_id,product_name,price,profile_picture,quantity;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vieworderdetails);


        lv=(ListView) findViewById(R.id.lv);
        bt2=(Button) findViewById(R.id.button2);

        bt2.setOnClickListener(this);




        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip= sh.getString("ip","");

        String url1 = "http://" + ip + ":5000/getordererdproducts";


        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
//            Toast.makeText(getApplicationContext(),"hai",Toast.LENGTH_SHORT).show();
        StringRequest postRequest = new StringRequest(Request.Method.POST, url1,
                new Response.Listener<String>()
                {
                    @Override
                    public void onResponse(String response) {

//                          Toast.makeText(getApplicationContext(),response,Toast.LENGTH_SHORT).show();


                        // response
                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            String sucs=   jsonObj.getString("status");
                            if(sucs.equalsIgnoreCase("ok"))


                            {
                                JSONArray jsa=jsonObj.getJSONArray("res");
                                product_id=new String[jsa.length()];
                                product_name=new String[jsa.length()];
                                price=new String[jsa.length()];
                                profile_picture=new String[jsa.length()];
                                quantity=new String[jsa.length()];


                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jsob=jsa.getJSONObject(i);
                                    product_id[i]=jsob.getString("product_id");
                                    product_name[i]=jsob.getString("product_name");
                                    price[i]=jsob.getString("price");
                                    profile_picture[i]=jsob.getString("profile_picture");
                                    quantity[i]=jsob.getString("quantity");

                                }

                                lv.setAdapter(new Custom_item(getApplicationContext(), product_id,product_name,price,profile_picture,quantity));


                            }
                        } catch (Exception e) {
                            Toast.makeText(getApplicationContext(),"eeeee"+e.toString(),Toast.LENGTH_LONG).show();
                        }
                    }
                },
                new Response.ErrorListener()
                {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        // error
                        Toast.makeText(getApplicationContext(),"eeeee"+error.toString(),Toast.LENGTH_SHORT).show();
                    }
                }
        ) {
            @Override
            protected Map<String, String> getParams()
            {
                SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
                Map<String, String> params = new HashMap<String, String>();

                params.put("wid",sh.getString("wid","" ));
                // params.put("sh_id", sh.getString("newid",""));
                // params.put("sh_id", "2");

                return params;
            }
        };
        requestQueue.add(postRequest);
    }
    @Override
    public void onClick(View view) {

        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String uid = sh.getString("uid", "");
        String hu = sh.getString("ip", "");
        String url = "http://" + hu + ":5000/updatestatus";

        RequestQueue requestQueue = Volley.newRequestQueue(getApplicationContext());
        StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        try {
                            JSONObject jsonObj = new JSONObject(response);
                            if (jsonObj.getString("status").equalsIgnoreCase("Ok")) {
                                Toast.makeText(getApplicationContext(), "Order Delivery Entry done successfully ", Toast.LENGTH_LONG).show();
                                Intent i=new Intent(getApplicationContext(),Home.class);
                                startActivity(i);
                            }
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
                params.put("workid", sh.getString("wid","" ));
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
