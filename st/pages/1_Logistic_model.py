# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 19:39:11 2022

@author: Slmss
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import streamlit as st
import sklearn
import joblib

import warnings
warnings.filterwarnings('ignore')
st.set_option('deprecation.showPyplotGlobalUse', False)
st.set_page_config(page_title="Model training", page_icon="📈")

def header(url):
     st.markdown(f'<p style="background-color:#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

header("Claimnants Dataset")

data=pd.read_csv("https://raw.githubusercontent.com/slmsshk/DataSet/main/claimants.csv")


# Columns

def head1(url):
     col1.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

col1,col2=st.columns(2)
head1("head")
col1.write(data.head())

def tail(url):
     col2.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

tail("Tail")
col2.write(data.tail())


def Viz(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)
# ========================================================================
Viz('Visualization')


for i in data.columns:
    if data[i].max()>1:
        plt.figure(figsize=(5,5))
        fig,ax=plt.subplots()
        ax.hist(data[i])
        ax.set_title(i)
        ax.set_xlabel(f'Skewness{round(data[i].skew(),2)}\nkurt: {round(data[i].kurt(),2)}')
        # ax.set_xticks([0,1])
        st.pyplot(fig)

    else:
        
        plt.figure(figsize=(10,10))
        fig,ax=plt.subplots()

        st.write(data[i].value_counts())

        ax.bar(data[i].value_counts().keys(),data[i].value_counts().values,)
        ax.set_title(i)
        # ax.set_xlabel(i)
        ax.set_xticks([0,1])
        st.pyplot(fig)

        plt.figure(figsize=(10,10))
        fig,ax=plt.subplots()
#--------------------------------------------------------------------
# ---------------------------------------------------------------------

def desc(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)
desc('Descriptive Stats')


col3,col4,col5=st.columns(3)

def descr(url):
     col3.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

descr("Descriptive Stats")
col3.write(data.describe())


def info(url):
     col4.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

info('Info')
col4.write('''
    CASENUM   1340 non-null   int64\n
    ATTORNEY  1340 non-null   int64\n
    CLMSEX    1328 non-null   float64\n
    CLMINSUR  1299 non-null   float64\n
    SEATBELT  1292 non-null   float64\n
    CLMAGE    1151 non-null   float64\n
    LOSS      1340 non-null   float64''')


def null(url):
     col5.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

null('Null Values')
col5.write(data.isnull().sum())

# =========================================================================

def pre(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

pre('Preprocessing')
st.code('''def Fill_Missing_Value(df):
    ind=0
    mean = 0
    for i in df.dtypes:
    
    #Converting numbers
        if i == 'float64' or i == 'int64':
            column_name=df.columns[ind]
            print(f'index No: {ind} Column: {column_name} \nType: {i}')
            print("null",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            column_value=df[column_name][0:]
            mean= column_value.mean()
            print(f"mean of column {column_name}: {mean}")
            
            df[column_name] = df[column_name].fillna(mean)
            print(df[column_name])
            print("After processing \nnull",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            for i in range(0,2):
                print("------------")

        #Converting Objects
        if i == 'object'or i=='o':
            column_name=df.columns[ind]
            print(f'index No: {ind} Column: {column_name} \nType: {i}')
            print("null",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            column_value=df[column_name][0:]
            mode= column_value.mode().values[0]
            print(f"mode of column {column_name}: {mode}")
            
            df[column_name] = df[column_name].fillna(mode,inplace=False)
            print(df[column_name])
            print("After processing \nnull",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            for i in range(0,2):
                print("------------")
        
        ind+=1

    return df

df=Fill_Missing_Value(data)

''')
#Function to preprocess data
def Fill_Missing_Value(df):
    ind=0
    mean = 0
    for i in df.dtypes:
    
    #Converting numbers
        if i == 'float64' or i == 'int64':
            column_name=df.columns[ind]
            print(f'index No: {ind} Column: {column_name} \nType: {i}')
            print("null",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            column_value=df[column_name][0:]
            mean= column_value.mean()
            print(f"mean of column {column_name}: {mean}")
            
            df[column_name] = df[column_name].fillna(mean)
            print(df[column_name])
            print("After processing \nnull",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            for i in range(0,2):
                print("------------")

        #Converting Objects
        if i == 'object'or i=='o':
            column_name=df.columns[ind]
            print(f'index No: {ind} Column: {column_name} \nType: {i}')
            print("null",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            column_value=df[column_name][0:]
            mode= column_value.mode().values[0]
            print(f"mode of column {column_name}: {mode}")
            
            df[column_name] = df[column_name].fillna(mode,inplace=False)
            print(df[column_name])
            print("After processing \nnull",(df[column_name].isnull().sum()/len(df[column_name].index))*100,'Null sum',df[column_name].isnull().sum())
            
            for i in range(0,2):
                print("------------")
        
        ind+=1

    return df

df=Fill_Missing_Value(data)

col6,col7=st.columns(2)

def head2(url):
     col6.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

head2('Head')
col6.write(data.head())

def null2(url):
     col7.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

null2('Null')
col7.write(data.isnull().sum())


def model(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

model('Model training')

st.code('''
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Seperating input and output

X,Y=df.iloc[:,2:],df['ATTORNEY']

x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size=.80)

model=LogisticRegression()

model.fit(x_train,y_train)

predicts=model.predict(x_test)

st.write(f'Accuracy: {round(accuracy_score(y_test,predicts),2)}')''')

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# Seperating input and output

X,Y=df.iloc[:,2:],df['ATTORNEY']

x_train,x_test,y_train,y_test=train_test_split(X,Y,train_size=.80)

model=LogisticRegression()

model.fit(x_train,y_train)

predicts=model.predict(x_test)

st.write(f'Accuracy: {round(accuracy_score(y_test,predicts),2)}')

joblib.dump(model,'Logistic_trained.h5')

# ==========================================================


def eval(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

eval('Evaluating model')

from sklearn.metrics import ConfusionMatrixDisplay,roc_curve,auc,RocCurveDisplay,confusion_matrix

col8,col9=st.columns(2)


def c8(url):
     col8.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

tpr,fpr,trsh=roc_curve(y_test,model.predict_proba(x_test)[:,1])
roc_auc = auc(fpr, tpr)
display = RocCurveDisplay(fpr=fpr, tpr=tpr, roc_auc=roc_auc,
                                  estimator_name='estimator')
display.plot()

c8("ROC & AUC")
col8.pyplot()



def c9(url):
     col9.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

cnf_matrix=confusion_matrix(y_test,predicts)
x=ConfusionMatrixDisplay(cnf_matrix,display_labels=model.classes_)
x.plot()
c9('Confusion Matrix')
col9.pyplot(plt.show())

from statsmodels.api import Logit

x=model_logit=Logit(Y,X).fit().summary()
print(x)
st.subheader("Summary")
st.write(x)




# ==================================================================
def ty(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)


ty('T♥h♥a♥n♥k♥ ♥Y♥o♥u')




