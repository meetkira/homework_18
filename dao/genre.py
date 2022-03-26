from sqlalchemy.orm import Session

from dao.model.genre import Genre


class GenreDAO():
    """Genre DAO class"""

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return Genre.query.all()

    def get_one(self, gid):
        return self.session.query(Genre).filter(Genre.id == gid).one()
