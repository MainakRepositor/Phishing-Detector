import streamlit as st
import pickle
import pandas as pd
from extract_features import ExtractFeatures
from PIL import Image


import streamlit as st

st.markdown(
    "<div style='display: flex; align-items: center; margin-bottom: -35px;'>"
    "<h1 style='color:#003E7F; margin-right: 10px;'> Unmasking Phishing Websites:</h1>"
    "</div>"
    "<h1 style='color:orange; margin-left: 10px;'>A Machine Learning Approach</h1>"
    "</div>",
    unsafe_allow_html=True
)

image=Image.open('cybersecpic.jpeg')
width=750
height=500
image_new=image.resize((width,height))
st.image(image_new)



