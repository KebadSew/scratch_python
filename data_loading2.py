# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 20:19:31 2020

@author: legen
"""

from clear_console import cls
import pandas as pd
import json
import requests as req
import sqlite3 as sql
import sqlalchemy as sqla


cls()

path = 'files/large_file.csv'

df = pd.read_csv(path)
print(df)

df = pd.read_csv(path,nrows=10)
print(df)

cls()

# Chunking
# =============================================================================
# df_chunk = pd.read_csv(path,chunksize=50)
# pd_aggregate = pd.Series([])
# 
# i = 0;
# for data in df_chunk:
#     if(i%2!=0):
#         print(data)
#     i+=1
# print('the total chunks is ', i)
# =============================================================================

cls()

#JSON

obj = """
{"name": "Wes",
 "places_lived": ["United States", "Spain", "Germany"],
 "pet": null,
 "siblings": 
     [{"name": "Scott", "age": 30,"pets": ["Zeus", "Zuko"]},
      {"name": "Katie", "age": 38,"pets": ["Sixes", "Stache", "Cisco"]},
      {"name": "Alex", "age": 25,"pets": ["buchi"]}]
}
"""
result = json.loads(obj) # convertes json to python object
print(result)
print(' ---- ')
print(result['name'])
print(result['places_lived'])
print(result['siblings'])
print(' --- ')

df_siblings = pd.DataFrame(result['siblings'],columns=['name','age','pets'])
print(df_siblings)

print(' ------- ')
path = 'files/example.json'
df_from_json = pd.read_json(path)
print(df_from_json)

print(' ---- ')
# =============================================================================
# as_json = json.dumps(result) # convertes python to json object
# print(as_json)
# =============================================================================

cls()

# Interacting with Web APIs

file_path = 'files/API-1.txt'

url = 'http://dummy.restapiexample.com/api/v1/employees'
response = req.get(url)
data = response.json()
# =============================================================================
# 
# f = open(file_path,"w")
# f.write(json.dumps(data))
# f.close()
# =============================================================================
print(data['status'])
print('----')
df = pd.DataFrame(data['data'],columns=['id','employee_name','employee_salary','employee_age'])
print(df)

cls()

# Interacting with Databases (sqllite3)

query="""
DROP TABLE test
"""
con = sql.connect('mydata.sqlite')
status = con.execute(query)
con.commit()

print(status)

query = """
CREATE TABLE test(a VARCHAR(20), b VARCHAR(20),c REAL, d INTEGER);
"""

status = con.execute(query)
con.commit()

print(status)

data = [('Atlanta', 'Georgia', 1.25, 6),
         ('Tallahassee', 'Florida', 2.6, 3),
         ('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO test VALUES(?,?,?,?)"
con.executemany(stmt, data)
con.commit()

query = "SELECT * FROM test"
cursor = con.execute(query)
rows = cursor.fetchall()
print(rows)

#print(cursor.description)

#df = pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
df = pd.DataFrame(rows, columns=['a','b','c','d'])
print(df)

print('Using SQL Alchemy ... ')

# USING SQLALCHEMY

db = sqla.create_engine('sqlite:///mydata.sqlite')
response = pd.read_sql(query,db)
print(response)



























