# Job_pipeline_ariflow

Automated Job Classification Pipeline using Apache Airflow

Project Overview

This project demonstrates a production-style ML retraining pipeline orchestrated using Apache Airflow.

#The pipeline:
Preprocesses raw job data
Trains a text classification model
Evaluates model performance
Saves the trained model


#Tech Stack:
Python
Pandas
Scikit-learn
Apache Airflow
TF-IDF Vectorization
Logistic Regression


#Output:
Processed dataset (processed_jobs.csv)
Trained model (job_model.pkl)
Evaluation accuracy logged in console

#DAG Schedule:
Runs daily using Airflow scheduler.
