from flask import Flask, render_template, request, jsonify


from dbconnection import conn
from flask.globals import session

app=Flask(__name__)
app.secret_key='hi'
c=conn()


@app.route('/adminsample')
def adminsample():
    return render_template(("admintemplate.html"))


@app.route('/aaa')
def loginpage():
    return render_template(("admin_login.html"))
@app.route('/login',methods=["post"])
def login():
    username=request.form["username"]
    # print(username)
    password=request.form["password"]
    # print(password)
    s="select * from login where user_name='"+username+"' and password='"+password+"'"
    res=c.selectone(s)
    # print(res)
    if res!=None:

        type=res[3]

        if type=="admin":
            session["id"]=0
            # print(session["id"])
            return  viewusers()
        else:
            query="select *from user where email='"+username+"'"
            print(query)
            res=c.selectone(query)
            session["id"]=res[0]
            # print(session["id"])
            return viewprofile()
    else:

        return render_template('login_main.html',status='no')
@app.route('/show')
def show():
    return render_template('user_register.html')
@app.route('/reg',methods=['post'])
def reg():
    name=request.form['name']
    print(name)
    phoneno = str(request.form['phonenumber'])
    print(phoneno)
    place=request.form['place']
    print(place)
    city=request.form['city']
    print(city)
    country=request.form['country']
    print(country)
    email=request.form['email']
    print(email)
    password=str(request.form['password'])
    print(password)
    confirmpassword=request.form['confirmpassword']
    print(confirmpassword)
    addprofilepic = request.files['add']
    print(addprofilepic)
    s="select max(user_id)from user"
    print(s)
    user_id=c.mid(s)
    print(user_id)
    path="static/userimgs/"+str(user_id)+".jpg"
    addprofilepic.save(path)
    if password==confirmpassword:
     query ="insert into user(name,phone,place,city,country,profilepic,email)values('"+name+"','"+phoneno+"','"+place+"','"+city+"','"+country+"','"+path+"','"+email+"')"
     print(query)
     i=c.nonreturn(query)
     query1="insert into login(user_name,password,type) values('"+email+"','"+password+"','user')"
     print(query1)
     i=c.nonreturn(query1)
     return 'ok'
    else:
        return 'currentpassword and confirmpassword are different'
def adminpage():
    return render_template('admin_page.html')
@app.route('/addcategory')
def addcategory():
    return render_template('admin_addcategory.html')
@app.route('/admin_addcategory',methods=['post'])
def admin_addcategory():
    categoryname= request.form['categoryname']
    c=conn()
    s="select max(category_id)from category"
    print(s)
    category_id=c.mid(s)
    print(category_id)
    query="insert into category(name)value('"+categoryname+"')"
    print(query)
    i=c.nonreturn(query)
    return view()
@app.route('/viewcategory')
def viewcategory():
    return render_template('admin_viewcayegory.html')
@app.route('/view')
def view():
    query="select * from category"

    res=c.selectall(query)
    print(res)

    return render_template('admin_viewcayegory.html', ab=res)

@app.route('/editcategory/<id>')
def editcategory(id):
    query="select*from category where category_id='"+str(id)+"'"
    res=c.selectone(query)
    return render_template('admin_editcategory.html',r=res)
@app.route('/editc',methods=['POST'])
def editc():
    categoryname=request.form['categoryname']
    categoryid = request.form['id']
    query="update category set name='"+categoryname+"' where category_id='"+str(categoryid)+"'"
    i=c.nonreturn(query)
    return view()
@app.route('/deletec/<id>')
def deletec(id):
    query="delete from category where category_id='"+str(id)+"'"
    i=c.nonreturn(query)
    return view()
@app.route('/addproduct')
def addproduct():
    query = "select * from category"
    res = c.selectall(query)
    return render_template('admin_addproduct.html', r=res)
@app.route('/admin_addproduct',methods=['post'])
def admin_addproduct():
    productname= request.form['productname']
    print(productname)
    profit=request.form["profit"]
    brandname = request.form['brandname']
    print(brandname)
    price = str(request.form['price'])
    print(price)
    category = request.form['category']
    print(category)
    description = request.form['description']
    print(description)
    profile_picture=request.files['profilepicture']
    s = "select max(product_id)from product"
    print(s)
    product_id = c.mid(s)
    print(product_id)
    path = "static/userimgs/" + str(product_id) + ".jpg"
    profile_picture.save(path)

    query = "insert into product(product_name,brandname,price,category_id,details,profile_picture,profit)value('" + productname + "','" + brandname + "','" + price + "','" + category + "','" + description + "','" + path + "','"+profit+"')"
    print(query)
    i=c.nonreturn(query)
    return viewp()


@app.route('/searchusers',methods=['POST'])
def searchusers():
    # search
    searchword = request.form["search"]
    query = "select * from user"
    res = c.selectall(query)
    totalitems = len(res)
    noofrows = int(totalitems / 3)
    return render_template('admin_customer.html', ac=res, totalitems=totalitems, noofrows=noofrows)

@app.route('/adminviewreports')
def adminviewreports():
    qry="select user.name,email,phone,place,date,total_amount from sales_master,user where sales_master.custid=user.user_id"
    c=conn()
    res=c.selectall(qry)
    return render_template("viewreports.html",res=res)


