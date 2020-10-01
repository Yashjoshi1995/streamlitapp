# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:41:13 2020

@author: Yash Joshi
"""

import streamlit as st
import pandas as pd
import numpy as np
import base64


# Function to export the data
def download_link(object_to_download, download_filename, download_link_text):
    """
    Generates a link to download the given object_to_download.

    object_to_download (str, pd.DataFrame):  The object to be downloaded.
    download_filename (str): filename and extension of file. e.g. mydata.csv, some_txt_output.txt
    download_link_text (str): Text to display for download link.

    Examples:
    download_link(YOUR_DF, 'YOUR_DF.csv', 'Click here to download data!')
    download_link(YOUR_STRING, 'YOUR_STRING.txt', 'Click here to download your text!')

    """
    if isinstance(object_to_download,pd.DataFrame):
        object_to_download = object_to_download.to_csv(index=True)

    # some strings <-> bytes conversions necessary here
    b64 = base64.b64encode(object_to_download.encode()).decode()

    return f'<a href="data:file/csv;base64,{b64}" download="{download_filename}">{download_link_text}</a>'




def main():

    data = pd.read_excel("BQ-Assignment-Data-Analytics.xlsx")

    # Extracting only months from the 'Date' column
    data['Month'] = data['Date'].map(lambda x: x.month)
    map_year = {1:'Jan 20', 2: 'Feb 20', 3: 'Mar 20', 4: 'Apr 20', 5: 'May 20'}
    data['Month'] = data['Month'].map(map_year)

    values = ['Select all']
    a = data['Item Type'].unique()
    values.extend(list(a))

    item = list(data['Item'].unique())
    sort_order = list(data['Item Sort Order'].unique())

    d = {}
    for i in range(len(item)):
        d[item[i]] = sort_order[i]


    #side = st.sidebar.selectbox('Item Type', values)

    rad = st.sidebar.radio("Item Type", values, index = 0)

    if rad == 'Fruit':
        data_fruit = data[data['Item Type'] == 'Fruit'][['Item','Sales','Month']]
        fruit = data_fruit.groupby(['Item','Month'])['Sales'].sum().reset_index()
        fruit = fruit.pivot_table(index = 'Item', columns = 'Month', values= 'Sales')
        fruit['Item Sort Order'] = fruit.index.values
        # Creating a copy of Item(which is in index) so as to replace it with Item Sort Order
        fruit['Item Sort Order'] = fruit['Item Sort Order'].map(d)
        # Creating a new dataframe to bring the columns in order as given in the sample
        month_cols = list(fruit.columns)[:-1]
        df_fruit = pd.DataFrame()
        df_fruit['Item'] = fruit.index.values
        df_fruit.set_index('Item', inplace = True)
        df_fruit['Item Sort Order'] = fruit['Item Sort Order'].values

        for i in month_cols:
            df_fruit[i] =  fruit[i].values

        sort = st.selectbox("Sort data by Item Sort order in:",['Ascending order','Descending order'], index = 0)
        if sort == 'Ascending order':
            df_fruit_sort = df_fruit.sort_values(by = 'Item Sort Order')
            st.dataframe(df_fruit_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_fruit_sort, 'fruit_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
    
        elif sort == 'Descending order':
            df_fruit_sort = df_fruit.sort_values(by = 'Item Sort Order', ascending = False)
            st.dataframe(df_fruit_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_fruit_sort, 'fruit_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
        else:
            st.dataframe(df_fruit)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_fruit, 'fruit_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
        
    
    elif rad == 'Vegetable':
        data_veg = data[data['Item Type'] == 'Vegetable'][['Item','Sales','Month']]
        veg = data_veg.groupby(['Item','Month'])['Sales'].sum().reset_index()
        veg = veg.pivot_table(index = 'Item', columns = 'Month', values= 'Sales')
        veg['Item Sort Order'] = veg.index.values
        # Creating a copy of Item(which is in index) so as to replace it with Item Sort Order
        veg['Item Sort Order'] = veg['Item Sort Order'].map(d)
        month_cols = list(veg.columns)[:-1]
        # Again here, creating a new dataframe to bring the columns in order as given in the sample
        df_veg = pd.DataFrame()
        df_veg['Item'] = veg.index.values
        df_veg.set_index('Item', inplace = True)
        df_veg['Item Sort Order'] = veg['Item Sort Order'].values

        for i in month_cols:
            df_veg[i] = veg[i].values
        
        sort = st.selectbox("Sort data by Item Sort order in:",['Ascending order','Descending order'], index = 0)
        if sort == 'Ascending order':
            df_veg_sort = df_veg.sort_values(by = 'Item Sort Order')
            st.dataframe(df_veg_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_veg_sort, 'veg_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
    
        elif sort == 'Descending order':
            df_veg_sort = df_veg.sort_values(by = 'Item Sort Order', ascending = False)
            st.dataframe(df_veg_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_veg_sort, 'veg_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
        else:
            st.dataframe(df_veg)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_veg, 'veg_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
    else:
        all_data = data.groupby(['Item','Month'])['Sales'].sum().reset_index()
        all_data1 = all_data.pivot_table(index = 'Item', columns = 'Month', values= 'Sales')
        all_data1['Item Sort Order'] = all_data1.index.values
        # Creating a copy of Item(which is in index) so as to replace it with Item Sort Order
        all_data1['Item Sort Order'] = all_data1['Item Sort Order'].map(d)
        month_cols = list(all_data1.columns)[:-1]
        # Again here, creating a new dataframe to bring the columns in order as given in the sample
        df_all = pd.DataFrame()
        df_all['Item'] = all_data1.index.values
        df_all.set_index('Item', inplace = True)
        df_all['Item Sort Order'] = all_data1['Item Sort Order'].values

        for i in month_cols:
            df_all[i] = all_data1[i].values
        
        sort = st.selectbox("Sort data by Item Sort order in:",['Ascending order','Descending order'], index = 0)
        if sort == 'Ascending order':
            df_all_sort = df_all.sort_values(by = 'Item Sort Order')
            st.dataframe(df_all_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_all_sort, 'all_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
    
        elif sort == 'Descending order':
            df_all_sort = df_all.sort_values(by = 'Item Sort Order', ascending = False)
            st.dataframe(df_all_sort)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_all_sort, 'all_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
        else:
            st.dataframe(df_all)
            if st.button('Download Dataframe as CSV'):
                tmp_download_link = download_link(df_all, 'all_data.csv', 'Click here to download your data!')
                st.markdown(tmp_download_link, unsafe_allow_html=True)
    
#if st.button('Download Dataframe as CSV'):
    #tmp_download_link = download_link(data, 'YOUR_DF.csv', 'Click here to download your data!')
    #st.markdown(tmp_download_link, unsafe_allow_html=True)

if __name__=='__main__':
    main()







            
