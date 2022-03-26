"""Movie CBV"""
from flask import request
from flask_restx import Resource, Namespace

from dao.model.movie import MovieSchema
from implemented import movie_service

movie_ns = Namespace('movies')

movies_schema = MovieSchema(many=True)
movie_schema = MovieSchema()


@movie_ns.route('/')
class MoviesView(Resource):

    def get(self):
        director_id = request.args.get("director_id")
        genre_id = request.args.get("genre_id")
        year = request.args.get("year")
        data = {"director_id": director_id, "genre_id": genre_id, "year": year}
        all_movies = movie_service.get_all(data)
        return movies_schema.dump(all_movies), 200

    def post(self):
        data = request.json
        movie_service.create(data=data)
        return "", 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):

    def get(self, mid):
        try:
            movie = movie_service.get_one(mid=mid)
            return movie_schema.dump(movie), 200
        except Exception:
            return "", 404

    def put(self, mid):
        try:
            data = request.json
            movie_service.update(mid=mid, data=data)
            return "", 204
        except Exception:
            return "", 404

    def delete(self, mid):
        try:
            movie_service.delete(mid=mid)
            return "", 204
        except Exception:
            return "", 404
