from flask import Flask, render_template, url_for, request
import sqlite3
from train_predict import Predict
from emotion import Detection
import os
connection = sqlite3.connect('user_data.db')
cursor = connection.cursor()

command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
cursor.execute(command)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('animal.html')

@app.route('/userlog', methods=['GET', 'POST'])
def userlog():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']

        query = "SELECT name, password FROM user WHERE name = '"+name+"' AND password= '"+password+"'"
        cursor.execute(query)

        result = cursor.fetchall()

        if result:
            return render_template('emotion.html')
        else:
            return render_template('index.html', msg='Sorry, Incorrect Credentials Provided,  Try Again')

    return render_template('index.html')


@app.route('/userreg', methods=['GET', 'POST'])
def userreg():
    if request.method == 'POST':

        connection = sqlite3.connect('user_data.db')
        cursor = connection.cursor()

        name = request.form['name']
        password = request.form['password']
        mobile = request.form['phone']
        email = request.form['email']
        
        print(name, mobile, email, password)

        command = """CREATE TABLE IF NOT EXISTS user(name TEXT, password TEXT, mobile TEXT, email TEXT)"""
        cursor.execute(command)

        cursor.execute("INSERT INTO user VALUES ('"+name+"', '"+password+"', '"+mobile+"', '"+email+"')")
        connection.commit()

        return render_template('index.html', msg='Successfully Registered')
    
    return render_template('index.html')

@app.route('/emotion', methods=['GET', 'POST'])
def emotion():
    if request.method == 'POST':
        img1 = request.form['img1']
        Detection('static/test/emotion/'+img1)
        return render_template('emotion.html', image = 'http://127.0.0.1:5000/static/test/emotion/'+img1, image2 = 'http://127.0.0.1:5000/static/result/frame.png')
    return render_template('emotion.html')

@app.route('/handwritten', methods=['GET', 'POST'])
def handwritten():
    if request.method == 'POST':
        img2 = request.form['img2']
        Predict('static/test/handwritten/'+img2)
        f = open('data.txt', 'r')
        data = f.read()
        data = data.split('\n')
        f.close()
        print(data)
        return render_template('handwritten.html', result=data, image = 'http://127.0.0.1:5000/static/test/handwritten/'+img2)
    return render_template('handwritten.html')

@app.route('/Live')
def Live():
    os.system('python live_emotion.py')
    return render_template('handwritten.html')

@app.route('/logout')
def logout():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
