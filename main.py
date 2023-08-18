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

# Update the record
@app.route("/update", methods = ['POST'])
def update():
    if request.method == 'POST':
        get_name = request.json["get_name"]
        cursor.execute("update taskdb.tasktable set number = number + 500 where name = %s ", (get_name, ))
        mydb.commit()
        return jsonify(str("Updated successfully"))

# Delete something from the record
@app.route("/delete", methods=['POST'])
def delete():
    if request.method=='POST':
        name_delete = request.json["name_delete"]
        cursor.execute("Delete from taskdb.tasktable where name = %s ", (name_delete,))
        mydb.commit()
        return jsonify(str("Deleted successfully"))

# Fetch data
@app.route("/fetch", methods=['POST','GET'])
def fetch_data():
    cursor.execute("select*from taskdb.tasktable")
    l=[]
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))

if __name__ == "__main__":
    app.run()

# Task---- read a file, give complete file path on api side. It should read the file and give a summary of the file
