package com.example.owner.armodel;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.preference.PreferenceManager;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v7.app.AppCompatActivity;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.MenuItem;
import android.view.View;
import android.widget.AdapterView;
import android.widget.EditText;
import android.widget.ListView;
import android.widget.TextView;
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

public class Pendingorders extends AppCompatActivity implements TextWatcher, AdapterView.OnItemClickListener {

    private TextView mTextMessage;

    private BottomNavigationView.OnNavigationItemSelectedListener mOnNavigationItemSelectedListener = new BottomNavigationView.OnNavigationItemSelectedListener() {

        @Override
        public boolean onNavigationItemSelected(@NonNull MenuItem item) {
            switch (item.getItemId()) {
                case R.id.navigation_orders:
                    // mTextMessage.setText(R.string.title_home);
                    Intent i=new Intent(getApplicationContext(),Home.class);
                    startActivity(i);
                    return true;
                case R.id.navigation_pending:
                    Intent ia=new Intent(getApplicationContext(),Pendingorders.class);
                    startActivity(ia);
                    // mTextMessage.setText(R.string.title_dashboard);
                    return true;

                case R.id.nav_logout:
                    Intent ii=new Intent(getApplicationContext(),login.class);
                    startActivity(ii);
                    return true;
            }
            return false;
        }
    };
    EditText edt;
    ListView gv;
    String [] name,email,phone,place,date,total_amount,transactionid,profilepic;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_pendingorders);

        gv=(ListView) findViewById(R.id.lvs);


        gv.setOnItemClickListener(this);


        edt=(EditText) findViewById(R.id.editText6);

        edt.addTextChangedListener(this);


        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip= sh.getString("ip","");

        String url1 = "http://" + ip + ":5000/usergetcompltedeassignedsearch";


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
                                name=new String[jsa.length()];
                                email=new String[jsa.length()];
                                phone=new String[jsa.length()];
                                place=new String[jsa.length()];
                                date=new String[jsa.length()];
                                total_amount=new String[jsa.length()];
                                profilepic=new String[jsa.length()];



                                transactionid=new String[jsa.length()];


                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jsob=jsa.getJSONObject(i);
                                    name[i]=jsob.getString("name");
                                    email[i]=jsob.getString("email");
                                    phone[i]=jsob.getString("phone");
                                    place[i]=jsob.getString("place");
                                    date[i]=jsob.getString("date");
                                    total_amount[i]=jsob.getString("total_amount");

                                    transactionid[i]=jsob.getString("transactionid");
                                    profilepic[i]=jsob.getString("profilepic");
                                }

                                gv.setAdapter(new Custom_view_product(getApplicationContext(), name,email,phone,place,date,total_amount,transactionid,profilepic));

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

                params.put("uid",sh.getString("userid","" ));
                params.put("sr",edt.getText().toString());
                // params.put("sh_id", sh.getString("newid",""));
                // params.put("sh_id", "2");

                return params;
            }
        };
        requestQueue.add(postRequest);





        BottomNavigationView navigation = (BottomNavigationView) findViewById(R.id.navigation);
        navigation.setOnNavigationItemSelectedListener(mOnNavigationItemSelectedListener);
    }

    @Override
    public void beforeTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void onTextChanged(CharSequence charSequence, int i, int i1, int i2) {

    }

    @Override
    public void afterTextChanged(Editable editable) {

        gv=(ListView) findViewById(R.id.lvs);
        edt=(EditText) findViewById(R.id.editText6);

        edt.addTextChangedListener(this);


        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        String ip= sh.getString("ip","");

        String url1 = "http://" + ip + ":5000/usergetcompltedeassignedsearch";


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
                                name=new String[jsa.length()];
                                email=new String[jsa.length()];
                                phone=new String[jsa.length()];
                                place=new String[jsa.length()];
                                date=new String[jsa.length()];
                                total_amount=new String[jsa.length()];

                                transactionid=new String[jsa.length()];


                                for(int i=0;i<jsa.length();i++)
                                {
                                    JSONObject jsob=jsa.getJSONObject(i);
                                    name[i]=jsob.getString("name");
                                    email[i]=jsob.getString("email");
                                    phone[i]=jsob.getString("phone");
                                    place[i]=jsob.getString("place");
                                    date[i]=jsob.getString("date");
                                    total_amount[i]=jsob.getString("total_amount");

                                    transactionid[i]=jsob.getString("transactionid");
                                }

//                                gv.setAdapter(new Custom_view_product(getApplicationContext(), pid, pname, price, image, description));

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

                params.put("uid",sh.getString("uid","" ));
                params.put("sr",edt.getText().toString());
                // params.put("sh_id", sh.getString("newid",""));
                // params.put("sh_id", "2");

                return params;
            }
        };
        requestQueue.add(postRequest);




    }

    @Override
    public void onItemClick(AdapterView<?> adapterView, View view, int i, long l) {


        SharedPreferences sh=PreferenceManager.getDefaultSharedPreferences(getApplicationContext());
        SharedPreferences.Editor ed=sh.edit();
        ed.putString("wid", transactionid[i]);
        ed.commit();




        Intent ins =new Intent(getApplicationContext(),Vieworderdetailspending.class);
        startActivity(ins);




    }
}
