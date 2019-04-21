package com.example.owner.armodel;

import android.content.SharedPreferences;
import android.preference.PreferenceManager;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.Toast;

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

public class Vieworderdetailspending extends AppCompatActivity {


    ListView lv;

    String [] product_id,product_name,price,profile_picture,quantity;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_vieworderdetailspending);


        lv=(ListView) findViewById(R.id.lv);




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
}
