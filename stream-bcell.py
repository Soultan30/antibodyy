import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('input-bcell.sav', 'rb'))

st.title('Prediksi Antibody Terhadap Penyakit COVID-19')

start_position = st.text_input ('Start Position')

end_position = st.text_input ('End Position')

chou_fasman = st.text_input ('Chou Fasman')

emini = st.text_input ('Emini')

kolaskar_tongaonkar = st.text_input ('Kolaskar Tongaonkar')

parker = st.text_input ('Parker')

isoelectric_point = st.text_input ('Isoelectric Point')

aromaticity = st.text_input ('Aromaticity')

hydrophobicity = st.text_input ('Hydrophobicity')

stability = st.text_input ('Stability')

bcell_diagnosis =''

if st.button('Prediksi Antibody Terhadap Penyakit COVID-19'):
    bcell_prediction = model.predict([[start_position, end_position, chou_fasman,  emini, kolaskar_tongaonkar, parker, isoelectric_point, aromaticity, hydrophobicity, stability]])

    if (bcell_prediction[0]==0):
        bcell_diagnosis = 'Lemah'
    else:
        bcell_diagnosis = 'Kuat'
st.success(bcell_diagnosis)
