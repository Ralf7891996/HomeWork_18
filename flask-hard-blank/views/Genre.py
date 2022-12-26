from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')

genres_schema = GenreSchema(many=True)
genre_schema = GenreSchema()


# создаем CBV для обработки GET и POST запросов
@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres)

    def post(self):
        req_json = request.json
        new_genre = genre_service.create(req_json)
        return "genre_added", 201, {"location": f"/genres/{new_genre.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_one(gid)
        return genre_schema.dump(genre)

    def put(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update(req_json)
        return "genre_update", 204

    def patch(self, gid):
        req_json = request.json
        req_json["id"] = gid
        genre_service.update_part(req_json)
        return "genre_update", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "genre_deleted", 204