@app.route('/adminassignget')
def adminassignget():
    qry="select user.name,email,phone,place,date,total_amount,sales_master.transactionid from sales_master,user where sales_master.custid=user.user_id and sales_master.`transactionid` NOT IN ( SELECT `orderid` FROM `order_assign`) "
    c=conn()
    res=c.selectall(qry)
    return render_template("assignordertostaff.html",res=res)


@app.route('/viewassignedorder')
def viewassignedorder():
    qry="SELECT user.name,email,user.phone,user.place,DATE,total_amount,sales_master.transactionid,`staff`.`name` AS 'Assigned To',`order_assign`.`status` FROM sales_master,USER,`order_assign`,`staff`  WHERE sales_master.custid=user.user_id   AND `staff`.`staffid`=`order_assign`.`staffid`  AND `order_assign`.`orderid`=`sales_master`.`transactionid` "
    print(qry)
    c=conn()
    res=c.selectall(qry)
    return render_template("viewassignedorder.html",res=res)
@app.route('/post_adminviewreports',methods=["POST"])
def post_adminviewreports():
    frm=request.form["from"]
    to=request.form["to"]
    qry = "select user.name,email,phone,place,date,total_amount from sales_master,user where sales_master.custid=user.user_id and date between '"+frm+"' and '"+to+"'"
    c = conn()
    res = c.selectall(qry)
    return render_template("viewreports.html", res=res)

def adminviewreports():
    qry="select user.name,email,phone,place,date,total_amount from sales_master,user where sales_master.custid=user.user_id"
    c=conn()
    res=c.selectall(qry)
    return render_template("viewreports.html",res=res)
@app.route('/getallproducts')
def getallproducts():
    # search

    query = "select * from product"
    res = c.selectall(query)
    totalitems = len(res)
    noofrows = int(totalitems / 3)
    return render_template('userviewproducts.html', ac=res, totalitems=totalitems, noofrows=noofrows)

@app.route("/productsearch",methods=['POST'])
def productsearch():
    kword=request.form['search']
    query = "select * from product where product_name like '%"+kword+"%' or brandname like '%"+kword+"%'"
    res = c.selectall(query)
    totalitems = len(res)
    noofrows = int(totalitems / 3)
    return render_template('userviewproducts.html', ac=res, totalitems=totalitems, noofrows=noofrows)

@app.route('/viewmyoffer')
def viewmyoffer():
    id=session["id"]
    qry="select product.*,offer.offer,offer.offr_latdate from offer inner join product on offer.product_id=product.product_id where offer_id in (select ofrid from offer_subscribed where uid='"+str(id)+"')"
    c=conn()
    res=c.selectall(qry)
    return render_template("user_myoffers.html",res=res)

@app.route("/addoffer",methods=['POST'])
def addoffer():

    catid=request.form["category"]

    productid=request.form['productname']


    qry="select brandname from product where product_id='"+productid+"'"
    resd=c.selectone(qry)
    brandname=resd[0]




    offer=request.form['offer']
    ldate=request.form['offerdate']
    qry="insert into offer (product_id,offer,offr_latdate) values ('"+str(productid)+"','"+offer+"','"+ldate+"')"
    print(qry)
    ofid=c.nonreturn(qry)


    qry="select * from user where user_id in (select custid from sales_master where transactionid in (select transactionid from sales_sub where itemid in ( select product_id from product where brandname in( select brandname from product where product_id='"+productid+"' ) or  category_id='"+catid+"' )))"
    resbuyedusers= c.selectall(qry)

    catscorepos=[]
    catscoreneg=[]

    catprob=[]


    brandscorepos=[]
    brandscoreneg=[]

    brandprob=[]
    cnt=[]
    indx=0
    for row in resbuyedusers:

        qw="select count(*) from product where category_id='"+catid+"' or brandname='"+brandname+"'"
        d=c.selectone(qw)
        cnt.append(d[0])
        qry="select scorepos,scoreneg from cat_score where catid='"+catid+"' and uid='"+str(row[0])+"'"
        resa=c.selectone(qry)
        if resa is not None:
            catscorepos.append(resa[0])
            catscoreneg.append(resa[1])
            if resa[0]==0:
                catprob.append(0)
            elif resa[1]==0:
                catprob.append(1)
            else:
                catprob.append(resa[0]/resa[1])
        else:
            catscorepos.append(0)
            catscoreneg.append(0)
            catprob.append(0)
        qry="select scorepositive,scorenegative from brand_score where brandname='"+brandname+"' and uid='"+str(row[0])+"'"
        resb=c.selectone(qry)
        if resb is not None:
            brandscorepos.append(resb[0])
            brandscoreneg.append(resb[1])
            if resb[0]==0:
                catprob.append(0)
            elif resb[1]==0:
                catprob.append(1)
            else:
                catprob.append(resb[0]/resb[1])
        else:
            brandscorepos.append(0)
            brandscoreneg.append(0)
            brandprob.append(0)
            catprob.append(0)
        print(str(catprob[indx]),str(cnt))
        if catprob[indx]>.5 and cnt[indx]>4:
            addsubscribers(row[0],productid,ofid)
        indx=indx+1
    return render_template("admin_addoffer_step2.html",users=resbuyedusers,bpos=brandscorepos,bneg=brandscoreneg,cpos=catscorepos,cneg=catscoreneg,ls=len(resbuyedusers),brandprob=brandprob,cnt=cnt)
