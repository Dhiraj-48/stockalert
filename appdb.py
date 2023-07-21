import sqlite3  
  
con = sqlite3.connect("stock.db")  
# print("Database opened successfully")  
  
# con.execute("create table Users (id INTEGER PRIMARY KEY AUTOINCREMENT, email TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")  
# con.execute("create table Ustock(cticker TEXT UNIQUE NOT NULL,low INTEGER NOT NULL, high INTEGER NOT NULL)")

# print("Table created successfully")  
  
# con.close() 






# test code section //not completed
# cursor=con.cursor()
# ct=cursor.execute("SELECT cticker FROM Ustock WHERE ID = (SELECT MAX(ID)  FROM Ustock);")
# results=cursor.fetchone()
# print(results)
# print(type(results))


# import yfinance as yf
# from datetime import date,timedelta

# today=date.today()
# ed=today.strftime("%Y-%m-%d")
# before=today-timedelta(days=365)
# sd=before.strftime("%Y-%m-%d")


# cticker="SELECT cticker FROM Ustock;"



# df=yf.download(results,start=sd,end=ed)
# df['Date']=df.index
# df=df[['Date','Open','High','Low','Close','Adj Close','Volume']]
# df.reset_index(drop=True,inplace=True)
# print(df)
# l=df['Low']
# l=l[-1:]
# print(l)
# h=df['High']
# h=h[-1:]
# print(h)
# completing it soon.......