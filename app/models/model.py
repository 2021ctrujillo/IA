from datetime import datetime, date

def makedatetime(date, time):

  split_date = date.split("-")
  year = int(split_date[0])
  month = int(split_date[1])
  day = int(split_date[2])

  split_time = time.split(":")
  hour = int(split_time[0])
  minute = int(split_time[1])

  return datetime.datetime(year = year, month = month, day = day, minute = minute, hour = hour)

def duration(event_startdate, event_enddate, event_starttime, event_endtime):
    start = makedatetime(event_startdate, event_starttime)
    end = makedatetime(event_enddate, event_endtime)
    duration = end - start
    return duration