def addsubscribers(uid,pid,ofid):
    c=conn()
    q="insert into offer_subscribed(uid,ofrid,pid) values('"+str(uid)+"','"+str(ofid)+"','"+str(pid)+"')"
    print(q)
    c.nonreturn("insert into offer_subscribed(uid,ofrid,pid) values('"+str(uid)+"','"+str(ofid)+"','"+str(pid)+"')")



@app.route("/edito",methods=['POST'])
def editoffer():
    oid = request.form['oid']
    productid=request.form['productname']
    offer=request.form['offer']
    ldate=request.form['offerdate']
    qry="update offer set offer='"+offer+"',offr_latdate='"+ldate+"' where offer_id='"+oid+"'"
    print(qry)
    c.nonreturn(qry)
    return admin_viewalloffers()
@app.route('/deleteo/<id>')
def deleteo(id):
    query = "delete from offer where offer_id='" + str(id) + "'"
    i=c.nonreturn(query)
    return admin_viewalloffers()


@app.route("/")
def mainlogin():
    return  render_template('login_main.html')

@app.route("/logout")
def logout():
    return render_template('login_main.html')

@app.route('/index')
def index():
    return  render_template("index.html")


@app.route('/admin_viewstaff')
def admin_viewalloffers():
    rescat=c.selectall("select * from staff")

    return render_template("admin_viewstaff.html",rescat=rescat)

@app.route('/editstaff/<id>')
def editstaff(id):
    session["stfid"]=str(id)
    rescat=c.selectone("select * from staff where staffid='"+str(id)+"'")

    return render_template("admin_editstaff.html",s=rescat)

@app.route('/deletestaff/<id>')
def deletestaff(id):
    c.nonreturn("delete  from staff where staffid='"+str(id)+"'")

    return admin_viewalloffers()


@app.route('/admin_addstaffget')
def admin_addstaffget():
    return render_template("admin_addstaff.html")

@app.route('/adminaddstaffpost',methods=['POST'])
def adminaddstaffpost():
    name=request.form["name"]
    gender=request.form["RadioGroup1"]
    dob=request.form["textfield"]
    hname=request.form["textfield2"]
    place=request.form["textfield3"]
    city=request.form["textfield4"]
    pin=request.form["textfield5"]
    email=request.form["textfield6"]
    phone=request.form["textfield7"]
    image=request.files["fileField"]

    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")

    image.save("C:\\Users\\MyPc\\Desktop\\New folder (4)\\mainproject\\static\\staffimages\\"+timestr+".jpg")
    filename="/static/staffimages/"+timestr+".jpg"
    qry="INSERT INTO staff (NAME,gender,dob,hname,place,city,pincode,emailid,phone,image) VALUES ('"+name+"','"+gender+"','"+dob+"','"+hname+"','"+place+"','"+city+"','"+pin+"','"+email+"','"+phone+"','"+filename+"')"
    c.nonreturn(qry)

    qry="INSERT INTO login (user_name,PASSWORD,TYPE) values ('"+email+"','123456','staff')"
    c.nonreturn(qry)

    return render_template('admin_Addstaff.html')

@app.route('/adminupdatestaffpost',methods=['POST'])
def adminupdatestaffpost():
    id=request.form["id"]
    name=request.form["name"]
    gender=request.form["RadioGroup1"]
    dob=request.form["textfield"]
    hname=request.form["textfield2"]
    place=request.form["textfield3"]
    city=request.form["textfield4"]
    pin=request.form["textfield5"]
    email=request.form["textfield6"]
    phone=request.form["textfield7"]
    image=request.files["fileField"]

    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")

    image.save("C:\\Users\\MyPc\\Desktop\\New folder (4)\\mainproject\\static\\staffimages\\"+timestr+".jpg")
    filename="/static/staffimages/"+timestr+".jpg"
    qry="UPDATE staff SET NAME='"+name+"',`gender`='"+gender+"',`dob`='"+dob+"',`hname`='"+hname+"',`place`='"+place+"',`city`='"+city+"',`pincode`='"+pin+"',`phone`='"+phone+"',`image`='"+filename+"' WHERE `staffid`='"+id+"'"
    c.nonreturn((qry))
    return render_template('admin_editstaff.html')





@app.route('/getproductitemsbycatid',methods=['POST'])
def getproductitemsbycatid():
    cat=request.form['a']
    print(cat)
    json_data = []
    res,cu = c.selectalljson("select * from product where category_id='"+str(cat)+"'")
    if res is not None:
        row_headers = [x[0] for x in cu.description]

        for result in res:
            json_data.append(dict(zip(row_headers, result)))

        print(json_data)


    return jsonify(json_data)


@app.route('/viewusers')
def viewusers():


    query = "select * from user"
    res = c.selectall(query)
    totalitems= len(res)
    noofrows=int(totalitems/3)
    return render_template('admin_customer.html', ac=res,totalitems=totalitems,noofrows=noofrows)

