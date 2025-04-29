
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
df = pd.read_csv("mock_intents.csv")

# pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
])

# Train model
pipeline.fit(df["User_Query"], df["Intent"])

# Save model
with open("intent_model.pkl", "wb") as f:
    pickle.dump(pipeline, f)
