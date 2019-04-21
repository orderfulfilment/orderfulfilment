package com.example.owner.armodel;

import android.content.Context;
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

public class Custom_category extends BaseAdapter {
    String []category_id,cat_name;
    private Context Context;
    public Custom_category(Context Context,String []category_id,String []cat_name)
    {
        this.Context=Context;
        this.category_id=category_id;
        this.cat_name=cat_name;

    }
    @Override
    public int getCount() {
        return cat_name.length;
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

            gridView=inflator.inflate(R.layout.custom_category,null);
        }
        else
        {
            gridView=(View)view;
        }
        TextView tv1=(TextView)gridView.findViewById(R.id.textView18);
        tv1.setTextColor(Color.BLACK);
        tv1.setText(cat_name[i]);
        return gridView;
    }
}
