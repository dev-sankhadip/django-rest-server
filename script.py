from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
from flaskext.mysql import MySQL

app=Flask(__name__)
CORS(app)

mysql=MySQL()

app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='telecom'
app.config['MYSQL_DATABASE_HOST']='localhost'

mysql.init_app(app)


conn=mysql.connect()
cursor=conn.cursor()


@app.route('/android/signup',methods=['POST'])
def signup():
    print(request.form['url'])
    cursor.execute("select * from netinfo")
    print(cursor.fetchall())
    return "sankha"






if __name__=="__main__":
    app.run(debug=True, port=3000)