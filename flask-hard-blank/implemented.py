# файл для создания DAO и сервисов чтобы импортировать их везде
from dao.DirectorDAO import DirectorDAO
from dao.GenreDAO import GenreDAO
from dao.MovieDAO import MovieDAO
from service.DirectorService import DirectorService
from service.GenreService import GenreService
from service.MovieService import MovieService
from setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(dao=movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(dao=director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(dao=genre_dao)


