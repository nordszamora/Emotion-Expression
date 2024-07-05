from datetime import datetime, timezone
from app.models import Emotion
from tests.conftest import model
from app import db

def test_emotiondb(model):
    
    testdb = Emotion(raw_text='New text data', processed_text='Processed text data', date=datetime.now(timezone.utc), label=1)

    db.session.add(testdb)
    db.session.commit()

    assert testdb
