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

st.subheader("Filter fata by genre")
genre_filter = st.selectbox("Select Genre", books_df['Genre'].unique())
filtered_df = books_df[books_df['Genre'] == genre_filter]
st.write(filtered_df)

st.sidebar.header("Add a new book data")
with st.sidebar.form("book_form"):
    new_name = st.text_input("Book Name")
    new_author = st.text_input("Author Name")
    new_user_rating = st.slider("User Rating", 0.0,5.0,0.0,0.1)
    new_reviews = st.number_input("Reviews", min_value=0, step=1)
    new_price = st.number_input("Price", min_value=0, step=1)
    new_year = st.number_input("Year", min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox("Genre", books_df["Genre"].unique())
    submit_button = st.form_submit_button(label="Add Book")

if submit_button:
    new_data = {
        'Name' : new_name,
        'Author' : new_author,
        'User Rating' : new_user_rating,
        'Reviews' : new_reviews,
        'Year' : new_year,
        'Genre' : new_genre
    }
    books_df = pd.concat([pd.DataFrame(new_data,index=[0]),books_df],ignore_index=True)
    books_df.to_csv('file.csv',index=False)
    st.sidebar.success("New book added successfully")

st.sidebar.header("Filter Option")
selected_author = st.sidebar.selectbox("Select Author",["All"] + list(books_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year",["All"] + list(books_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre",["All"] + list(books_df['Genre'].unique()))
min_rating = st.sidebar.slider("Minimum User Rating", 0.0,5.0,0.0,0.1)
max_prize = st.sidebar.slider("Max Price",0,books_df['Price'].max(),books_df['Price'].max())