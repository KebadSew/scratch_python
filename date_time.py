# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 21:07:27 2020

@author: legen
"""

import clear_console as cs
import datetime as dt
import time as tm
import pytz 

cs.cls()

print(dt.datetime.now())
print(dt.datetime.now().time())
print(dt.datetime.now().date())
print(dt.datetime.now().day)
print(dt.datetime.now().minute)
print(dt.datetime.now().month)
print(dt.datetime.now().hour)
print(' ----- ')
print(dt.datetime.now().isoweekday())
print(dt.datetime.now().ctime())


d = dt.datetime.now().ctime()
print(type(d))

x = d.split(' ')
print(x)
print(x[0])
print(x[1])
print(x[2])
print(x[4])

cs.cls()

d = dt.datetime.now()
print(d)
print(d.strftime('%m/%d/%Y %H:%M'))
a = d.strftime('%m/%d/%y %H:%M')
print(a)
dtx = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(dtx)
dtx = dt.datetime.now().strftime('%Y%m%d %H:%M:%S')
print(dtx)
print(' --- ')
t = tm.time()
#lt = tm.localtime()
utc_now = dt.datetime.utcnow()
print(t)
#print(lt)
print(utc_now)
utc_now = dt.datetime.now(dt.timezone.utc)
print(utc_now)
print(' --- ')

p = pytz.utc.localize(dt.datetime.utcnow())
print(p)

EST = pytz.timezone('US/Eastern')
NY = pytz.timezone('America/New_York') 
IST = pytz.timezone('Asia/Kolkata') 
UTC = pytz.utc

print(dt.datetime.now(EST))
print(dt.datetime.now(NY))
print(dt.datetime.now(IST))
print(dt.datetime.now(UTC))
