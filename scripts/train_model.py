import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

os.makedirs("/content/job_pipeline_airflow/models", exist_ok=True)

df = pd.read_csv("/content/job_pipeline_airflow/data/processed_jobs.csv")

X = df["jobdescription"]
y = df["industry"]

vectorizer = TfidfVectorizer()
X_vec = vectorizer.fit_transform(X)

model = LogisticRegression()
model.fit(X_vec, y)

with open("/content/job_pipeline_airflow/models/job_model.pkl", "wb") as f:
    pickle.dump((model, vectorizer), f)

print("Model trained and saved successfully.")