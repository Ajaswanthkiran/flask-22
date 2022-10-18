from flask import Flask,render_template,redirect,url_for,request

import mongod__

app=Flask(__name__)

@app.route('/')
def sample():
    return render_template('home.html')

@app.route('/nav')
def sample2():
    return render_template('nav_bar.html')
@app.route("/labtest")
def lab():
    return render_template('labtest.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')

@app.route("/medi")
def med():
    return render_template('medi.html')

@app.route('/nibbi',methods=["POST","GET"])

def nibbi():
    if request.method == 'POST':
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        uname = request.form.get("username")
        email = request.form.get("email")
        pword = request.form.get("password")
        mongod__.mg(fname, lname, uname,email,pword)
        return render_template('signup.html')
    else:
        return "welcome"

@app.route('/con',methods=["POST","GET"])

def check():
    if request.method == 'POST':
        email = request.form.get("email")
        passw = request.form.get("passw")
        a=mongod__.check_it(email)
        db = mongod__.db
        if(db.details.find_one({'email' : email},{"email":1,"_id": False})):
            return render_template('after_login.html',email=email)
        else:
            return 'data'
    else:
        return "welcome"

if __name__=='__main__':
    app.run(debug=True)