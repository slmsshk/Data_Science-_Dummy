#Background Image
import base64
import streamlit as st

def add_bg_from_local(image_file):
    with open(image_file,"rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-Image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>""",
    unsafe_allow_html=True
    )

def write(
    value,tag='p',color=None,fontsize=10,fontweight=None,
    textalign=None,padding=None,bg=None ,margin=None):

    """
    Parameters
    value=Value to be printed
    tag=HTML tag you want to use
    color: Color to be used default red
    fontsize: font size to use default 10px
    fontweight: (def-normal)(accepted(normal,bold,italic))
    textalign: alignment accepted values(center,left,right)
    padding(str): add padding in px
    bg(background color): Add background color
    """
    
    st.markdown(f"""<{tag} style='color:{color};font-size:{str(fontsize)+'px'};font-weight:{fontweight};text-align:{textalign};padding:{padding};background-color:{bg};margin:{margin};'>
    {value}    </{tag}>""",unsafe_allow_html=True)





