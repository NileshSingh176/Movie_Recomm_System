import streamlit as st
import pickle
import numpy as np
import requests


# movies_list = pickle.load(open("Movies.pkl","rb"))
movies_dict = pickle.load(open("Movies.pkl","rb"))
movies_list = movies_dict["title"].values
similarity = pickle.load(open("similarity.pkl","rb"))


sorted_result = sorted(enumerate(similarity[0]), reverse=True, key=lambda x: x[1])[1:6]
formatted_result = [(index, round(float(value), 3)) for index, value in sorted_result]

def recommend(movie):
    #   movie_index = [movies_list["title"] == movie].index[0]
    movie_index = np.where(movies_list == movie)[0]
    if len(movie_index) == 0:
        st.write("Movie not found in dataset.")
        st.stop()  # Stops further execution
    movie_index = movie_index[0]
    distance = similarity[movie_index]
    sorted_result = sorted(enumerate(similarity[movie_index]), reverse=True, key=lambda x: x[1])[1:6]
    # movie_list = formatted_result

    for i in movies_list:
        movie_id = i[0]

    recommended_movies = [movies_list[i[0]] for i in sorted_result]
    return recommended_movies

    # recommended_movies = []
    # for i in movie_list:
    #     recommended_movies.append(movies_list.iloc[i[0]].title)



st.title("Movie Recommendation System")
select_movie_name = st.selectbox("Select a movie",(movies_list))

if st.button("Recommend"):
    recommendation = recommend(select_movie_name)
    for movie in recommendation:
        st.write(movie)

