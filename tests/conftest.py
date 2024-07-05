from app import create_app, db
import pytest

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
         yield client

@pytest.fixture
def model():
    app = create_app()

    with app.app_context():
         db.create_all()
         yield model
