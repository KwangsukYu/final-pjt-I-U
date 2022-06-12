from .models import Actor, Movie, Genre
import requests
from .tmdb import TMDB_API_KEY


def makeDB():
    API_KEY = TMDB_API_KEY
    POPULAR_MOVIE_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&language=ko-KR&page='
    GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}&language=ko-KR'
            
    # 장르에 데이터 추가
    genre_data = requests.get(GENRE_URL).json()['genres']
    for data in genre_data:
        Genre.objects.create(genre_id=data['id'], genre_name=data['name'])

            
    # 영화에 데이터 추가
    # 20 페이지까지의 영화 넣기
    for num in range(1, 21):
        url = POPULAR_MOVIE_URL + str(num)
        movie_data = requests.get(url).json()['results']

        for movie in movie_data:
            movie_id = movie.get('id')
            title = movie.get('title')
            overview = movie.get('overview')
            released_date =  movie.get('release_date')
            poster_path = movie.get('poster_path')
            genre_ids = movie.get('genre_ids')
            vote_average = movie.get('vote_average')
            vote_count = movie.get('vote_count')
            popularity = movie.get('popularity')
            Video_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={API_KEY}&language=ko-KR'
            video_data = requests.get(Video_URL).json()['results']
            if video_data:
                video='https://youtube.com/embed/'+ video_data[-1]['key']
                               
            print(video)
            if movie_id and title and overview and released_date and poster_path and genre_ids and vote_average and vote_count and popularity and video:
                m = Movie.objects.create(movie_id=movie_id, title=title, overview=overview, released_date=released_date, poster_path="https://image.tmdb.org/t/p/w500/" + poster_path, vote_average=vote_average, vote_count=vote_count, popularity=popularity, video_path=video)
                # 중개 테이블에 데이터 넣기
                for genre in genre_ids:
                    print(genre)
                    g = Genre.objects.get(genre_id=genre)
                    print(g)
                    m.genres.add(g)

def makeActorDB():
    API_KEY = TMDB_API_KEY
    movies = Movie.objects.all()
    for movie in movies:
        Actor_URL = f'https://api.themoviedb.org/3/movie/{movie.movie_id}/credits?api_key={API_KEY}&language=ko-KR'
        actor_data = requests.get(Actor_URL).json()['cast']
        for data in actor_data:
            if data['profile_path']:
                at = Actor.objects.create(movie_id=movie.movie_id, name=data['name'], character=data['character'], profile_path="https://image.tmdb.org/t/p/w500"+data['profile_path'])
                print(at.name)
                movie.actors.add(at)

def makeVideoDB():
    API_KEY = TMDB_API_KEY
    movies = Movie.objects.all()
    for movie in movies:
        Video_URL = f'https://api.themoviedb.org/3/movie/{movie.movie_id}/videos?api_key={API_KEY}&language=ko-KR'
        video_data = requests.get(Video_URL).json()['results']
        for data in video_data:
            if data['key']:
                youtube_path = 'https://youtube.com/embed/' + data['key']
                movie.video_path.add(youtube_path)
                print(movie.movie_id)
                # print(youtube_path)
                