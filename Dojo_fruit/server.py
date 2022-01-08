from flask import Flask, render_template, request, redirect
from datetime import datetime
app = Flask(__name__)

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    order_info = {
        'strawberry':request.form['strawberry'],
        'raspberry':request.form['raspberry'],
        'apple':request.form['apple'],
        'firstName':request.form['first_name'],
        'lastName':request.form['last_name'],
        'studentId':request.form['student_id']

        # include K/V of all fruits and user info inside dict. 
        } 
    print(order_info)
    return render_template("checkout.html", order = order_info,date_time = date_time)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")


if __name__=="__main__":   
    app.run(debug=True)