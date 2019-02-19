# -*- coding: utf-8 -*-

'''获取当前日期前后N天或N月的日期'''

from time import strftime, localtime
from datetime import timedelta, date
import calendar

year = strftime("%Y",localtime())
mon  = strftime("%m",localtime())
day  = strftime("%d",localtime())
hour = strftime("%H",localtime())
min  = strftime("%M",localtime())
sec  = strftime("%S",localtime())

def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''''
    return date.today()

def todaystr():
    '''
    get date string, date format="YYYYMMDD"
    '''
    return year+mon+day

def datetime():
    '''''
    get datetime,format="YYYY-MM-DD HH:MM:SS"
    '''
    return strftime("%Y-%m-%d %H:%M:%S",localtime())

def datetimestr():
    '''''
    get datetime string
    date format="YYYYMMDDHHMMSS"
    '''
    return year+mon+day+hour+min+sec

def get_day_of_day(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        return date.today()-timedelta(days=n)
    else:
        return date.today()+timedelta(days=n)

def get_days_of_month(year,mon):
    '''''
    get days of month
    '''
    return calendar.monthrange(year, mon)[1]

def get_firstday_of_month(year,mon):
    '''''
    get the first day of month
    date format = "YYYY-MM-DD"
    '''
    days="01"
    if(int(mon)<10):
        mon = "0"+str(int(mon))
    arr = (year,mon,days)
    return "-".join("%s" %i for i in arr)




if __name__=="__main__":
    print(today())
    print(todaystr())
    print(datetime())
    print(datetimestr())
    print(get_day_of_day(7))
    print(get_day_of_day(-7))