@app.route('/viewproduct')
def viewproduct():
    return render_template('admin_viewproduct.html')
@app.route('/viewp')
def viewp():
    query="select*from product"
    res=c.selectall(query)
    return render_template('admin_viewproduct.html', ac=res)
@app.route('/editpr/<id>')
def editpr(id):
    query="select*from product where product_id='"+str(id)+"'"
    res=c.selectone(query)
    query = "select * from category"

    res2 = c.selectall(query)

    return render_template('admin_editproduct.html',r=res,res2=res2)

@app.route('/editoffr/<id>')
def editoffr(id):
    query = "select*from product"
    res2 = c.selectall(query)

    query="select*from offer where offer_id='"+str(id)+"'"
    res=c.selectone(query)





    return render_template('admin_edit_offer.html',r=res,res2=res2)

@app.route('/user_myanalytics')
def user_myanalytics():
    con=conn()
    res=con.selectall("select brandname,scorepositive,scorenegative from brand_score where uid='"+str(session["id"])+"'")
    res1=con.selectall("select name,scorepos,scoreneg  from category,cat_score where cat_score.catid=category.category_id and uid='"+str(session["id"])+"'")

    print(res)
    print(res1)
    return render_template("user_myanalytics.html",res=res,res1=res1)

@app.route('/editp',methods=['POST'])
def editp():
    productid = request.form['productcode']
    productname = request.form['productname']
    brandname = request.form['brandname']
    price = str(request.form['price'])
    profit=request.form['profit']
    category = request.form['category']
    description = request.form['description']

    if 'profilepicture' in request.files:
        profilepicture = request.files['profilepicture']
        path = "static/userimgs/" + str(productid) + ".jpg"
        profilepicture.save(path)

    query = "update product set product_name='" + productname + "',profit='"+profit+"',brandname='"+brandname+"',price='" + price + "', category_id='" + category + "',details='" + description + "' where product_id='" + str(productid) + "'"
    i=c.nonreturn(query)
    return viewp()
@app.route('/deletep/<id>')
def deletep(id):
    query = "delete from product where product_id='" + str(id) + "'"
    i=c.nonreturn(query)
    return 'ok'
@app.route('/viewsale')
def viewsale():
    return render_template('admin_viewsalesreport.html')
@app.route('/viewsalereport')
def viewsalereport():
    fromdate='1/1/2018'
    # print("frr",fromdate)

    todate='1/1/2018'
    query=" select transaction_master.transaction_id, transaction_master.date, transaction_master.amount, user.name  from transaction_master inner  join user  where transaction_master.transaction_id = user.user_id and transaction_master.date between '"+fromdate+"' to '"+todate+"'"
    res=c.selectall(query)
    siz=len(res)
    print(res)
    if res!=None:
       return render_template('admin_viewsalesreport.html', ac=res,cn=siz)
    else:
        return render_template('admin_viewsalesreport.html')

@app.route('/admin_trans')
def admin_trans():
    return render_template('admin_transcationaldetails.html')
@app.route('/purchasehistory')
def purchasehistory():
    return render_template('user_purchasehistory.html')
@app.route('/viewpurchasehistory')
def viewpurchasehistory():
    query="select transaction_master.transaction_id,transaction_master.date,transaction_master.amount,payment.accountno from transaction_master inner join payment where transaction_master.payment_id=payment.payment_id"
    res=c.selectall(query)
    return render_template('user_purchasehistory.html', ac=res)
@app.route('/payment')
def payment():
    return render_template('user_payment.html')
@app.route('/paymentu',methods=["post"])
def paymentu():
    bank= str(request.form['bank'])
    print(bank)
    accountno=str(request.form['accountnumber'])
    key=str(request.form['key'])
    print(key)
    s="select max(payment_id)from payment"
    print(s)
    payment_id=c.mid(s)
    print(payment_id)
    query="insert into payment(bank,accountno,keyvalue)value('"+bank+"','"+accountno+"','"+key+"')"
    print(query)
    i=c.nonreturn(query)
    return 'ok'
@app.route('/userpage')
def userpage():
    return render_template('userpage.html')
@app.route('/viewprofile')
def viewprofile():
    s1=str(session["id"])
    print(s1)
    s2="select * from user where user_id='"+s1+"'"
    res=c.selectone(s2)
    return render_template("user_myaccount.html",va=res)
@app.route('/viewuser')
def viewuser():
    s1 = str(session["id"])
    s2 = "select * from user where user_id='" + s1 + "'"
    res = c.selectone(s2)
    return render_template("user_editaccount.html", va=res)
@app.route('/editaccount',methods=['POST'])
def editaccount():
    s1=str(session["id"])
    name=request.form['name']
    print(name)
    phoneno = str(request.form['phonenumber'])
    print(phoneno)
    city=request.form['city']
    print(city)
    country=request.form['country']
    print(country)
    addprofilepic = request.files['profilepicture']
    print(addprofilepic)
    user_id=str(session["id"])
    path = "static/userimgs/" + str(user_id) + ".jpg"
    addprofilepic.save(path)
    query= "update user set name='" + name + "',phone='" + phoneno + "',city='" + city + "',country='" + country + "',profilepic='" + path + "' where user_id='"+s1+"'"
    i = c.nonreturn(query)
    return 'ok'
