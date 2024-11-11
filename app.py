import pickle
import streamlit as st
import numpy as np

st.header("Books Recommender System")

modals = pickle.load(open('artifacts/modal.pkl', 'rb'))
books_name = pickle.load(open('artifacts/books_name.pkl', 'rb'))
final_rating = pickle.load(open('artifacts/final_rating.pkl', 'rb'))
book_pivot = pickle.load(open('artifacts/book_pivot.pkl', 'rb'))

def fatch_poster(suggestion):
    ids_index = []
    poster_url = []

    for book_id in suggestion[0]:
        book_name = book_pivot.index[book_id]
        ids = np.where(final_rating['title'] == book_name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['img_url']
        poster_url.append(url)

    return poster_url

def recomendad_books(book_name):
    book_list = []
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = modals.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=6)

    poster_url = fatch_poster(suggestion)

    for i in range(1, len(suggestion[0])): 
        books = book_pivot.index[suggestion[0][i]]
        book_list.append(books)

    return book_list, poster_url

selected_books = st.selectbox("Type or Select a book", books_name)

if st.button('Recommend'):
    recommended_books, poster_url = recomendad_books(selected_books)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended_books[0])
        st.image(poster_url[0])

    with col2:
        st.text(recommended_books[1])
        st.image(poster_url[1])

    with col3:
        st.text(recommended_books[2])
        st.image(poster_url[2])

    with col4:
        st.text(recommended_books[3])
        st.image(poster_url[3])

    with col5:
        st.text(recommended_books[4])
        st.image(poster_url[4])
