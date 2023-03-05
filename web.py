import streamlit as st
import pandas as pd
import plotly.express as px

st.title('Temperature Plot')

df=pd.read_csv('data.txt')

plot=px.line(x=df['date'],y=df['temperature'],labels={'x':'Date','y':'Temperature (C)'})
st.plotly_chart(plot)