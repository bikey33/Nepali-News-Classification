# Models Directory

This directory should contain the trained machine learning models exported from Google Colab:

1. **svm_model.pkl** - The trained SVM classifier
2. **tfidf_vectorizer.pkl** - The TF-IDF vectorizer fitted on training data
3. **label_encoder.pkl** - The LabelEncoder used for encoding category labels

## How to use:

1. Train your SVM model in Google Colab
2. Export the models using joblib.dump():
   ```python
   import joblib
   
   # Save SVM model
   joblib.dump(svm_model, 'svm_model.pkl')
   
   # Save TF-IDF vectorizer
   joblib.dump(tfidf_vectorizer, 'tfidf_vectorizer.pkl')
   
   # Save LabelEncoder
   joblib.dump(label_encoder, 'label_encoder.pkl')
   ```
3. Place the .pkl files in this directory
4. Restart the FastAPI backend or call the /reload-models endpoint

The backend will automatically load these models on startup. 