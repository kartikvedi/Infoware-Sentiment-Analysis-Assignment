import pandas as pd
import streamlit as st
import datetime
import matplotlib.pyplot as plt
st.set_page_config(page_title="Sentiment Analytics App",page_icon="chart_with_upwards_trend",layout="wide",initial_sidebar_state="expanded")

data = pd.read_csv('finance.csv')
df_ibm = pd.read_csv('IBM_Sentiment.csv')
df_aapl = pd.read_csv('AAPL_Sentiment.csv')
df_tsla = pd.read_csv('TSLA_Sentiment.csv')
df_baba = pd.read_csv('BABA_Sentiment.csv')
df_oracle = pd.read_csv('oracle_Sentiment.csv')
df_amazon = pd.read_csv('amazon_Sentiment.csv')
df_ma = pd.read_csv('ma_Sentiment.csv')
df_microsoft = pd.read_csv('microsoft_Sentiment.csv')
df_nike = pd.read_csv('nike_Sentiment.csv')
df_nvda = pd.read_csv('nvda_Sentiment.csv')

df_ibm['Date'] =  pd.to_datetime(df_ibm['Date'])
df_aapl['Date'] =  pd.to_datetime(df_aapl['Date'])
df_tsla['Date'] =  pd.to_datetime(df_tsla['Date'])
df_baba['Date'] =  pd.to_datetime(df_baba['Date'])
df_oracle['Date'] =  pd.to_datetime(df_oracle['Date'])
df_ma['Date'] =  pd.to_datetime(df_ma['Date'])
df_microsoft['Date'] =  pd.to_datetime(df_microsoft['Date'])
df_nike['Date'] =  pd.to_datetime(df_nike['Date'])
df_nvda['Date'] =  pd.to_datetime(df_nvda['Date'])
df_amazon['Date'] =  pd.to_datetime(df_amazon['Date'])

st.subheader('Twitter Tweets Sentiment Analysis on Stock Data')
st.sidebar.subheader('Selection Menu & Instructions')
data = data.set_index('Date')

st.sidebar.info('Select a Ticker for Trend Line Chart to see Market Trend for 14 Days from the Symbol Selection Below.')
sel_symbol = st.sidebar.selectbox('Select a Symbol for Trend Line', ('TSLA','AAPL','IBM','BABA','ORCL','NKE','AMZN','MSFT','NVDA','MA'))
st.sidebar.info('Select a Date for Tweet Sentiment for a given Date in the graphs Right hand side.')
sel_date = st.sidebar.date_input('Select a Date for Sentiment Count',datetime.date(2022, 6, 21))
data = data[[sel_symbol]]
st.write('Trend for Stock of', str(sel_symbol))
st.line_chart(data, use_container_width=True)

if sel_symbol == 'IBM':
    graph_data = (df_ibm['Date'] == str(sel_date))
    graph_data = df_ibm.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'AAPL':
    graph_data = (df_aapl['Date'] == str(sel_date))
    graph_data = df_aapl.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'TSLA':
    graph_data = (df_tsla['Date'] == str(sel_date))
    graph_data = df_tsla.loc[graph_data]
    bar_value = graph_data['Sentiment'].value_counts()

    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)

elif sel_symbol == 'BABA':
    graph_data = (df_baba['Date'] == str(sel_date))
    graph_data = df_baba.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'ORCL':
    graph_data = (df_oracle['Date'] == str(sel_date))
    graph_data = df_oracle.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'NKE':
    graph_data = (df_nike['Date'] == str(sel_date))
    graph_data = df_nike.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'AMZN':
    graph_data = (df_amazon['Date'] == str(sel_date))
    graph_data = df_amazon.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'MSFT':
    graph_data = (df_microsoft['Date'] == str(sel_date))
    graph_data = df_microsoft.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'NVDA':
    graph_data = (df_nvda['Date'] == str(sel_date))
    graph_data = df_nvda.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
elif sel_symbol == 'MA':
    graph_data = (df_ma['Date'] == str(sel_date))
    graph_data = df_ma.loc[graph_data]

    bar_value = graph_data['Sentiment'].value_counts()
    tot_count = len(graph_data['Sentiment'])
    y = bar_value.values
    mylabels = bar_value.index
    plt.pie(y, labels = mylabels, autopct='%1.1f%%', startangle=90)
    plt.savefig('pie_graph.png')
    col = st.columns(2)
    with col[0]:
        st.write('Percentage Distribution')
        st.image('pie_graph.png')
    with col[1]:
        st.write('Count Distribution for',str(tot_count), 'Samples')
        st.bar_chart(bar_value, height=380)
