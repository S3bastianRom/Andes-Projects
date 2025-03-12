from ..config.db import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    __tablename__ ='usuario'
    #PK
    id = db.Column(db.Integer, primary_key = True, nullable = False ,autoincrement = True)
    #Columns
    username = db.Column (db.String(500))
    password  = db.Column (db.String(500))
    es_admin = db.Column (db.Boolean)

    @classmethod
    def create_test_users(cls):
        if not cls.query.first():
            users = [
                cls(username="admin", password=("admin123"), es_admin = False),
                cls(username="user1", password=("user123"), es_admin = False),
                cls(username="testuser", password=("test123"), es_admin = False),
                cls(username="sebas", password=("1234"), es_admin = True),
            ]
            db.session.bulk_save_objects(users)
            db.session.commit()