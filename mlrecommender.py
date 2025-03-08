import streamlit as st
import pickle
import pandas as pd
#import requests
#def fetch_poster(movie_id):
 #   requests.get()
def recommend(movie):
    movie_index=movies[movies["title_x"]==selectedmovie].index[0]
    distances=similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    recommended=[]
    for i in movies_list:
        movieid=i[0]
        #Poster Fetch from API
        recommended.append(movies.iloc[i[0]].title_x)
    return recommended
moviesdict=pickle.load(open("moviesdict.pkl","rb"))
similarity=pickle.load(open("similarity.pkl","rb"))
movies=pd.DataFrame(moviesdict)
st.title("Movie Recommender System")
selectedmovie=st.selectbox("Select a movie:",movies["title_x"].values)
if(st.button("Reommend")):
    recommendations=recommend(selectedmovie)
    for i in recommendations:
        st.write(i)