from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/testfun")
def test():
    get_name = request.args.get("get_name")
    mobile_number = request.args.get("mobile")
    mail_id = request.args.get("mail_id")
    #return "This is my first function for get {} ".format(get_name)
    return "The mail id and phone number of {} is {} and {}".format(get_name, mail_id, mobile_number)

if __name__=='__main__':
    app.run(port=5002)

#Type this on the browser for answer- http://127.0.0.1:5002/testfun?get_name=simmi singh
#http://127.0.0.1:5002/testfun?get_name=simmi%20singh%20&mail_id=simmisingh22299@gmail.com%20&mobile=9234567879