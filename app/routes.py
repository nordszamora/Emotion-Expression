from flask import Blueprint, request, render_template, jsonify
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from app.preprocess import preprocessed_text
from app.models import Emotion
from datetime import datetime
from collections import Counter
from . import db
import pandas as pd
import joblib
import os

try:
    # Load model & Converter
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model/emotion_model.joblib')
    VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), 'model/vectorizer.joblib')

    model = joblib.load(open(MODEL_PATH, 'rb'))
    vectorizer = joblib.load(open(VECTORIZER_PATH, 'rb'))
except Exception as e:
    print(f'An error occurred: {e}')

try:
    # Connect db for pandas
    engine = create_engine('mysql://<user>:@<host>:<port>/<database>') # Edit
    connection = engine.connect()
    print('Connection to the database was successful.')
    connection.close()
except SQLAlchemyError as e:
    print(f'An error occurred: {e}')

blueprint = Blueprint('blue_print', __name__)

@blueprint.route('/', methods=['GET', 'POST'])
def predict_emotional_expression():
    if request.method == 'POST':

       text = request.form.get('expression')
       preprocessed = preprocessed_text(text) # Preprocess new textual data

       # Predict new textual data
       converted_text = vectorizer.transform([preprocessed])
       prediction = model.predict(converted_text)[0]
       probability = f'{(model.predict_proba(converted_text)[0][prediction] * 100):.0f}%'

       # Add new textual data
       new_text_data = Emotion(raw_text=text, processed_text=preprocessed, label=prediction)
       db.session.add(new_text_data)
       db.session.commit()

       return render_template('index.html', predicted=prediction, proba=probability)
    
    return render_template('index.html')

@blueprint.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@blueprint.route('/api/total_expression')
def total():
    total_expression = Emotion.query.count() 

    return jsonify({'total_expression': total_expression})

@blueprint.route('/api/expression_counts')
def linechart():
    expression_date = Emotion.query.all()

    # Filter date format
    monthly_expression = []
    for date in expression_date:
        month_ = datetime.strptime(str(date.date), "%Y-%m-%d %H:%M:%S")
        month = month_.strftime("%Y-%m")
        monthly_expression.append(month)

    # Count date
    counts = Counter(monthly_expression)

    return jsonify({'date_counts': counts})

@blueprint.route('/api/emotion_distribution')
def doughnutchart():
    data = pd.read_sql('SELECT label FROM emotion', con=engine)
    
    # Filter emotional distribution
    distribution = {
        'Sad': data.query('label == 0').shape[0],
        'Joy': data.query('label == 1').shape[0],
        'Love': data.query('label == 2').shape[0],
        'Anger': data.query('label == 3').shape[0],
        'Fear': data.query('label == 4').shape[0],
        'Surprice': data.query('label == 5').shape[0]
    }

    return jsonify({'distribution': distribution})

@blueprint.route('/api/common_words')
def barchart_and_wordcloud():
    common_words = Emotion.query.all()

    text_words = []
    for data in common_words:
        text_words.append(data.processed_text)
    
    split_words = ' '.join(text_words)
    words = Counter(split_words.split()) # Count common words

    return jsonify({'common_words': words})
