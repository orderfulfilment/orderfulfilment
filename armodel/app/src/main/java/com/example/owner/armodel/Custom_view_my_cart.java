package com.example.owner.armodel;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import com.android.volley.DefaultRetryPolicy;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.squareup.picasso.Picasso;

import org.json.JSONObject;

import java.util.HashMap;
import java.util.Map;

public class Custom_view_my_cart extends BaseAdapter {
    String [] cid,pname,price,image,total,qty;
    private Context Context;
    public Custom_view_my_cart(Context Con,String [] cid,String [] pname,String [] price,String [] image,String [] total,String [] qty)
    {
        this.Context=Con;
        this.cid=cid;
        this.pname=pname;
        this.price=price;
        this.image=image;
        this.qty=qty;
        this.total=total;
    }
    @Override
    public int getCount() {
        return total.length;
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {
        LayoutInflater inflator=(LayoutInflater)Context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);

        View gridView;
        if(view==null)
        {
            gridView=new View(Context);
            //   gridView=inflator.inflate(R.layout.mac_custom, null);
            gridView=inflator.inflate(R.layout.custom_view_my_cart,null);
        }
        else
        {
            gridView=(View)view;
        }

        TextView tv1=(TextView)gridView.findViewById(R.id.textView7);
        TextView tv2=(TextView)gridView.findViewById(R.id.textView11);
        TextView tv3=(TextView)gridView.findViewById(R.id.textView12);
        ImageView im=(ImageView)gridView.findViewById(R.id.imageView4);
        Button bt=(Button)gridView.findViewById(R.id.button6) ;
        bt.setTag(i);
        bt.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                int ii=Integer.parseInt(view.getTag().toString());
                final String cids=cid[ii];
                final  SharedPreferences she= PreferenceManager.getDefaultSharedPreferences(Context);
                String ip= she.getString("ip","");

                String url = "http://" + ip + ":5000/deletecart";
//        String name="";

                RequestQueue requestQueue = Volley.newRequestQueue(Context);
                StringRequest postRequest = new StringRequest(Request.Method.POST, url,
                        new Response.Listener<String>() {
                            @Override
                            public void onResponse(String response) {

                                try {
                                    JSONObject jsonObj = new JSONObject(response);
                                    if (jsonObj.getString("status").equalsIgnoreCase("Ok")) {


                                    }


                                    // }
                                    else {
                                        Toast.makeText(Context, "Not found", Toast.LENGTH_LONG).show();
                                    }

                                }    catch (Exception e) {
                                    Toast.makeText(Context, "Error" + e.getMessage().toString(), Toast.LENGTH_SHORT).show();
                                }
                            }
                        },
                        new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // error
                                Toast.makeText(Context, "eeeee" + error.toString(), Toast.LENGTH_SHORT).show();
                            }
                        }
                ) {
                    @Override
                    protected Map<String, String> getParams() {
                        SharedPreferences sh = PreferenceManager.getDefaultSharedPreferences(Context);
                        Map<String, String> params = new HashMap<String, String>();

                        params.put("cid",cids);
                        return params;
                    }
                };

                int MY_SOCKET_TIMEOUT_MS=100000;

                postRequest.setRetryPolicy(new DefaultRetryPolicy(
                        MY_SOCKET_TIMEOUT_MS,
                        DefaultRetryPolicy.DEFAULT_MAX_RETRIES,
                        DefaultRetryPolicy.DEFAULT_BACKOFF_MULT));
                requestQueue.add(postRequest);

            }
        });

        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);


        tv1.setText("Name       :"+pname[i]);
        tv2.setText("Quantity   :"+qty[i]);
        tv3.setText("Price      :"+total[i]);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000/"+image[i];
        Log.d("photoooo",url);
        Picasso.with(Context).load(url).into(im);




        return gridView;
    }
}
