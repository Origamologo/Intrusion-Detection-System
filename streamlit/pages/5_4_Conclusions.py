import streamlit as st
from PIL import Image

# original_title = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 40px"> ' \
                 # 'Let\'s drag some conclusions</p>'
# st.markdown(original_title, unsafe_allow_html=True)

st.markdown("# Let's drag some conclusions")

st.markdown(" ")
st.markdown(" ")


original_title = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 30px"> ' \
                 '• A data analyst mindset can be very very useful when facing cybersecurity problematics</p> '
st.markdown(original_title, unsafe_allow_html=True)

original_title_0 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 30px"> ' \
                 '• It\'s usually easier and cheaper to harm than to protect</p> '
st.markdown(original_title_0, unsafe_allow_html=True)

original_title_1 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 30px"> ' \
                 '• You don\'t need to be a data analyst or even to know how to code to goof around but...</p> '
st.markdown(original_title_1, unsafe_allow_html=True)

original_title_2 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 30px"> ' \
                 '• ...don\'t be a jerk and pursuit knowledge, it\'s way more satisfaying</p> '
st.markdown(original_title_2, unsafe_allow_html=True)

original_title_3 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 30px"> ' \
                 '• Love pandas, hate bulling</p> '
st.markdown(original_title_3, unsafe_allow_html=True)

background = Image.open("./imagenes/panda.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, use_column_width=False, width=300)

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