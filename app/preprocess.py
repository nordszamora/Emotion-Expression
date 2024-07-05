from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import re

lemma = WordNetLemmatizer()

def preprocessed_text(text):
    regex = re.sub(r'[^a-zA-Z\s]', '', text)
    stop_words = set(stopwords.words('english'))
    tokenize = word_tokenize(regex.lower())
    process_words = [lemma.lemmatize(word) for word in tokenize if word not in stop_words]
    return ' '.join(process_words)
