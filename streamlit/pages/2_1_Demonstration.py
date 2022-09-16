import streamlit as st

original_title = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 35px"> ' \
                 'Let\'s see some cool stuff we can do when we know how to analyze, interpret and modify data with python 🐼❤️🐍</p> '
st.markdown(original_title, unsafe_allow_html=True)

st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")
st.markdown(" ")

video_file = open('/home/miguel/PycharmProjects/attackclassifier_streamlit/imagenes/oioi.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)

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