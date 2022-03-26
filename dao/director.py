from sqlalchemy.orm import Session

from dao.model.director import Director


class DirectorDAO():
    """Director DAO class"""

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        return Director.query.all()

    def get_one(self, did):
        return self.session.query(Director).filter(Director.id == did).one()
