from app.models.User import User

from app.models.models import db


class UserRepository:

    @staticmethod
    def get_all():
        return db.session.query(User).all()
