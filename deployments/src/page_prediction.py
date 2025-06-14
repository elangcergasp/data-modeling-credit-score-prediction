import dill as pickle
from ast import literal_eval
import json
import pandas as pd
import numpy as np
import streamlit as st

global pd_col_list_to_encoded_pre
global pd_col_list_to_encoded
global pd_col_list_to_encoded_type_of_loan

def run():
    global pd_col_list_to_encoded_pre
    global pd_col_list_to_encoded
    global pd_col_list_to_encoded_type_of_loan
    
    #load model
    with open('./src/models_best.pkl', 'rb') as file_1:
        model = pickle.load(file_1)

    with open('./src/cols_form_config.json', 'r') as file_5:
        cols_form_config = json.load(file_5)

    st.subheader('Credit Score - Prediction')

    # FORM
    inputs = {}
    with st.form(key='ftds-p1w4d2am-fifa-2021'):
        for col in cols_form_config:
            config = cols_form_config[col]
            title = col.replace('_', ' ').title()
            if config['type'] == 'text':
                inputs[col] = st.text_input(title, help=col)
            elif config['type'] == 'int':
                tmp_min = None
                if 'min' in config:
                    tmp_min = int(config['min'])
                inputs[col] = st.number_input(title, min_value=tmp_min, step=1, value=int(config['value']), help=col)
            elif config['type'] == 'number':
                tmp_min = None
                if 'min' in config:
                    tmp_min = int(config['min'])
                inputs[col] = st.number_input(title, min_value=tmp_min, value=int(config['value']), help=col)
            elif config['type'] == 'select':
                inputs[col] = st.selectbox(title, config['value'], help=col)
            elif config['type'] == 'select_multiple':
                inputs[col] = st.multiselect(title, config['value'], help=col)
    
        st.markdown('---')
        submitted = st.form_submit_button('Predict')
    
    # create new data, gunakan keseluruhan data
    data_inf = pd.DataFrame([inputs])
    # print(data_inf)
    
    y_pred_inf = model.predict(data_inf)
    # print(y_pred_inf)

    st.write('### Credit Score : ', str(int(y_pred_inf)))

if __name__ == '__main__':
    run()
