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

st.subheader("Summary statistics")
total_books = books_df.shape[0]
unique_title = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1 = st.metric("Total Books", total_books)
col2 = st.metric("Book Titile", unique_title)
col3 = st.metric("User Rating", f"{average_rating:.2f}")
col4 = st.metric("Price", f"${average_price:.2f}")

st.subheader("Statistics")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("top 10 books title")
    top_title = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_title)

with col2:
    st.subheader("top 10 authors")
    top_author = books_df['Author'].value_counts().head(10)
    st.bar_chart(top_author)

st.subheader("Genre distribution")
fig = px.pie(books_df, names="Genre", title="Most liked genre 2009-20022", color="Genre",
color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Top 15 authors")
top_authors = books_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author', 'Count']

figg = px.bar(top_authors, x="Count", y="Author", orientation="h",
              title="top 15 authors",
              labels = {"Count": "Counts of books published", "Author": "Author"},
              color="Count", color_continuous_scale=px.colors.sequential.Plasma)

st.plotly_chart(figg)