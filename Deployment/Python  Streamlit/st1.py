# -*- coding: utf-8 -*-
"""
Created on Thu Aug  4 10:46:11 2022

@author: Slmss
"""

import streamlit as st
import pandas as pd
# import matplotlib.pyplot as plt

st.write('Hello world')

data=pd.read_csv('claimants.csv')
st.write(data)