@app.route('/editpassword')
def editpassword():
    return render_template('user_editpassword.html')
@app.route('/epassword',methods=["post"])
def epassword():
    s1 = str(session["id"])
    old=request.form['oldpassword']
    current=request.form['currentpassword']
    confirm=request.form['confirmpassword']
    if current==confirm:
        query="update login set password='"+current+"' where login_id='"+s1+"'"
        i=c.nonreturn(query)
        return 'ok'
    else:
        return 'currentpassword and confirmpassword are different'

@app.route("/savecomment",methods=['POST'])
def savecomment():
    comment=request.form['comment']
    pid=request.form["pid"]
    qry="select category_id,brandname from product where product_id="+str(pid)+""
    c=conn()
    res=c.selectone(qry)
    brandname=res[1]
    catid=res[0]

    uid=session["id"]
    qry="insert into comment (user_id,product_id,comment,date) values ('"+str(uid)+"','"+str(pid)+"','"+comment+"',CURDATE())"
    print(qry)
    c = conn()
    c.nonreturn(qry)

    pstv = 0
    ngtv = 0
    ntl = 0
    sid = SentimentIntensityAnalyzer()

    ss = sid.polarity_scores(comment)
    print(ss)

    a = float(ss['pos'])
    b = float(ss['neg'])
    c = float(ss['neu'])

    sts=""
    if a > b:
        if a > c:
            sts="P"

        else:
            sts="Ne"
    else:
        if b > c:
            sts="Ne"
        else:
            sts="N"

    c=conn()
    if sts== "P":
        c=conn()
        ary="select * from  brand_score where uid='"+str(uid)+"' and brandname='"+brandname+"'"
        print(ary)
        ress=c.selectall(ary)
        print("----------------------------",ress)
        if len(ress)==0:
            qry="insert into brand_score(brandname,uid,scorepositive,scorenegative) values ('"+brandname+"','"+str(uid)+"','1','0')"
            c.nonreturn(qry)
        else:
            qry="update brand_score set scorepositive=scorepositive+1 where uid='"+str(uid)+"' and brandname='"+brandname+"'"
            c.nonreturn(qry)

        ary="select * from cat_score where catid='"+str(catid)+"' and uid='"+str(uid)+"'"
        ress=c.selectall(ary)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",ress)

        if len(ress)==0:
            qry = "insert into cat_Score (catid,scorepos,scoreneg,uid) values ('" + str(catid) + "','1','0','" + str(uid) + "')"
            c.nonreturn(qry)
        else:
            qry="update cat_score set scorepos=scorepos+1 where catid='"+str(catid)+"' and uid='"+str(uid)+"'"
            c.nonreturn(qry)
    elif sts=="Ne":
        print("helllllo")
        ary = "select * from  brand_score where uid='" + str(uid) + "' and brandname='" + brandname + "'"
        print("Abbbbbbbbbbbbbbbbbbbbbbbbbbbb",ary)
        ress = c.selectall(ary)
        if len(ress) == 0:
            qry = "insert into brand_score(brandname,uid,scorepositive,scorenegative) values ('" + brandname + "','" + str(uid) + "','0','1')"
            c.nonreturn(qry)
        else:
            qry = "update brand_score set scorenegative=scorenegative+1 where uid='" + str(uid) + "' and brandname='" + brandname + "'"
            c.nonreturn(qry)

        ary = "select * from cat_score where catid='" + str(catid) + "' and uid='" + str(uid) + "'"
        ress = c.selectall(ary)

        if len(ress) == 0:
            qry = "insert into cat_Score (catid,scorepos,scoreneg,uid) values ('" + catid + "','0','1','" + str(uid) + "')"
            c.nonreturn(qry)
        else:
            qry = "update cat_score set scoreneg=scoreneg+1 where catid='" + str(catid) + "' and uid='" + str(uid) + "'"
            c.nonreturn(qry)

    return comments(pid)


@app.route('/addtocartpost',methods=['POST'])
def addtocartpost():
    pid=request.form['pid']
    uid=session["id"]

    qry="insert into cart_table(userid,pdctid) values ('"+str(uid)+"','"+str(pid)+"')"
    c.nonreturn(qry)

    return mycartget(pid)


@app.route("/paymentfinal",methods=['POST'])
def paymentfinal():

    totamnt=request.form["totamnt"]
    uid = str(session['id'])
    totamnt = request.form["totamnt"]
    tid = c.nonreturn(
        "insert into sales_master(total_amount,date,custid) values ('" + totamnt + "',CURDATE(),'" + uid + "')")
    print(tid)
    qry = "select pdctid from cart_table where userid='" + uid + "'"
    res = c.selectall(qry)
    for a in res:
        c.nonreturn("insert into sales_sub values('" + str(tid) + "','" + str(a[0]) + "','1')")
    c.nonreturn("delete from cart_table where userid='" + uid + "'")
    # c.nonreturn("update bank_dummy set amount=amount- where accountno='" + accno + "'")

    return render_template("usermessage.html", msg="Payment Done successfully")




