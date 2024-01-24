import streamlit as st

st.title("การทดสอบสร้างเว็บด้วยPython")
st.image("data.jpeg")
st.header("การนำเสนอข้อมูลกราฟด้วย Python") 
col1, col2, col3, = st.columns(3)

with col1:
    st.header("Versicolor")
    st.image("https://en.wikipedia.org/wiki/Iris_versicolor#/media/File:Blue_Flag,_Ottawa.jpg")

with col2:
    st.header("Verginica")
    st.image("https://en.wikipedia.org/wiki/Iris_virginica#/media/File:Iris_virginica_2.jpg") 

with col3:
    st.header("Setosa")
    st.image("https://en.wikipedia.org/wiki/Iris_setosa#/media/File:Irissetosa1.jpg")

