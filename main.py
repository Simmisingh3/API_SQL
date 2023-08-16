from flask import Flask ,request,jsonify
import mysql.connector as conn

app = Flask(__name__)

mydb = conn.connect(host = "localhost" , user = 'root' , passwd = "SIMMIs@0003")
cursor = mydb.cursor()
cursor.execute("create database if not exists taskdb")
cursor.execute("create table if not exists taskdb.tasktable (name varchar(30) , number int)")


# creating functions to insert record inside the table
@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method=='POST':
        name = request.json["name"]
        number = request.json["number"]
        cursor.execute("insert into taskdb.tasktable values(%s, %s)", (name , number))
        mydb.commit()
        return jsonify(str("successfully inserted"))

if __name__ == "__main__":
    app.run()