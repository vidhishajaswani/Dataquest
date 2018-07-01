## 3. Psycopg2 ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
print(cur)
conn.close()

## 4. Creating a table ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
q="CREATE TABLE notes ( id integer PRIMARY KEY, body text, title text)"
cur.execute(q)
conn.close()

## 5. SQL Transactions ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
q="CREATE TABLE notes ( id integer PRIMARY KEY, body text, title text)"
cur.execute(q)
conn.commit()
conn.close()

## 6. Autocommitting ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit=True
q="CREATE TABLE facts ( id integer PRIMARY KEY, country text, value text)"
cur.execute(q)
conn.close()

## 7. Executing queries ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
q="INSERT INTO notes VALUES(1,'Do more missions on Dataquest.','Dataquest reminder')"
cur.execute(q)
conn.commit()
cur.execute("SELECT * FROM notes;")
rows = cur.fetchall()
print(rows)
conn.close()

## 8. Creating a database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit=True
q="CREATE DATABASE income owner dq"
cur.execute(q)
conn.close()

## 9. Deleting a database ##

import psycopg2
conn = psycopg2.connect("dbname=dq user=dq")
cur = conn.cursor()
conn.autocommit=True
q="DROP DATABASE income;"
cur.execute(q)
conn.close()