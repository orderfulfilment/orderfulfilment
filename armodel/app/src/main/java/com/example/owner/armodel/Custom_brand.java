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

import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;


public class Custom_brand extends BaseAdapter {
    String[] brandid,brandname,brandlogo;
    private Context Context;
    public Custom_brand(Context Context,String[] brandid,String[]brandname,String[]brandlogo)
    {
        this.Context=Context;
        this.brandid=brandid;
        this.brandname=brandname;
        this.brandlogo=brandlogo;
    }
    @Override
    public int getCount() {
        return brandid.length;
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
            gridView=inflator.inflate(R.layout.custom_brand,null);
        }
        else
        {
            gridView=(View)view;
        }

        TextView tv1=(TextView)gridView.findViewById(R.id.textView14);

        ImageView im=(ImageView)gridView.findViewById(R.id.imageView7);


        tv1.setTextColor(Color.BLACK);


        tv1.setText(brandname[i]);

        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000"+brandlogo[i];
        Log.d("photoooo",url);
        Picasso.with(Context).load(url).into(im);




        return gridView;
    }
}
