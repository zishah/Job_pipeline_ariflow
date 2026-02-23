import pandas as pd

df = pd.read_csv("/content/job_pipeline_airflow/data/raw_jobs.csv")

# Basic cleaning
df = df.dropna()
df["jobdescription"] = df["jobdescription"].str.lower()

df.to_csv("/content/job_pipeline_airflow/data/processed_jobs.csv", index=False)

print("Data preprocessing complete.")