import streamlit as st
from transformers import pipeline

st.image("https://image.shutterstock.com/image-photo/english-vs-germany-german-smoky-260nw-1401171731.jpg")

st.title('Tłumacz angielsko - niemiecki')
st.subheader('Aplikacja pozwalająca przetłumaczyć tekst z języka angielski na język niemiecki, wykorzystując uczenie maszynowe.')

st.spinner()
inputText = st.text_area(label = "Tekst do tłumaczenia")
submit = st.button("Tłumacz")

if submit:
    if inputText == "":
        st.warning("Wprowadź tekst do przetłumaczenia")
    else:
        with st.spinner(text='Tłumaczę...'):
            translator = pipeline("translation_en_to_de")
            answer = translator(inputText)[0]["translation_text"]
            st.success(answer)

st.text('s20008')