import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Name' : ['Charlie', 'John', 'Bob'],
    'Age' : [21,23,31],
    'City' : ['Tirana', 'Prishtina','Tetova']
})

st.write(df)

books_df = pd.read_csv("file.csv")

st.title("Best selling boooks")
st.write("The best selling books from 2009 to 2022")

st.subheader("The summary statistics")
total_books = books_df.shape[0]
unique_title = books_df['Name'].nunique()
avarage_rating = books_df['User Rating'].mean()
avarage_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1 = st.metric("Total Books", total_books)
col2 = st.metric("Book Titile", unique_title)
col3 = st.metric("User Rating", avarage_rating)
col4 = st.metric("Price", avarage_price)