@app.route("/gettransactionsubbytid/<tid>")
def gettransactionsubbytid(tid):
    qry="select * from product where product_id in (select itemid from sales_sub where transactionid='"+str(tid)+"')"
    res = c.selectall(qry)
    print(res)
    totalitems = len(res)
    noofrows = int(totalitems / 3)
    return render_template('userviewsingletransaction.html', ac=res, totalitems=totalitems, noofrows=noofrows)



@app.route("/getmytransactions")
def getmytransactions():
    uid=str(session['id'])
    res=c.selectall("select * from sales_master where custid='"+uid+"'")
    print(res)
    return render_template("user_mytransaction.html",res=res)




@app.route("/userpaymentsummary")
def userpaymentsummary():
    uid=str(session['id'])
    query = "select product.*,cart_table.cartid from product inner join cart_table on product.product_id = cart_table.pdctid  where userid='" + str(
        uid) + "'"



    print(query)
    res = c.selectall(query)

    query="select sum(price) from product inner join cart_table on product.product_id = cart_table.pdctid  where userid='" + str(
        uid) + "'"
    res1=c.selectone(query)







    return render_template('user_paymentsummary.html', ac=res,total=res1[0])





@app.route('/getitemsinmycart')
def getitemsinmycart():
    uid=session["id"]
    query = "select product.*,cart_table.cartid from product inner join cart_table on product.product_id = cart_table.pdctid  where userid='"+str(uid)+"'"
    print(query)
    res = c.selectall(query)
    totalitems = len(res)
    noofrows = int(totalitems / 3)
    return render_template('userviewcartitems.html', ac=res, totalitems=totalitems, noofrows=noofrows)

@app.route("/removecart/<pid>")
def removecart(pid):
    qry="delete from cart_table where cartid='"+str(pid)+"'"
    c.nonreturn(qry)
    return  getitemsinmycart()


@app.route("/mycartget/<productid>")
def mycartget(productid):
    # query="select comment.comment,comment.date,user.name,user.email,profilepic  from comment inner join user on comment.user_id=user.user_id where comment.product_id='"+productid+"'"
    # res = c.selectall(query)

    query="select * from product"
    res1 = c.selectone(query)



    return render_template('user_mycart.html',pdata= res1)




@app.route("/comment/<productid>")
def comments(productid):
    query="select comment.comment,comment.date,user.name,user.email,profilepic  from comment inner join user on comment.user_id=user.user_id where comment.product_id='"+productid+"'"
    res = c.selectall(query)

    return render_template('user_productcomments.html',data=res,id=str(productid))



@app.route('/showcomment')
def showcomment():
    query = "select user.profilepic,comment.comment,comment.date from comment inner join user where comment_id=user_id"
    res = c.selectall(query)
    print(res)
    return render_template('user_comment.html', ac=res)
@app.route('/comment',methods=["post"])
def comment():
    com=request.form['qr']
    s = "select max(comment_id)from comment"
    i=c.nonreturn(s)
    comment_id=c.mid(s)
    print(comment_id)
    querys="insert into comment (comment)value('"+com+"')"
    print(querys)
    i=c.nonreturn(querys)
    return 'ok'
    # query="select user.profilepicture,comment.comment,comment.date from comment inner join user where user_id=comment_id"
    # res=c.selectall(query)
    # print(res)
    # return render_template('user_comment.html', ac=res)
@app.route('/usersee')
def usersee():
    query="select *from product"
    res=c.selectall(query)

    return render_template('user_seen.html',ac=res)
@app.route('/load_trans')
def load_trans():
    return render_template('admin_hui.html',sz=0,sz1=0)

