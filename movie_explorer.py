import pandas as pd
import numpy as np
import streamlit as st

st.set_page_config(
    page_title="Movie Explorer App",
    page_icon=":cinema:",
    layout="wide",  # (Default:"centered" or "wide")
    initial_sidebar_state="expanded", # (D:"auto"[ie responsive] or "expanded" or "collapsed")
    menu_items={
        'Get Help': 'https://www.example.com/help',
        'Report a bug': "https://www.example.com/bug",
        'About': "## This is a demo app for *ATHEX*!"
    }      
    
)

@st.cache
def load_movies():    
    movies = pd.read_csv('https://raw.githubusercontent.com/nchris/pythoncourse/master/imdb_top_1000.csv', index_col=0)
    movies.index.name = None # clearing the index name (optional)
    movies['decade'] = (movies['startYear']  // 10) * 10
    movies['runtimeMinutes'] = movies['runtimeMinutes'].astype(int)
    movies['link'] = "<a target='_blank' href='https://www.imdb.com/title/"+movies.index+"'>IMDB</a>"
    return movies
    
movies = load_movies()    
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2790/2790961.png", width=80)
st.header("Movie Explorer")

def durations(x):
    if x == 120:
        return "Less than two hours"
    else:
        return "Any"
st.sidebar.subheader("Duration")    
duration = st.sidebar.radio(
    "Select movie duration",
    (120, 500),
    format_func=durations,
    index=1)

st.sidebar.subheader("Genres")
genres = st.sidebar.multiselect(
    'Select movie genre(s)',
    movies['genres'].str.get_dummies(sep=",").columns,
    ['Action', 'Adventure', 'Comedy', 'Crime', 'Drama', 'Mystery', 'Thriller'])

st.sidebar.subheader("Release Year")
years = st.sidebar.slider(
 'Select a range of release years',
    min_value=int(movies['startYear'].min()),
    max_value=int(movies['startYear'].max()),
     value=(int(movies['startYear'].min()), int(movies['startYear'].max())),
    step=1
     )

st.sidebar.subheader("Rating")

min_rating = st.sidebar.slider(
 'Select the minimum rating',
    min_value=float(movies['averageRating'].min()),
    max_value=float(movies['averageRating'].max()),
    step=0.1)

st.sidebar.subheader("Votes")
min_votes = st.sidebar.slider(
 'Select the minimum number of votes (in thousands)',
    min_value=int(movies['numVotes'].min()//1000),
    max_value=int(movies['numVotes'].max()//1000),
     value=int(movies['numVotes'].min()//1000),
    step=100)

def filtered_results(data=movies, duration=duration, genres=genres, years=years, min_rating=min_rating, min_votes=min_votes):
    mycols = ['primaryTitle', 'startYear', 'director','runtimeMinutes', 'genres', 'averageRating', 'numVotes', 'link']
    mask = (data['runtimeMinutes'] <= duration) & \
(data['genres'].str.contains("|".join(genres))) & \
(data['startYear'] >= years[0]) & \
(data['startYear'] <= years[1]) & \
(data['averageRating'] >= min_rating) & \
(data['numVotes'] >= min_votes*1000)
    return data.loc[mask, mycols].sort_values(['averageRating', 'numVotes'], ascending=False)

result = filtered_results()
st.write("### Filtered Results ("+str(result.shape[0])+")")  

st.write(result.to_html(escape=False, index=False), unsafe_allow_html=True) 
 
