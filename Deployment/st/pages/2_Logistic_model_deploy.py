import streamlit as st
import pandas as pd
import joblib
st.set_page_config(page_title="Deployment", page_icon="📈")

model=joblib.load('Logistic_trained.h5')

# prediction =None



def head(url):
     st.markdown(f'<p style="background-color:#f4c2c2 ;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

head("(人◕‿◕) 𝔼𝕟𝕥𝕖𝕣 𝕧𝕒𝕝𝕦𝕖𝕤 𝕥𝕠 𝕔𝕙𝕖𝕔𝕜 (•◡•)")

CLMSEX=st.selectbox(("Enter CLMSEX"),['Male','Female'])
if CLMSEX=='Male':
    CLMSEX=1
else:
    CLMSEX=0

CLMINSUR=st.number_input('Enter CLMINSUR')

SEATBELT=st.selectbox(("Enter SEATBELT"),['Yes','No'])
if SEATBELT=='Yes':
    SEATBELT=1
else:
    SEATBELT=0

CLMAGE=st.number_input("Enter CLMAGE")

LOSS =st.number_input("Enter Loss")

ui=pd.Series({'CLMSEX':CLMSEX,'CLMINSUR':CLMINSUR,'SEATBELT':SEATBELT,
'CLMAGE':CLMAGE,'LOSS':LOSS})

prediction=model.predict([ui])

def pred(url):
     st.markdown(f'<p style="background-color:	#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

if prediction==1:
    pred('Wont Hire Attorney')
else:
    pred('Will Hire Attorney')