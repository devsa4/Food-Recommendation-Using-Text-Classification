import pandas as pd
import nltk
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from collections import Counter

# Download stopwords
nltk.download('stopwords')
from nltk.corpus import stopwords
# Load the dataset
from google.colab import files
uploaded = files.upload()

filename = input("Enter the filename (e.g., 'Restaurant reviews.csv'): ")
review_column = input("Enter the column name for reviews: ")
rating_column = input("Enter the column name for ratings: ")

df = pd.read_csv(filename)
def clean_text(text):
    if not isinstance(text, str):
        text = str(text)
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    text = text.split()
    text = [word for word in text if word not in set(stopwords.words('english'))]
    return ' '.join(text)

df[review_column] = df[review_column].astype(str).apply(clean_text)


df[rating_column] = pd.to_numeric(df[rating_column], errors='coerce')


df['Liked'] = (df[rating_column] >= 3).astype(int)
