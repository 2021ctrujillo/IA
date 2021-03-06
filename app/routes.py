3import os
from app import app
from flask import render_template, request, redirect
from app.models import model



from flask_pymongo import PyMongo

# name of database
app.config['MONGO_DBNAME'] = "test"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:Funnyturtle40@cluster0-iwlen.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)


# INDEX



@app.route('/')
@app.route('/index', methods = ["get", "post"])
def index():
    collection = mongo.db.compsci
    events = list(collection.find({}))
    return render_template('index.html', events = events)



@app.route('/add', methods = ["get", "post"])
def add():
    if request.method == "GET":
        return render_template('add.html')
    else:
        try:
            user_info = dict(request.form)
            print(user_info)

            event_name = user_info["event_name"]
            event_startdate = user_info["event_startdate"]
            event_enddate = user_info["event_enddate"]
            event_category = user_info["category"]
            event_starttime = user_info["event_starttime"]
            event_endtime = user_info["event_endtime"]
            collection = mongo.db.compsci

            collection.insert({"event_name": event_name, "event_startdate": event_startdate, "event_enddate": event_enddate, "event_category": event_category, "event_endtime": event_endtime, "event_starttime": event_starttime})
            return redirect('/index')
        except:
            return render_template('errormessage.html')


@app.route('/results', methods = ["get", "post"])
def results():

    return redirect('/index')


@app.route('/myday', methods = ['get', 'post'])
def myday():
    percentages = model.peritem()
    reccomend = model.rec()
    saythis = model.reccomend()
    return render_template('myday.html', percentages = percentages, reccomend = reccomend, saythis = saythis)


@app.route('/delete')
def delete():
    collection = mongo.db.compsci
    collection.delete_many({})
    return redirect('/index')


@app.route('/test', methods = ["get", "post"])
def test():
    collection = mongo.db.compsci
    thing = model.reccomend()
    print (thing)

    return "go check the terminal"
