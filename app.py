import streamlit as st
import pickle
import pandas as pd
import requests

movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl', 'rb'))

def fetch_poster(movie_title, api_key='3196bf33'):
    query = movie_title.replace(" ", "+")
    url = f"http://www.omdbapi.com/?t={query}&apikey={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["Response"] == "True":
            return data.get("Poster", None)
    return None

def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_list:
        movie_id = i[0]
        movie_title = movies.iloc[movie_id].title
        
        poster_url = fetch_poster(movie_title)
        
        recommended_movies.append(movie_title)
        recommended_posters.append(poster_url)

    return recommended_movies, recommended_posters

st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select Movie', movies['title'].values)

if st.button('Recommend'):
    recommendations, posters = recommend(selected_movie_name)
    
    cols = st.columns(len(recommendations))
    
    for idx, col in enumerate(cols):
        with col:
            if posters[idx]:
                st.image(posters[idx])
            else:
                st.write("Poster not available")
            st.write(recommendations[idx])
            
