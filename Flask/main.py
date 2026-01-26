from flask import Flask,render_template
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.This should be an amazing course"

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/aboutus")
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)