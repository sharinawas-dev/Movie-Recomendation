import streamlit as st
import pickle
import request

st.title("Movie Recomended System")
st.text("The dtabse for these movie recomnded is taken from TMBD website")
movie=pickle.load(open('movie.pkl','rb'))
similarity=pickle.load(open('similarity.pkl','rb'))

movie_list=movie['title'].values
selected_movie=st.selectbox("Type",movie_list,index=None)

def recommend(movie):
    index=movies[movies['title']==movies].index[0]
    distances = sorted(list(enumerate(similarity[index])),key=lambda x:x[1],reverse=True)[1:6]
    recommneded_movie_names=[]
    for i in distances:
        movie_id=movies.iloc[i[0]].movie_id
        recommneded_movie_names.append(movies.iloc[i[0]].title)
    return recommneded_movie_names


if st.button("Show Recomendation")
    st.write("Herea are the similirality movies to watch")
    recommneded_movie_names=recommend(movie)
    for i in recommneded_movie_names:
        st.subheader(i)

