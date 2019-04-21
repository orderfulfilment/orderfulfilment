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

public class Custom_view_my_previous extends BaseAdapter{
    String [] pname,image,qty,total,date;
    private android.content.Context Context;
    public Custom_view_my_previous(Context Con,String [] pname,String [] image,String [] date,String [] qty,String [] total)
    {
        this.Context=Con;
        this.date=date;
        this.pname=pname;

        this.image=image;
        this.qty=qty;
        this.total=total;
    }
    @Override
    public int getCount() {
        return date.length;
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
            gridView=inflator.inflate(R.layout.custom_view_myprevious,null);
        }
        else
        {
            gridView=(View)view;
        }

        TextView tv1=(TextView)gridView.findViewById(R.id.tvname);
        TextView tv2=(TextView)gridView.findViewById(R.id.tvprice);
        TextView tv3=(TextView)gridView.findViewById(R.id.tvqty);
        TextView tv4=(TextView)gridView.findViewById(R.id.tvdate);
        ImageView im=(ImageView)gridView.findViewById(R.id.imageView6);

        tv1.setTextColor(Color.BLACK);
        tv2.setTextColor(Color.BLACK);
        tv3.setTextColor(Color.BLACK);
        tv4.setTextColor(Color.BLACK);


        tv1.setText("Name       :   "+pname[i]);
        tv2.setText("Quantity   :   "+qty[i]);
        tv3.setText("Total      :   "+total[i]);
        tv4.setText("Date       :   "+date[i]);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000/"+image[i];
        Log.d("photoooo",url);
        Picasso.with(Context).load(url).into(im);




        return gridView;
    }
}
