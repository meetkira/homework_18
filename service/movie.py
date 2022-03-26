from dao.movie import MovieDAO


class MovieService:
    """Movie Service class"""

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self, data):
        if data["director_id"]:
            return self.dao.get_by_director_id(director_id=data["director_id"])
        elif data["genre_id"]:
            return self.dao.get_by_genre_id(genre_id=data["genre_id"])
        elif data["year"]:
            return self.dao.get_by_year(year=data["year"])
        else:
            return self.dao.get_all()

    def get_one(self, mid):
        return self.dao.get_one(mid=mid)

    def create(self, data):
        return self.dao.create(data=data)

    def update(self, mid, data):
        movie = self.get_one(mid)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.dao.update(movie=movie)

    def delete(self, mid):
        movie = self.get_one(mid)
        self.dao.delete(movie=movie)
