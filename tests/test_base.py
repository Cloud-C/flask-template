from app import create_app
from app.models.models import db


class TestBase:

    def setup(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.db = db
        self.db.drop_all()
        self.db.create_all()
        self.test_client = self.app.test_client()

    def teardown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()
