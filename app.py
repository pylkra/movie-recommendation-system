#flask use karsakte hain par streamlit use kar rahe hain
import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/ {}?api_key=474336d8e7075e9a7269b5e75c225920&language=en-US'.format(movie_id))
    data = response.json()
    #full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    #return full_path
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']


def recommend(movie,movies_list_df ):
    move_index = movies_list_df[movies_list_df['title']==movie].index[0]
    #search in the similarity matrix where the movie is
    distance = similarity[move_index]
    movies_list_df = sorted(list(enumerate(distance)),reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]

    for i in movies_list_df:
        movie_id = movies_list.iloc[i[0]].movie_id
        recommended_movies.append(movies_list.iloc[i[0]].title)
        #fetch poster from api
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies, recommended_movies_poster

similarity = pickle.load(open('similarity.pkl','rb'))
movies_dict = pickle.load(open('movies_list_dict.pkl','rb'))
movies_list = pd.DataFrame(movies_dict)
st.title('Movie Recommendation System')
selected_option = st.selectbox(
    "How would you like to be contacted?",
    movies_list['title'].values)

if st.button("Recommend"):
    recommended, posters = recommend(selected_option, movies_list)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommended[0])
        st.image(posters[0])

    with col2:
        st.text(recommended[1])
        st.image(posters[1])

    with col3:
        st.text(recommended[2])
        st.image(posters[2])

    with col4:
        st.text(recommended[3])
        st.image(posters[3])
    with col5:
        st.text(recommended[4])
        st.image(posters[4])


