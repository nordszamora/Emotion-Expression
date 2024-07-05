def test_prediction(client):
    text_data = {'expression': 'Im happy:)'}
    prediction = client.post('/', data=text_data)
    
    assert prediction.status_code == 200

def test_dashboard(client):
    dashboard = client.get('/dashboard')

    assert dashboard.status_code == 200

def test_expression_counts(client):
    expression_counts = client.get('/api/expression_counts')

    assert expression_counts.status_code == 200

def test_emotional_distribution(client):
    emotional_distribution = client.get('/api/emotion_distribution')

    assert emotional_distribution.status_code == 200

def test_common_words(client):
    common_words = client.get('/api/common_words')

    assert common_words.status_code == 200

def test_total_expression(client):
    total_expression = client.get('/api/total_expression')

    assert total_expression.status_code == 200