@app.route('/trans')
def trans():

    d1=request.args.get("dt1")
    d2 = request.args.get("dt2")
    print(d1)
    print(d2)
    transaction1 = []
    qty = []
    profit = []
    tu1 = []

    itmid = []
    itub = []
    ubitm = []
    Ubfpe = []

    c=conn()
    q1 = "SELECT transactionid FROM sales_master"  # WHERE DATE BETWEEN  '"+d1+"' AND '"+d2+"'"
    rs1 = c.selectall(q1)

    for i in range(len(rs1)):
        q2 = "select itemid,quantity from sales_sub where transactionid='" + str(rs1[i][0]) + "' order by itemid"

        rs2 = c.selectall(q2)
        transaction = "";
        quantity = "";
        profitstring = "";
        tu = 0;

        for k in range(len(rs2)):
            q3 = "select profit from product where product_id='" + str(rs2[k][0]) + "'"
            # print('q3',q3)
            rs3 = c.selectone(q3)
            profitstring = profitstring + str(rs3[0]) + ":"
            transaction = transaction + str(rs2[k][0]) + ":"
            quantity = quantity + str(rs2[k][1]) + ":"
            a = int(rs3[0])
            b = int(rs2[k][1])
            cb = a * b;
            tu = tu + cb;

        transaction1.append(transaction)
        qty.append(quantity)
        profit.append(profitstring)
        tu1.append(tu)

    item = []
    iprofit = []

    count = 0
    #     item=' '.join(item).split()
    #     iprofit=' '.join(iprofit).split()
    #     print("it",item)
    #     print("pr",iprofit)
    q5 = "select distinct itemid from sales_sub,sales_master where sales_master.transactionid=sales_sub.transactionid and sales_master.DATE BETWEEN  '"+d1+"' AND '"+d2+"' order by itemid"

    rs5 = c.selectall(q5)
    for i in range(len(rs5)):
        itmid.append(str(rs5[i][0]))
    for i in range(len(itmid)):
        q4 = "select profit from product where product_id='" + str(itmid[i]) + "'"

        rs4 = c.selectone(q4)
        for j in range(len(transaction1)):
            ar3 = transaction1[j].split(":")
            ar4 = qty[j].split(":")
            ar4 = ' '.join(ar4).split()
            ar3 = ' '.join(ar3).split()
            #             print("ar3",ar3)
            #             print(ar4)
            for k in range(len(ar3)):
                if (str(itmid[i]) == str(ar3[k])):
                    q = int(ar4[k])
                    count = count + q

        ut = int(rs4[0]) * count

        itub.append(ut)
        count = 0

    # ubitem
    for i in range(len(itub)):
        item_id = itmid[i]
        ubitem = 0
        for j in range(len(transaction1)):
            trans_action = transaction1[j]
            tru = int(tu1[j])
            sp = trans_action.split(':')
            for m in range(len(sp)):
                if (str(sp[m]) == item_id):
                    ubitem = ubitem + tru;
                    break

        ubitm.append(str(ubitem))

    # ubfpe
    for i in range(len(itub)):
        item_id = itmid[i]
        ubf_pe = 0
        for j in range(len(transaction1)):
            trans_action = transaction1[j]
            quan_tity = qty[j]
            prof_it = profit[j]
            ar1 = trans_action.split(':')
            ar2 = quan_tity.split(':')
            ar3 = prof_it.split(':')
            for m in range(len(ar1)):
                if (str(ar1[m]) == item_id):
                    itemidPosition = m
                    k = itemidPosition
                    while (k >= 0):
                        x = int(ar2[k]);
                        y = int(ar3[k]);
                        z = x * y;
                        ubf_pe = ubf_pe + z;
                        k = k - 1;

        Ubfpe.append(str(ubf_pe))
    session["trans"] = transaction1
    session["prof"] = profit
    session["qty"] = qty
    session["tu"] = tu1
    session["itmid"] = itmid
    session["itu"] = itub
    session["ubitm"] = ubitm
    session["ubfp"] = Ubfpe
    tid=[]
    for i in range(len(rs1)):
        tid.append(str(rs1[i][0]))


    return jsonify(data='ok',  tr=transaction1, qun=qty, prf=profit, tuu=tu1,r1=tid, itid=itmid, itu=itub, ub=ubitm, ubfp_e=Ubfpe)
@app.route('/dhup')
def dhup():
    q1 = "SELECT product_id FROM product order by product_id"
    rs1 = c.selectall(q1)
    itemstring = []
    newaddeditem = []
    u = []
    ubitem = []
    ubfpe = []
    status = []
    minu = request.args.get("min")
    trans = session["trans"]
    prof = session["prof"]
    qty = session["qty"]
    Sitmid = session["itmid"]
    Subfpe = session["ubfp"]
    Situ = session["itu"]
    Subitm = session["ubitm"]
    loopindex = 0
    for i in range(len(Sitmid)):
        utility = int(Subfpe[i])
        if (utility >= int(minu)):
            itemstring.append(Sitmid[i])
            newaddeditem.append("")
            u.append(Situ[i])
            ubitem.append(Subitm[i])
            ubfpe.append(Subfpe[i])
            status.append("pending")
    while (loopindex < len(itemstring)):
        ub_fpe = int(ubitem[loopindex])
        pattern = itemstring[loopindex]
        patternnexcoloumn = newaddeditem[loopindex]
        if (patternnexcoloumn != ""):
            pattern = pattern + ":" + str(patternnexcoloumn)
        patternend = pattern[len(pattern) - 1]

        subitems = getremainingprefixitems(patternend, rs1)
        for m in range(len(subitems)):
            newpattern = pattern + ":" + str(subitems[m])
            ubitem_sub = 0
            u_sub = 0
            ubfpe_sub = 0

            r1, r2, r3 = traverse(newpattern, trans, minu, u_sub, ubitem_sub, ubfpe_sub, trans, qty, prof, rs1)

            if (r1 >= int(minu)):
                itemstring.append(pattern)
                newaddeditem.append(subitems[m])
                u.append(r3)
                ubitem.append(r2)
                ubfpe.append(r1)
                status.append("pending")

        status[loopindex] = "done"
        loopindex = loopindex + 1
    HHH = 0

    session["its"] = itemstring
    session["nad"] = newaddeditem
    session["ubfpe"] = ubfpe

    return jsonify(data='ok', itst=itemstring, nad=newaddeditem, ut=u, ub=ubitem, ubf=ubfpe, sta=status)


