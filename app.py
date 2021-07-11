from flask.wrappers import Request
import requests
import json
from flask import Flask, json,render_template,request, redirect, url_for, flash ,jsonify

# from flask_ngrok import run_with_ngrok

import sqlite3

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.exc import SQLAlchemyError
import os

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "student.db"))

app = Flask(__name__)
# run_with_ngrok(app)

# dbstuff

app.secret_key = "Secret Key"

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    name = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    bloodtype = db.Column(db.String(80),nullable=False)
    location = db.Column(db.String(80),nullable=False)
    country = db.Column(db.String(80),nullable=False)
    gender = db.Column(db.String(80),nullable=False)
    recoverydate = db.Column(db.String(80),nullable=False)
    
    def __init__(self,name,bloodtype,location,country,recoverydate,gender): 
        self.name =  name
        self.bloodtype = bloodtype
        self.location = location
        self.country = country
        self.gender  = gender
        self.recoverydate = recoverydate




#this route is for inserting data to mysql database via html forms
@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == 'POST':

        name = request.form["name"]              
        location = request.form["location"]
        country = request.form["country"]
        recoverydate = request.form["recoverydate"]
        gender = request.form["gender"]
        bloodtype = request.form["bloodtype"]

        try:
            my_data = Student(name,bloodtype,location,country,recoverydate,gender)
            db.session.add(my_data)
            db.session.commit()
        except SQLAlchemyError as e:
            error = str(e.__dict__['orig'])
        
        

        return redirect(url_for('index'))


#this is our update route where we are going to update our employee
@app.route('/update', methods = ['GET','POST'])
def update():
    if request.method == 'POST':
        my_data = Student.query.get(request.form.get('oldname'))
        my_data.name = request.form["oldname"]              
        my_data.location = request.form["location"]
        my_data.country = request.form["country"]
        my_data.recoverydate = request.form["recoverydate"]
        my_data.gender = request.form["gender"]
        my_data.bloodtype = request.form["bloodtype"]

        db.session.commit()
        return redirect(url_for('index'))


#This route is for deleting our employee
@app.route('/delete/<name>/', methods = ['GET', 'POST'])
def delete(name):
    my_data = Student.query.get(name)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('index'))



@app.route('/' , methods=['GET' ,'POST'])
def index():
    if(request.method == 'POST'):
        return render_template('index.html',title = "Covid Tracker",data='POST')
    all_data = Student.query.all()
    result = requests.get('https://corona.lmao.ninja/v2/continents?yesterday=true&sort=true')
    data = json.loads(result.content)
    print(data[0]['continent'])
    return render_template('index.html',title = "Covid Tracker",result = data ,employees = all_data )


# @app.route('/conitnent/<name>' , methods=['GET' ,'POST'] )   #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
# def continent(name):  
#     if(request.method == 'POST'):
#         print('continent = ' +  name)
#         continent = name
#         url = "https://corona.lmao.ninja/v2/continents/" + continent+ "?yesterday&strict"

#         payload={}
#         headers = {}

#         response = requests.request("GET", url, headers=headers, data=payload)

#         # print(response.text)
#         name = response.json()['countries']
#         listToStr = ','.join(name)
#         # print(type(listToStr))
#         print(listToStr)
#         return redirect(url_for('get_countries',name =listToStr ))
#     return render_template('404.html',title = "Covid Tracker",result = "404 not-Found")


@app.route('/hi',methods=['POST'])
def hi():
    print(request.form['data'])
    continent = request.form['data']  
    url = "https://corona.lmao.ninja/v2/continents/" + continent+ "?yesterday&strict"
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.text)
    name = response.json()['countries']
    listToStr = ','.join(name)
    # print(type(listToStr))
    print(listToStr)
    return jsonify(url = '/countries', params = listToStr , status = 'OK')
    # return redirect(url_for('get_countries',name =listToStr ))
    # return render_template('404.html',title = "Covid Tracker",result = 'fafafaf')
    # return render_template('index.html',title = "Covid Tracker",result = listToStr)


@app.route('/continent' , methods=['GET' ,'POST'] )   #int has been used as a filter that only integer will be passed in the url otherwise it will give a 404 error
def continent():  
    if request.method == 'POST':
        # print('continent = ' +  str(request.get_json()))
        # return request.get_json()
        # continent =  request.args()
        # print(type(continent))
        print(request.json['data'])
        print(request.form['data'])
    return render_template('404.html',title = "Covid Tracker",result = request.json['data'])
        # continent = name
        # url = "https://corona.lmao.ninja/v2/continents/" + continent+ "?yesterday&strict"

        # payload={}
        # headers = {}

        # response = requests.request("GET", url, headers=headers, data=payload)

        # # print(response.text)
        # name = response.json()['countries']
        # listToStr = ','.join(name)
        # # print(type(listToStr))
        # print(listToStr)
        # return redirect(url_for('get_countries',name =listToStr ))
    return render_template('404.html',title = "Covid Tracker",result = "404 not-Found")



@app.route('/countries/<name>')
def get_countries(name):
    # print(type(name))

    url = "https://corona.lmao.ninja/v2/countries/"+str(name)+"?yesterday"

    payload={}
    headers = {}

    result = requests.request("GET", url, headers=headers, data=payload)

    data = json.loads(result.content)
    print(data[0]['continent'])
    return render_template('country.html',title = "Covid Tracker",result = json.loads(result.content))
    # return jsonify(status='OK' , result = response.text)


@app.route('/countryData/<country>')
def countryData(country):
    query = country
    url = "https://corona.lmao.ninja/v2/countries/"+query+"?yesterday&strict&query "
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    data = json.loads(response.content)
    print(data)
    return render_template('oneCountry.html',title = "Covid Tracker",data = data)

if __name__ == "__main__":
    app.run()