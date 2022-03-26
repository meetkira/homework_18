from sqlalchemy.orm import Session

from dao.model.movie import Movie


class MovieDAO():
    """Movie DAO class"""

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return Movie.query.all()

    def get_by_director_id(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def get_by_genre_id(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def get_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

        return movie

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, movie):
        self.session.delete(movie)
        self.session.commit()