@app.route('/tpkit')
def tpkit():
    HUIITEM = []
    UBFPE = []
    ITNM=[]

    itst = session["its"]
    print(itst)
    nad = session["nad"]
    print("nad",nad)
    ubfpe = session["ubfpe"]
    print("ubfpe",ubfpe)

    for i in range(len(itst)):
        #                      //itemstring
        #                 //newaddeditem
        #                 //ubfpe
        print(itst[i])

        c1=itst[i].split(":")
        hh=""

        for k in range(len(c1)):
            print("c",c1[k])

            q1 = "SELECT product_name FROM product where product_id='"+str(c1[k])+"'"
            print(q1)
            rs1 = c.selectone(q1)
            hh=hh+rs1[0]+","




        print("hh",hh)
        ITNM.append(hh)

        h = itst[i] + ":" + str(nad[i])
        d = int(ubfpe[i])
        HUIITEM.append(str(h))
        UBFPE.append(str(d))



    for passnum in range(len(UBFPE) - 1, 0, -1):

        for i in range(passnum):
            if int(UBFPE[i]) < int(UBFPE[i + 1]):
                temp = UBFPE[i]
                UBFPE[i] = UBFPE[i + 1]
                UBFPE[i + 1] = temp

                temp1 = HUIITEM[i]
                HUIITEM[i] = HUIITEM[i + 1]
                HUIITEM[i + 1] = temp
    print(ITNM)

                #                 dtfinal.Rows.Add(h, d);
    return jsonify(data='ok', hut=HUIITEM, ubfp=UBFPE,itn=ITNM)


@app.route('/assignworks/<wid>')
def assignworks(wid):
    c=conn()
    qry="select * from staff"
    res=c.selectall(qry)
    return render_template('admin_assignorder.html',data=res,r=wid)

@app.route('/inswork',methods=['post'])
def inswork():
    wid=request.form["wid"]
    staffid=request.form["sid"]
    c=conn()
    qry="INSERT INTO `order_assign` (`orderid`,`staffid`,`status`,`dates`) VALUES ('"+wid+"','"+staffid+"','pending',CURDATE())"
    c.nonreturn(qry)
    return "ok"






@app.route('/andlogin',methods=['POST'])
def andlogin ():
    c=conn()

    uname=request.form["username"]
    pasword=request.form["password"]


    qry="SELECT `staff`.`staffid` FROM `login`,staff WHERE login.user_name=staff.emailid AND    `user_name`='"+uname+"' AND PASSWORD='"+pasword+"' AND TYPE='staff' "
    res=c.selectone(qry)

    if res is not None:
        return jsonify(status='ok',uid=res[0])
    else:
        return jsonify(status='mo')

@app.route('/usergetassigned',methods=['POST'])
def usergetassigned():
    uid=request.form["uid"]
    qry="select user.name,email,phone,place,date,total_amount,sales_master.transactionid,`profilepic` from sales_master,user where sales_master.custid=user.user_id and sales_master.`transactionid`   IN ( SELECT `orderid` FROM `order_assign` where status='pending' and staffid='"+uid+"') "
    c=conn()
    res=c.jsonselect(qry)
    return jsonify(status='ok',res=res)


@app.route('/usergetassignedsearch',methods=['POST'])
def usergetassignedsearch():
    uid=request.form["uid"]
    sr=request.form["sr"]

    qry="select user.name,email,phone,place,date,total_amount,sales_master.transactionid,profilepic from sales_master,user where sales_master.custid=user.user_id and sales_master.`transactionid` NOT IN ( SELECT `orderid` FROM `order_assign` where status='pending' and staffid='"+uid+"')  and name like '%"+sr+"%'"
    c=conn()
    res=c.jsonselect(qry)
    return jsonify(status='ok',res=res)

@app.route('/usergetcompltedeassignedsearch',methods=['POST'])
def usergetcompltedeassignedsearch():
    uid=request.form["uid"]
    sr=request.form["sr"]

    qry="select user.name,email,phone,place,date,total_amount,sales_master.transactionid,profilepic from sales_master,user where sales_master.custid=user.user_id and sales_master.`transactionid`  IN ( SELECT `orderid` FROM `order_assign` where status='completed' and staffid='"+uid+"')  and name like '%"+sr+"%'"
    c=conn()
    res=c.jsonselect(qry)
    return jsonify(status='ok',res=res)

@app.route('/getordererdproducts',methods=['POST'])
def getordererdproducts():
    wid=request.form["wid"]
    c=conn()
    qry="SELECT `product`.`product_id`,`product_name`,`price`,`profile_picture`,sales_sub.quantity FROM `product` INNER JOIN `sales_sub` ON `product`.`product_id`=`sales_sub`.`itemid` WHERE `transactionid`="+wid+""
    res=c.jsonselect(qry)
    return jsonify(status='ok',res=res)


@app.route('/updatestatus',methods=['POST'])
def updatestatus():
    wid=request.form["workid"]
    c=conn()
    qry="UPDATE `order_assign` SET `status`='completed' WHERE `orderid`='"+wid+"'"
    c.nonreturn(qry)
    return jsonify(status='ok')



@app.route('/usergetcompleted',methods=['POST'])
def usergetcompleted():
    uid=request.form["uid"]
    qry="select user.name,email,phone,place,date,total_amount,sales_master.transactionid from sales_master,user where sales_master.custid=user.user_id and sales_master.`transactionid` NOT IN ( SELECT `orderid` FROM `order_assign` where status='completed' and staffid='"+uid+"') "
    c=conn()
    res=c.jsonselect(qry)
    return jsonify(status='ok',res=res)




if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')