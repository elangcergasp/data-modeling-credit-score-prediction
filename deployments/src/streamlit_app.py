import streamlit as st
import page_dataset
import page_eda
import page_prediction
import dill as pickle
import json
from ast import literal_eval

global pd_col_list_to_encoded_pre
global pd_col_list_to_encoded
global pd_col_list_to_encoded_type_of_loan

#load model
with open('./src/models_best.pkl', 'rb') as file_1:
    model = pickle.load(file_1)

page = st.sidebar.radio('Pilih Halaman', ('Dataset', 'EDA', 'Prediction'))

st.title('Dashboard Credit Score')

if page == 'Dataset':
    page_dataset.run()
if page == 'EDA':
    page_eda.run()
if page == 'Prediction':
    page_prediction.run()

st.write('---')
st.code('By Elang Cergas Pembrani - 2025')
