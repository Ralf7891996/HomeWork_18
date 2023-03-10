from flask import request
from flask_restx import Resource, Namespace

from dao.model.director import DirectorSchema
from implemented import director_service

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

# создаем CBV для обработки GET и POST запросов
@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    def post(self):
        req_json = request.json
        new_director = director_service.create(req_json)
        return "director_added", 201, {"location": f"/directors/{new_director.id}"}


# создаем CBV для обработки GET, PUT, PATCH и DELETE запросов
@director_ns.route('/<int:did>')
class DirectorView(Resource):
    def get(self, did):
        director = director_service.get_one(did)
        return director_schema.dump(director), 200

    def put(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update(req_json)
        return "director_update", 204

    def patch(self, did):
        req_json = request.json
        req_json["id"] = did
        director_service.update_part(req_json)
        return "director_update", 204

    def delete(self, did):
        director_service.delete(did)
        return "director_deleted", 204
