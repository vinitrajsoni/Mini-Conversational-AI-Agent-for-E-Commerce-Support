# Intent Classification App

## Overview
This app classifies user input into predefined intents using a machine learning pipeline built with scikit-learn. It is designed to demonstrate natural language understanding using simple classical NLP techniques.

## Libraries Used
- `pandas` – for data handling
- `scikit-learn` – for ML pipeline and model training
- `joblib` – for saving the model
- `streamlit` – for creating the front-end demo

## Model Architecture
- **Vectorizer**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classifier**: Multinomial Naive Bayes
- The model uses a `Pipeline` object to combine the vectorizer and classifier seamlessly.

## How to Run
1. Install required packages:
   ```bash
   pip install pandas scikit-learn joblib streamlit
