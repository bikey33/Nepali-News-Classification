from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import os
from pathlib import Path
import logging
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Nepali News Classifier API",
    description="API for classifying Nepali news articles using SVM model",
    version="1.0.0"
)

# Add CORS middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://frontend:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for request validation
class NewsRequest(BaseModel):
    text: str

# Pydantic model for response
class NewsResponse(BaseModel):
    category: str
    confidence: float

# Global variables to store loaded models
svm_model = None
tfidf_vectorizer = None
label_encoder = None

def load_models():
    """
    Load the trained ML models from pickle files.
    Automatically loads the latest models from the models/ directory.
    """
    global svm_model, tfidf_vectorizer, label_encoder
    
    models_dir = Path(__file__).parent / "models"
    
    try:
        # Load SVM model
        svm_path = models_dir / "svm_model.pkl"
        if svm_path.exists():
            svm_model = joblib.load(svm_path)
            logger.info("SVM model loaded successfully")
        else:
            logger.error(f"SVM model not found at {svm_path}")
            
        # Load TF-IDF vectorizer
        tfidf_path = models_dir / "tfidf_vectorizer.pkl"
        if tfidf_path.exists():
            tfidf_vectorizer = joblib.load(tfidf_path)
            logger.info("TF-IDF vectorizer loaded successfully")
        else:
            logger.error(f"TF-IDF vectorizer not found at {tfidf_path}")
            
        # Load Label Encoder
        label_path = models_dir / "label_encoder.pkl"
        if label_path.exists():
            label_encoder = joblib.load(label_path)
            logger.info("Label encoder loaded successfully")
        else:
            logger.error(f"Label encoder not found at {label_path}")
            
    except Exception as e:
        logger.error(f"Error loading models: {str(e)}")
        raise

@app.on_event("startup")
async def startup_event():
    """
    Load models when the application starts.
    """
    logger.info("Starting Nepali News Classifier API...")
    load_models()
    logger.info("API startup complete")

@app.get("/")
async def root():
    """
    Root endpoint to check if the API is running.
    """
    return {
        "message": "Nepali News Classifier API is running",
        "status": "active",
        "models_loaded": all([svm_model, tfidf_vectorizer, label_encoder])
    }

@app.get("/health")
async def health_check():
    """
    Health check endpoint to verify API and model status.
    """
    models_status = {
        "svm_model": svm_model is not None,
        "tfidf_vectorizer": tfidf_vectorizer is not None,
        "label_encoder": label_encoder is not None
    }
    
    return {
        "status": "healthy" if all(models_status.values()) else "unhealthy",
        "models": models_status,
        "message": "All models loaded successfully" if all(models_status.values()) else "Some models failed to load"
    }

@app.post("/predict", response_model=NewsResponse)
async def predict_news_category(request: NewsRequest):
    """
    Predict the category of Nepali news text.
    
    Args:
        request: NewsRequest object containing the news text
        
    Returns:
        NewsResponse object with predicted category and confidence score
    """
    # Check if models are loaded
    if not all([svm_model, tfidf_vectorizer, label_encoder]):
        raise HTTPException(
            status_code=500,
            detail="ML models not loaded. Please check the backend logs."
        )
    
    try:
        # Validate input text
        if not request.text.strip():
            raise HTTPException(
                status_code=400,
                detail="News text cannot be empty"
            )
        
        # Vectorize the input text using TF-IDF
        text_vectorized = tfidf_vectorizer.transform([request.text])
        
        # Make prediction using SVM model
        prediction = svm_model.predict(text_vectorized)
        
        # Get confidence score (use decision function if available, otherwise default to 0.8)
        try:
            # Try to get decision function values
            decision_values = svm_model.decision_function(text_vectorized)
            # Convert decision values to confidence-like scores (0-1 range)
            confidence = float(1.0 / (1.0 + np.exp(-np.max(np.abs(decision_values)))))
        except:
            # Fallback to a default confidence if decision function is not available
            confidence = 0.8
        
        # Decode the predicted label using LabelEncoder
        predicted_category = label_encoder.inverse_transform(prediction)[0]
        
        logger.info(f"Prediction successful: {predicted_category} (confidence: {confidence:.3f})")
        
        return NewsResponse(
            category=predicted_category,
            confidence=confidence
        )
        
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error during prediction: {str(e)}"
        )

@app.post("/reload-models")
async def reload_models():
    """
    Manually reload the ML models from the models/ directory.
    Useful when new model files are added without restarting the service.
    """
    try:
        load_models()
        return {
            "message": "Models reloaded successfully",
            "status": "success"
        }
    except Exception as e:
        logger.error(f"Error reloading models: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Error reloading models: {str(e)}"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 