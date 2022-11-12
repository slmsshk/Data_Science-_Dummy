import pandas as pd
import streamlit as st
# from sklearn import linear_model

# Reading Dataset
data=pd.read_csv('Cars.csv')


# =============================================================================
# StreamLit APP
# =============================================================================
# c1,c2 =st.columns(2)
# # with st.sidebar:
# #     # with st.echo():
# #     st.write("Make predictions")
        
# st.
# with c1:
with st.expander("Cars Dataset",expanded =True):
    st.write(data)
     

# c1,c2 =st.columns(2)
# with st.sidebar:
# with c2:
tab1, tab2, tab3 = st.tabs(["Describe", "Info", "Corr"])
with tab1:
    st.write(data.describe())
with tab2:
    st.write(data.info())
with tab3:
    st.write(data.corr())

l=[]
for i,j in enumerate(data.columns):
    if data[j].dtypes=='obj':
        l.append(j)

df1=data.drop(l,axis=1)

st.write(df1.head())

st.backGroundColor='red'
    
    
    
# st.header("A cat")
# st.image("https://static.streamlit.io/examples/cat.jpg")

# with tab2:
# st.header("A dog")
# st.image("https://static.streamlit.io/examples/dog.jpg")

# # with tab3:
# st.header("An owl")
# st.image("https://static.streamlit.io/examples/owl.jpg")
