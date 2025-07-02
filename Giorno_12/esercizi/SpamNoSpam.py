import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# NLP & modello
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

df = pd.read_csv("spam.csv", encoding='latin-1')  # usa 'ISO-8859-1' se dà errore
df = df[['v1', 'v2']]  # seleziona solo le colonne utili
df.columns = ['label', 'message']
df.head()

#vado a convertire le due label in 0 e 1 per facilitare la classificazione
df['label_num'] = df.label.map({'ham': 0, 'spam': 1})

X = df['message']
y = df['label_num']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer(stop_words='english')
X_train_vect = vectorizer.fit_transform(X_train)
X_test_vect = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train_vect, y_train)

y_pred = model.predict(X_test_vect)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

