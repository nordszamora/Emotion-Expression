# Emotional classification & Analysis
![Screenshot (115)](https://github.com/nordszamora/Emotion-Expression/assets/100557534/d738311f-50d1-41ee-a2a5-4cd314acc199)
### About:
The Machine learning project where user express there emotion and classify at the following (Sad, Joy, Love, Anger, Fear, Surprice). We use a CNB model for text classification with the accuracy of 88%.

#### Data source:

[Emotions](https://www.kaggle.com/datasets/nelgiriyewithana/emotions)

#### Notebook:

[emotion-analysis-and-model](https://www.kaggle.com/code/nordszamora/emotion-analysis-and-model)

[Emotion-Analysis](https://github.com/nordszamora/DS-ML-projects/blob/main/Emotion-Analysis/Emotions.ipynb)

### Note:
The prediction may encounter a unexpected expression result.

### Installation:
Install this project on your local and here are the following steps.

1.) Open your terminal and clone the repo.
```
$ git clone https://github.com/nordszamora/Emotion-Expression

$ cd Emotion-Expression
```
2.) Install dependencies.
```
$ pip install -r requirements.txt

$ python nltk_setup.py
```
3.) Mysql database setup.
```
$ flask db init

$ flask db migrate -m 'emotion'

$ flask db upgrade
```
4.) Run project
```
$ python app.py
```

### Unit test
```
$ cd tests

$ pytest
```
