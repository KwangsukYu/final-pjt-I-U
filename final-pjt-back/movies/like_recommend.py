from .models import Movie
from accounts.models import User
import numpy as np
import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame

def find_sim_movie_item(df, title_name, top_n=5):
    # print(df)
    like_rmd_lst = []
    
    try:
        title_movie_sim = df[[title_name]].drop(title_name, axis=0)
        title_movie_sim = title_movie_sim.sort_values(title_name, ascending=False)[:top_n]
    except:
        return like_rmd_lst
    for i in range(len(title_movie_sim)):
        if title_movie_sim[title_name][i] > 0.5:
            like_rmd_lst.append(title_movie_sim.index[i])
        else:
            break

    return like_rmd_lst
    
def recommend_like_movie():
    movies = Movie.objects.all()
    movie_df = read_frame(movies)
    users = User.objects.all()
    user_id = []
    movie_id = []
    like_lst = []
    
    for user in users:
        # user_df.loc
        favorite = user.favorite_movies.all()
        for mv in favorite:
            user_id.append(user.id)
            movie_id.append(mv.id)
            like_lst.append(1)
    like_df = pd.DataFrame({"user_id":user_id, "id":movie_id, "like":like_lst})
    like_movies_df = pd.merge(like_df, movie_df, on='id')
    like_movies_matrix = like_movies_df.pivot_table('like', index='user_id', columns='title')
    like_movies_matrix.fillna(0, inplace=True)
    like_movies_matrix_T = like_movies_matrix.transpose()

    item_sim = cosine_similarity(like_movies_matrix_T, like_movies_matrix_T)
    item_sim_df = pd.DataFrame(data=item_sim, index=like_movies_matrix.columns, columns=like_movies_matrix.columns)
    
    return item_sim_df
