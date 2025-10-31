import streamlit as st
from PIL import Image


col1, col2 = st.columns((4,5))

with col1:
    st.title("My Resume")
    st.header("Justus Selwyn")

with col2:
    image = Image.open('Professor_(Money_Heist).jpg')
    st.image(image, width=200)

st.divider()
st.markdown("**About Me**")
st.text("I am a professor.")
st.divider()

st.markdown("")

st.markdown("**Education**")
st.markdown("**Work Experience**")
st.header("**Projects**")
st.header("**Hobbies**")

st.markdown("**Contact me:**")
st.text_input("Your Name: ")
st.text_input("Your Email: ")
st.text_input("Your Message for me: ")
st.button("Send Message")