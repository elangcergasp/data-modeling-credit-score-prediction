import streamlit as st
from ast import literal_eval
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

def run():
    st.subheader('Credit Score - EDA')
    
    df = pd.read_csv('./src/dataset_credit_score.csv')
    df = df.set_index('id')
    df['credit_score'] = df['credit_score'].astype(str)
    df['type_of_loan'] = df['type_of_loan'].apply(literal_eval)
    df = df[(df['month'] == 'July') | (df['month'] == 'August')]
    
    # Pie Chart
    st.write('### Pie Chart')
    pie_cols = ['credit_score', 'credit_mix', 'payment_of_min_amount']
    for col in pie_cols:
        fig = px.pie(
            df[col].value_counts().reset_index(), 
            names=col,
            values='count',
            title=f'Pie Chart of [{col}]', 
            # color_discrete_sequence=px.colors.qualitative.T10,
        )
        st.plotly_chart(fig)
    st.write('---')
    
    # Horizontal Bar
    st.write('### Bar Plot')
    bar_cols = ['occupation', 'payment_behaviour']
    for col in bar_cols:
        fig = px.bar(
            df[col].value_counts().reset_index(), 
            x='count', y=col, 
            title=f'Bar Plot of [{col}]', 
            orientation='h', barmode='stack', height=700, text_auto=True,
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )
        st.plotly_chart(fig)
        fig = px.bar(
            df[[col, 'credit_score']].value_counts().reset_index(), 
            x='count', y=col, color='credit_score',
            title=f'Bar Plot of [{col}] with [credit_score]', 
            orientation='h', barmode='stack', height=700,
            color_discrete_sequence=px.colors.qualitative.Plotly,
        )
        st.plotly_chart(fig)
    fig = px.bar(
        df.explode('type_of_loan')['type_of_loan'].value_counts().reset_index(), 
        x='count', y='type_of_loan', 
        title=f'Bar Plot of [type_of_loan]', 
        orientation='h', barmode='stack', height=700, text_auto=True,
        color_discrete_sequence=px.colors.qualitative.Plotly,
    )
    st.plotly_chart(fig)
    st.write('---')
    
    # Histogram
    st.write('### Histogram of Numeric Cols')
    num_cols = [
        'age', 'annual_income', 'monthly_inhand_salary', 
        'credit_history_age', 'total_emi_per_month', 
        'num_bank_accounts', 'num_credit_card', 'interest_rate', 
        'num_of_loan', 'delay_from_due_date', 'num_of_delayed_payment', 
        'changed_credit_limit', 'num_credit_inquiries', 'outstanding_debt', 
        'credit_utilization_ratio', 'amount_invested_monthly', 'monthly_balance'
    ]
    for col in num_cols:
        fig = px.histogram(df[col], title=f'Histogram of [{col}]')
        st.plotly_chart(fig)
    st.write('---')
    
    # Boxplot
    st.write('### Boxplot of Numeric Cols')
    for col in num_cols:
        fig = px.box(df[col], title=f'Boxplot of [{col}]')
        st.plotly_chart(fig)


if __name__ == '__main__':
    run()
