import streamlit as st
from PIL import Image

original_title = '<p style="text-align: center; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 45px;font-weight: 500"> ' \
                 'CLASSIFICATION ALGORITHMS</p> '
st.markdown(original_title, unsafe_allow_html=True)
original_title = '<p style="text-align: center; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 45px;font-weight: 500"> ' \
                 'AND</p> '
st.markdown(original_title, unsafe_allow_html=True)

original_title = '<p style="text-align: center; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 45px; font-weight: 500"> ' \
                 '💻 CYBERSECURITY 💻</p> '
st.markdown(original_title, unsafe_allow_html=True)

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

# background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/eye.webp")
background = Image.open("./imagenes/eye.webp")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=True)

#with st.sidebar:
    #p = pathlib.Path("./imagenes/ironhack.png")
    #img = Image.open(p)
    #st.image(img, width=100)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(https://startupxplore.com/uploads/ff8080815d6764c2015d736de6ab0087-large.png);
                background-size: 150px;
                background-repeat: no-repeat;
                padding-top: 100px;
                background-position: 10px 10px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "Index";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
add_logo()
