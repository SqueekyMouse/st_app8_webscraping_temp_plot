import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

st.title('Temperature Plot')

dbconn=sqlite3.connect('data.sqlite')
cursor=dbconn.cursor()

cursor.execute("SELECT * FROM temp")
rows=cursor.fetchall()
temp=[row[1] for row in rows]
date=[row[0] for row in rows]

# Same as above
# cursor.execute("SELECT date FROM temp")
# date=cursor.fetchall()
# date=[i[0] for i in date]
# cursor.execute("SELECT date FROM temp")
# temp=cursor.fetchall()
# temp=[i[1] for i in temp]

plot=px.line(x=date,y=temp,labels={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(plot)