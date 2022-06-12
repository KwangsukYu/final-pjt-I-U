from .models import Movie, Genre
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from django_pandas.io import read_frame

def make_recommend_movie(df, movie_title, genre_cosine_sim, top=20):
    target_movie_index = df[df['title'] == movie_title].index.values
    # cosine similarity 중 해당 값과 비슷한 cosine similarity 20개를 구함
    sim_index = genre_cosine_sim[target_movie_index, : top].reshape(-1)
    # 이름이 같은 영화는 제외
    sim_index = sim_index[sim_index != target_movie_index]

    result = df.iloc[sim_index].sort_values('vote_count', ascending=False)[:5]
    result = result[['id', 'title']]
    return result

def movie_recommend():
    movies = Movie.objects.all()
    df = read_frame(movies)
    # 영화 장르 리스트 불러오기
    genre_lst = []
    for movie in movies:
        movie_genre =[]
        genres = movie.genres.all()
        # 각 영화의 분류된 장르들을 genre_lst에 담고
        for genre in genres:
            movie_genre.append(genre.genre_name)
        genre_lst+=[movie_genre]
    genre_lst = [[" ".join(x)] for x in genre_lst]
    print(genre_lst)
    # 장르 리스트 데이터프레임 형태로 변경
    genre_df = pd.DataFrame({'genre_lst':genre_lst})
    # 기존의 영화 데이터와 합치기
    movie_data = pd.concat([df, genre_df], axis=1)
    # 장르 전처리
    movie_data['genre_lst'] = movie_data['genre_lst'].apply(lambda x: " ".join(x))
    # 각 장르들의 문자열 값을 숫자로 벡터화
    count_vector = CountVectorizer(ngram_range=(1,3))
    genre_cosine_vector = count_vector.fit_transform(movie_data['genre_lst'])
    # 장르의 consine similarity를 구한 벡터 값을 구함
    genre_cosine_sim = cosine_similarity(genre_cosine_vector, genre_cosine_vector).argsort()[:,::-1]
    print(genre_cosine_sim)
    for movie in movies:
        title = movie.title
        
        try:
            recommend_movie = make_recommend_movie(movie_data, title, genre_cosine_sim)
            print(recommend_movie)
            for movie_id in recommend_movie['id']:
                m = Movie.objects.get(pk=movie_id)
                movie.recommend_movies.add(m)
        except ValueError:
            continue
        