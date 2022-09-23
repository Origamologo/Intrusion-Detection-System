import streamlit as st
from PIL import Image

st.balloons()

st.markdown("# Thank you for listening!!!")
st.markdown('# 🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧🐧')
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
original_title = '<p style="text-align: center; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 45px;font-weight: 500"> ' \
                 'github.com/Origamologo</p> '
st.markdown(original_title, unsafe_allow_html=True)
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/qr.jpg")
# background = Image.open("./imagenes/qr.jpg")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=False, width=600)
# image = Image.open("./imagenes/qr.jpg")
# st.image(image)
