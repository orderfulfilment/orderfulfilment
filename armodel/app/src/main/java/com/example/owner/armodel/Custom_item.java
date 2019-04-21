package com.example.owner.armodel;

import android.content.Context;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.preference.PreferenceManager;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.squareup.picasso.Picasso;

public class Custom_item extends BaseAdapter {
    String [] product_id,product_name,price,profile_picture,quantity;
    public Context Context;
    public Custom_item(Context Con, String [] product_id,String [] product_name,String [] price,String [] profile_picture,String [] quantity)
    {
        this.Context=Con;
        this.product_id=product_id;
        this.product_name=product_name;
        this.price=price;
        this.profile_picture=profile_picture;
        this.quantity=quantity;
    }
    @Override
    public int getCount() {
        return product_id.length;
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
            gridView=inflator.inflate(R.layout.custom_items,null);
        }
        else
        {
            gridView=(View)view;
        }

        TextView tvname=(TextView)gridView.findViewById(R.id.textView2);
        TextView tvprice=(TextView)gridView.findViewById(R.id.textView8);
        TextView tvqua=(TextView)gridView.findViewById(R.id.textView13);
        ImageView im=(ImageView)gridView.findViewById(R.id.imageView3);


        tvname.setText(product_name[i]);
        tvprice.setText(price[i]);
        tvqua.setText(quantity[i]);



      //  tv3.setText("Description  :   "+description[i]);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000/"+profile_picture[i];
        Picasso.with(Context).load(url).into(im);




        return gridView;
    }
}
