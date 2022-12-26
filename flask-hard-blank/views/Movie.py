from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


# создаем CBV для обработки GET и POST запросов
@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        data_req = {"director_id": director_id, "genre_id": genre_id, "year": year}
        all_movies = movie_service.get_all(data_req)
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        new_movie = movie_service.create(data)
        return "movie_added", 201, {"location": f"/movies/{new_movie.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@movie_ns.route("/<int:mid>")
class MovieView(Resource):

    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie)

    def put(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update(data)
        return "movie_update", 204

    def patch(self, mid):
        data = request.json
        data["id"] = mid
        movie_service.update_part(data)
        return "movie_update", 204

    def delete(self, mid):
        movie_service.delete(mid)
        return "movie_deleted", 204
