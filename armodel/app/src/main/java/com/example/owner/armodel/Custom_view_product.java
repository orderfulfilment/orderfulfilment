package com.example.owner.armodel;

import android.content.Context;
import android.content.Intent;
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

public class Custom_view_product extends BaseAdapter {
    String [] name,email,phone,place,date,total_amount,transactionid,profilepic;
    public Context Context;
    public Custom_view_product(Context Con, String [] name,String [] email,String [] phone,String [] place,String [] date,String [] total_amount,String [] transactionid,String [] profilepic)
    {
        this.Context=Con;
        this.name=name;
        this.email=email;
        this.phone=phone;
        this.place=place;
        this.date=date;
        this.total_amount=total_amount;
        this.transactionid=transactionid;
        this.profilepic=profilepic;
    }
    @Override
    public int getCount() {
        return name.length;
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
            gridView=inflator.inflate(R.layout.custom_view_product,null);
        }
        else
        {
            gridView=(View)view;
        }

        TextView tvid=(TextView)gridView.findViewById(R.id.textView28);
        TextView tvname=(TextView)gridView.findViewById(R.id.textView29);
        TextView tvplace=(TextView)gridView.findViewById(R.id.textView30);
        TextView tvemail=(TextView)gridView.findViewById(R.id.textView31);
        TextView tvphn=(TextView)gridView.findViewById(R.id.textView32);
        TextView tvamnt=(TextView)gridView.findViewById(R.id.textView33);
//        TextView tv3=(TextView)gridView.findViewById(R.id.txtdes);
        ImageView im=(ImageView)gridView.findViewById(R.id.imv);


        tvid.setText(transactionid[i]);
        tvname.setText(name[i]);
        tvplace.setText(place[i]);
        tvemail.setText(email[i]);
        tvphn.setText(phone[i]);
        tvamnt.setText(total_amount[i]);


      //  tv3.setText("Description  :   "+description[i]);
        SharedPreferences sh= PreferenceManager.getDefaultSharedPreferences(Context);
        String ip=sh.getString("ip","");
        String url="http://" + ip + ":5000/"+profilepic[i];
        Picasso.with(Context).load(url).into(im);




        return gridView;
    }
}
