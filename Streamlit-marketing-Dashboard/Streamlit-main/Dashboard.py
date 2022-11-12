# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 23:57:53 2022

@author: DELL
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import requests 
import plotly.express as px


#st.title("Marketing Dashboard")
st.markdown("<h1 style='text-align: left; color: White; font-size:45px; '>Marketing Dashboard</h1>", unsafe_allow_html=True)

#Background image
import base64
def add_bg_from_local(cry):
    with open(cry, "rb") as cry:
        encoded_string = base64.b64encode(cry.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: 1024x768
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('cry.jpg') 


#Separating orderbook and trade columns
df=pd.read_json('data.json')

l0 = df.columns
l1 = []
l2 = []

i=0
for i,x in enumerate (l0) :
    if 'orderbook' in x :
        l1.append(x)
    elif 'trade' in x:
        l2.append(x)
    i += 1

df1 = pd.DataFrame(l1)
df2 = pd.DataFrame(l2) 

# Functions for each of the pages
#All types of charts

#Adding dataframe in a button to show
st.markdown("<h3 style='text-align: left; color: White; font-size:15px; '>Dataset</h1>", unsafe_allow_html=True)
Dataset = st.checkbox('')
   
if Dataset:     
    st.write(df)

    
    

def interactive_plot1(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Line Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.line(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)

def interactive_plot2(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Bar Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.bar(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)

def interactive_plot3(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Area Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.area(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)


def interactive_plot4(l0):
    st.markdown("<h2 style='text-align: center; color: White; font-size:25px; '>Scatter Chart</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df1)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df2)

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot)


#Sidebar navigation
st.sidebar.title('Navigation')
    
option=st.sidebar.radio('Select what you want to display:',['Line Chart','Bar Chart','Area Chart','Scatter Chart'])
#option = st.sidebar.checkbox('Preview Dataset')
#st.dataframe(df)
             

st.sidebar.image('https://cdn.shortpixel.ai/spai/q_lossy+to_webp+ret_img/https://www.onlc.com/blog/wp-content/uploads/2017/10/ONLC-2017-637x350.png')
 
# Navigation options
if option == 'Line Chart':
  interactive_plot1(df)
elif option == 'Bar Chart':
  interactive_plot2(df)
elif option == 'Area Chart':
  interactive_plot3(df)
elif option == 'Scatter Chart':
  interactive_plot4(df)



