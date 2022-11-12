# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:01:17 2020

"""

import pandas as pd
import streamlit as st 
from sklearn.linear_model import LogisticRegression
from pickle import dump
from pickle import load

st.title('Model Deployment: Logistic Regression')

   
df = pd.read_csv(r"\Users\Slmss\Desktop\excelr\Deployment\Python  Streamlit\Claimants_Test.csv")
df.drop(["CASENUM"],inplace=True,axis = 1)
df = df.dropna().reset_index()
df.drop(["index"],inplace=True,axis = 1)

#st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('Logistic_Model.sav', 'rb'))

prediction = loaded_model.predict(df)
prediction_proba = loaded_model.predict_proba(df)

#st.subheader('Predicted Result')
#st.write('Yes' if prediction_proba[0][1] > 0.5 else 'No')

st.subheader('Prediction Probability')
st.write(prediction_proba)

output=pd.concat([df,pd.DataFrame(prediction_proba)],axis=1)

output.to_csv('output.csv')


