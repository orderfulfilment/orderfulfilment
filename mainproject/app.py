from flask import Flask,render_template,request
from  dbconnection import conn
from flask.globals import session
app = Flask(__name__)
app.secret_key='hi'

app.route('/show')
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
    c=conn()
    s="select max(user_id)from user"
    print(s)
    user_id=c.mid(s)
    print(user_id)
    path="static/user_img/"+user_id+".jpg"
    addprofilepic.save(path)
    query ="insert into user(name,email,password,phone,place,city,country,profilepic)values('"+name+"','"+password+"','"+phoneno+"','"+place+"','"+city+"','"+country+"','"+path+"')"
    print(query)
    query1="insert into login(user_name,password,type) values('"+name+"','"+password+"','user')"
    print(query1)
    i=c.nonreturn(s)
    return i

if __name__ == '__main__':
    app.run(debug=True,port=3000)
