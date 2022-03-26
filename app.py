from flask import Flask
from flask_restx import Api

from config import Config

from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from setup_db import db
from views.director import director_ns
from views.genre import genre_ns
from views.movie import movie_ns


def create_app(config_object):
    """create app"""
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    """register extensions"""
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    create_data(app, db)


def create_data(app, db):
    """create data in database"""
    with app.app_context():
        db.drop_all()
        db.create_all()

        d1 = Director(id=1, name='Эльдар Рязанов')
        d2 = Director(id=2, name='Леонид Гайдай')
        d3 = Director(id=3, name='Кеннет Брана')
        d4 = Director(id=4, name='Марк Захаров')
        g1 = Genre(id=1, name='Комедия')
        g2 = Genre(id=2, name='Трагикомедия')
        g3 = Genre(id=3, name='Мюзикл')
        g4 = Genre(id=4, name='Детектив')
        m1 = Movie(id=1, title='Служебный роман',
                   description='Фильм повествует о жизни нескольких сотрудников обычного московского учреждения.',
                   year=1977, rating=10, director_id=1, genre_id=2)
        m2 = Movie(id=2, title='Иван Васильевич меняет профессию.',
                   description='Фильм рассказывает об инженере-изобретателе Шурике, создавшем машину времени, которая открывает двери в 16 век — во времена Ивана Грозного, в результате чего царь оказывается в советской Москве, а его тезка — управдом Иван Бунша вместе с вором-рецидивистом Жоржем Милославским — в палатах царя',
                   year=1973, rating=10, director_id=2, genre_id=1)
        m3 = Movie(id=3, title='Смерть на Ниле',
                   description='Американский фильм в жанре детективной драмы режиссёра Кеннета Браны, снятый по одноимённому роману Агаты Кристи о бельгийском сыщике Эркюле Пуаро.',
                   year=2022, rating=10, director_id=3, genre_id=4)
        m4 = Movie(id=4, title='Обыкновенное чудо',
                   description='Главный герой фильма — Волшебник, который, чтобы развлечь себя и свою жену, выдумывает сказки. Герои сказок оживают, приходят в его дом и начинают жить своей жизнью. Очередная сказка получилась очень грустной.',
                   year=1979, rating=10, director_id=4, genre_id=3)

        with db.session.begin():
            db.session.add_all([d1, d2, d3, d4, g1, g2, g3, g4, m1, m2, m3, m4])


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
