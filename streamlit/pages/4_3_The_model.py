import streamlit as st
import pandas as pd
import pickle
import random
from PIL import Image

st.markdown("# Time to try the model!!!")
# original_title = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 40px"> ' \
                 # 'Time to try the model!!!</p> '
# st.markdown(original_title, unsafe_allow_html=True)
original_title_2 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 20px"> ' \
                 'A Decission Tree Classifier was chosen among 7 classification algorithms becase it had the best balance between performance an trining time.</p> '
st.markdown(original_title_2, unsafe_allow_html=True)
original_title_3 = '<p style="text-align: left; font-family:Vengeance Bold, sans-serif; color:#ddebf0; font-size: 20px"> ' \
                 'Just press the button and wait for the magic to happen 🦄</p> '
st.markdown(original_title_3, unsafe_allow_html=True)

st.markdown(" ")
st.markdown(" ")

df = pd.read_csv(r"https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/data/df_attacks_enc.csv")
# df = pd.read_csv(r"/home/miguel/PycharmProjects/attackclassifier_streamlit/data/df_attacks_enc.csv")
df.drop(columns=['Unnamed: 0'], inplace=True)

df2 = df.drop(columns=['Attack Type'], inplace=False)

decission_tree = pickle.load(open('https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/data/2_dt.pkl', 'rb'))
# decission_tree = pickle.load(open('/home/miguel/PycharmProjects/attackclassifier_streamlit/data/2_dt.pkl', 'rb'))

if st.button('Launch attack'):
    row = random.randint(0, 494021)
    x = df2.iloc[[row]]

    prediction = decission_tree.predict(x)

    y = prediction[0]
    # st.write(prediction[0])
    # st.write(df.iloc[row]['Attack Type'])
    if y == "normal" and y == df.iloc[row]['Attack Type']:
        st.markdown(f"## Calm down, that was a {y} connection")
        background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/Chuckfinal.png")
        # background = Image.open("./imagenes/Chuckfinal.png")
        col1, col2, col3 = st.columns([0.2, 5, 0.2])
        col2.image(background, use_column_width=True)
    elif y == df.iloc[row]['Attack Type']:
        if y == "dos":
            st.markdown(f"## Great!!! You stopped a {y} attack")
            background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/ddos.jpg")
            # background = Image.open("./imagenes/ddos.jpg")
            col1, col2, col3 = st.columns([0.2, 5, 0.2])
            col2.image(background, use_column_width=True)
        # st.write(row)
        elif y == "u2r":
            st.markdown(f"## Great!!! You stopped a {y} attack")
            background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/Om.jpeg")
            # background = Image.open("./imagenes/Om.jpeg")
            col1, col2, col3 = st.columns([0.2, 5, 0.2])
            col2.image(background, use_column_width=True)
        elif y == "probe":
            st.markdown(f"## Great!!! You stopped a {y} attack")
            background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/probe.jpg")
            # background = Image.open("./imagenes/probe.jpeg")
            col1, col2, col3 = st.columns([0.2, 5, 0.2])
            col2.image(background, use_column_width=True)
        elif y == "r2l":
            st.markdown(f"## Great!!! You stopped a {y} attack")
            background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/r2l.jpg")
            # background = Image.open("./imagenes/r2l.jpeg")
            col1, col2, col3 = st.columns([0.2, 5, 0.2])
            col2.image(background, use_column_width=True)

    else:
        st.markdown(f"## Sorry darling, you've mistaken a {y} for a {df.iloc[row]['Attack Type']}")
        background = Image.open("https://github.com/Origamologo/Intrusion-Detection-System/blob/main/streamlit/imagenes/catwoman.jpg")
        # background = Image.open("./imagenes/catwoman.jpg")
        col1, col2, col3 = st.columns([0.2, 5, 0.2])
        col2.image(background, use_column_width=True)


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
