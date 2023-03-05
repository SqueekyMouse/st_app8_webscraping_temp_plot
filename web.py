import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

st.title('Temperature Plot')

# df=pd.read_csv('data.txt')

dbconn=sqlite3.connect('data.sqlite')
cursor=dbconn.cursor()
cursor.execute("SELECT * FROM temp")
rows=cursor.fetchall()
temp=[row[1] for row in rows]
date=[row[0] for row in rows]

plot=px.line(x=date,y=temp,labels={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(plot)