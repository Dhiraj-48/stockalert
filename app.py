from flask import *
import sqlite3  
from flask_mail import Mail, Message


app = Flask(__name__)  
app.secret_key = 'thisissecretkey'


# configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'dhirasu.48@gmail.com'
app.config['MAIL_PASSWORD'] = 'vocktettitadfdkp'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True

mail = Mail(app)




@app.route("/")
def welcome():
    return render_template("welcome.html")


@app.route("/register")  
def index():  
    return render_template("register.html"); 

@app.route("/login",methods=['POST','GET'])
def login():
    msg = "msg"  
    if request.method == "POST":  
        try:  
            email = request.form["email"]  
            password= request.form["password"]  
            with sqlite3.connect("stock.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into Users (email,password) values (?,?)",(email,password))  
                con.commit()  
                msg = "Successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add to the list"  
        finally:  
            return render_template("login.html",msg = msg)  
            con.close() 





@app.route('/home',methods=['GET','POST'])
def home():
    msg='Dont have account, first register!'
    if request.method=='POST':
        connection=sqlite3.connect('stock.db')
        cursor=connection.cursor()
        print(cursor)

        email=request.form['email']
        password=request.form['password']
        # print(name,password)
        query="SELECT email,password FROM Users WHERE email='"+email+"' and password='"+password+"'"
        cursor.execute(query)
        results=cursor.fetchall()
        # print(results)
        # print(len(results))

        if len(results)==0:
            print("Sorry")

        else:
            return render_template("home.html")

    return render_template('login.html',msg=msg)



import yfinance as yf
from datetime import date,timedelta

@app.route("/hold",methods=['POST','GET'])
def hold():
    if request.method=="POST":
        cticker= request.form["ticker"]  
        low= request.form["low"]
        high= request.form["high"]
        em=request.form["emaill"]
        today=date.today()
        ed=today.strftime("%Y-%m-%d")
        before=today-timedelta(days=5)
        sd=before.strftime("%Y-%m-%d")
        df=yf.download(cticker,start=sd,end=ed)
        df['Date']=df.index
        df=df[['Date','Open','High','Low','Close','Adj Close','Volume']]
        df.reset_index(drop=True,inplace=True)
        yf_high=df['High']
        yf_low=df['Low']


        for i in yf_high:
            if float(high)<=i:
               
                msg=Message(subject="Target high price reached",
                            sender="dhirasu.48@gmail.com",
                            recipients=['nagarkotidhiraj@gmail.com'])
                msg.body=f'The target highest price of {high} for {cticker} has been reached if you want to sell it is the right time.'
                mail.send(msg)

                flash('Email sent successfully.')
            else:
                flash(f'Target price of {high} has not been reached.')


        for l in yf_low:
            if float(low)>=l:
                msg=Message(subject="Target low price reached",
                            sender="dhirasu.48@gmail.com",
                            recipients=['nagarkotidhiraj@gmail.com'])
                msg.body=f'The target lowest price of {low} for {cticker} has been reached if you want to buy it is the right time.'
                mail.send(msg)

                flash('Email sent successfully.')
            else:
                flash(f'Target price of {low} has not been reached.')


    return render_template('hold.html')







# The following code is incomplete and will be deleted if the above code works

# @app.route("/hold",methods=['POST','GET'])
# def hold():
#     msg = "msg"  
#     if request.method == "POST":  
#         try:  
#             cticker= request.form["ticker"]  
#             low= request.form["low"]
#             high= request.form["high"]  
#             with sqlite3.connect("stock.db") as con:  
#                 cur = con.cursor()  
#                 cur.execute("INSERT into Ustock (cticker,low,high) values (?,?,?)",(cticker,low,high))  
#                 con.commit()  
#                 msg = "Successfully Added"  
#         except:  
#             con.rollback()  
#             msg = "We can not add to the list"  
#         finally:  
#             return render_template("hold.html",msg = msg)  
#             con.close() 


# message ko condition meet vayo vane email pathauna
# this code section is not completed



# import yfinance as yf
# from datetime import date,timedelta

# @app.route('/success',methods=['GET','POST'])
# def success():
#     msg=''
#     if request.method=='POST':
#         try:
#             connection=sqlite3.connect('stock.db')
#             cursor=connection.cursor()

            # cticker=cursor.execute("SELECT cticker FROM Ustock")
            # results=cursor.fetchone()
            # results= request.form["ticker"]
            # today=date.today()
            # ed=today.strftime("%Y-%m-%d")

            # before=today-timedelta(days=365)
            # sd=before.strftime("%Y-%m-%d")

            # df=yf.download(results,start=sd,end=ed)
            # df['Date']=df.index
            # df=df[['Date','Open','High','Low','Close','Adj Close','Volume']]
            # df.reset_index(drop=True,inplace=True)

            # l=df['Low']
            # l=l[-1:]


            # h=df['High']
            # h=h[-1:]

            # query="SELECT low,high FROM Ustock WHERE low='"+l+"'and high='"+h+"'"
            # cursor.execute(query)
            # result=cursor.fetchall()
            # print(results)
            # print(len(results))

        #     if len(result)==0:
        #         print("Sorry",msg=df)

        #     else:
        #         return render_template("success.html")
        # finally:
        #      return render_template('hold.html',msg=msg)

# upto here







# to make debug true so we dont need to rerun app every time we make changes
if __name__ == "__main__":  
    app.run(debug = True) 