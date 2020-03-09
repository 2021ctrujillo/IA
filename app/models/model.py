import os
from app import app
from flask import render_template, request, redirect
from datetime import datetime, date, timedelta
from flask_pymongo import PyMongo

# import pandas as pd
# import datetime as dt


app.config['MONGO_DBNAME'] = "test"

# URI of database
app.config['MONGO_URI'] = "mongodb+srv://admin:Funnyturtle40@cluster0-iwlen.mongodb.net/test?retryWrites=true&w=majority"

mongo = PyMongo(app)

def makedatetime(date, time):

  split_date = date.split("-")
  year = int(split_date[0])
  month = int(split_date[1])
  day = int(split_date[2])

  split_time = time.split(":")
  hour = int(split_time[0])
  minute = int(split_time[1])

  return datetime(year = year, month = month, day = day, hour = hour, minute = minute)

def duration(event_startdate, event_enddate, event_starttime, event_endtime):
    start = makedatetime(event_startdate, event_starttime)
    end = makedatetime(event_enddate, event_endtime)
    duration = end - start
    # print (duration)
    return duration


def catime ():
    collection = mongo.db.compsci
    allfamitems = list(collection.find({"event_category": "Family"}))
    allworkitems = list(collection.find({"event_category": "Work"}))
    alltravelitems = list(collection.find({"event_category": "Travel"}))
    allsocialitems = list(collection.find({"event_category": "Social"}))
    allrelationshipitems = list(collection.find({"event_category": "Relationship"}))
    # print (allfamitems)
    # print (allworkitems)
    # print (alltravelitems)
    # print (allsocialitems)
    # print (allrelationshipitems)
    catdictionary = {"familydd": timedelta(0,0,0,0,0), "workdd": timedelta(0,0,0,0,0), "traveldd": timedelta(0,0,0,0,0), "socialdd": timedelta(0,0,0,0,0), "relationshipdd": timedelta(0,0,0,0,0)}
    for item in allfamitems:
        catdictionary["familydd"] += duration(item["event_startdate"], item['event_enddate'], item['event_starttime'], item['event_endtime'])
    for item in allworkitems:
        catdictionary["workdd"] += duration(item["event_startdate"], item['event_enddate'], item['event_starttime'], item['event_endtime'])
    for item in alltravelitems:
        catdictionary["traveldd"] += duration(item["event_startdate"], item['event_enddate'], item['event_starttime'], item['event_endtime'])# startdates = list(collection.find({"event_startdate"}))
    for item in allsocialitems:
        catdictionary["socialdd"] += duration(item["event_startdate"], item['event_enddate'], item['event_starttime'], item['event_endtime'])
    for item in allrelationshipitems:
        catdictionary["relationshipdd"] += duration(item["event_startdate"], item['event_enddate'], item['event_starttime'], item['event_endtime'])
    # print (catdictionary)
    # print (catdictionary["relationshipdd"].days)
    return catdictionary

def totalseconds():
    catdictionary = catime()
    days = 0
    seconds = 0
    for item in catdictionary:
        days += catdictionary[item].days
        seconds += catdictionary[item].seconds

    # print("the number of days is " + str(days))
    days = days*24*60*60
    # print("the number of seconds is " + str(seconds))
    totalseconds = seconds + days
    # print("the total number of seconds is " + str(totalseconds))
    return totalseconds


def peritem():
    catdictionary = catime()
    days = 0
    minutes = 0
    famsec = (catdictionary["familydd"].days * 24*60*60) + catdictionary["familydd"].seconds
    worksec = (catdictionary["workdd"].days * 24*60*60) + catdictionary["workdd"].seconds
    travelsec = (catdictionary["traveldd"].days * 24*60*60) + catdictionary["traveldd"].seconds
    socialsec = (catdictionary["socialdd"].days * 24*60*60) + catdictionary["socialdd"].seconds
    relationshipsec = (catdictionary["relationshipdd"].days * 24*60*60) + catdictionary["relationshipdd"].seconds
    x = totalseconds()

    print("Seconds for each category:")
    print(famsec)
    print(worksec)
    print(travelsec)
    print(socialsec)
    print(relationshipsec)
    print("Total seconds is:")
    print(totalseconds())
    print("That was total seconds")

    familypercentage = round(famsec / x *100, 2)
    workpercentage = round(worksec / x *100,2)
    travelpercentage = round(travelsec / x *100,2)
    socialpercentage = round(socialsec / x *100,2)
    relationshippercentage = round(relationshipsec / x *100,2)

    percentages = {"familyper" : familypercentage, "travelper" : travelpercentage, "workper" : workpercentage, "socialper" : socialpercentage, "relationshipper" : relationshippercentage}
    print (percentages)
    return percentages
