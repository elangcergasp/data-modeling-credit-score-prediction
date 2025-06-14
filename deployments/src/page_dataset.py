import streamlit as st
import pandas as pd

def run():
    st.subheader('Credit Score - Dataset')
    
    df = pd.read_csv('./src/dataset_credit_score.csv')
    df = df.set_index('id')
    df_limit = df[(df['month'] == 'July') | (df['month'] == 'August')]

    # DATAFRAME
    st.write('### Dataset Full')
    st.write(f'#### Size : {df.shape}')
    st.dataframe(df)

    st.write('---')
    
    # DATAFRAME
    st.write('### Dataset - Limited `July` and `August`')
    st.write(f'#### Size : {df_limit.shape}')
    st.dataframe(df_limit)

if __name__ == '__main__':
    run()
