import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

df = pd.read_csv("/content/job_pipeline_airflow/data/processed_jobs.csv")

with open("/content/job_pipeline_airflow/models/job_model.pkl", "rb") as f:
    model, vectorizer = pickle.load(f)

X = vectorizer.transform(df["jobdescription"])
y_true = df["industry"]

y_pred = model.predict(X)

accuracy = accuracy_score(y_true, y_pred)

print("Model Accuracy:", accuracy)