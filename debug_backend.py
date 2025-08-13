#!/usr/bin/env python3
"""
Debug script for Nepali News Classifier Backend
Run this to check what's wrong with the backend
"""

import requests
import json
import sys

def check_backend_status():
    """Check if backend is running and models are loaded"""
    print("🔍 Checking Backend Status...")
    print("=" * 40)
    
    try:
        # Check root endpoint
        print("1️⃣ Testing root endpoint...")
        response = requests.get("http://localhost:8000/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint: {data['message']}")
            print(f"   Models loaded: {data['models_loaded']}")
        else:
            print(f"❌ Root endpoint failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Cannot connect to backend: {e}")
        return False
    
    print()
    
    try:
        # Check health endpoint
        print("2️⃣ Testing health endpoint...")
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check: {data['status']}")
            print(f"   Models status:")
            for model, status in data['models'].items():
                print(f"     {model}: {'✅' if status else '❌'}")
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check failed: {e}")
        return False
    
    print()
    
    try:
        # Test prediction with sample text
        print("3️⃣ Testing prediction endpoint...")
        sample_text = "नेपालमा आजको दिन विभिन्न क्षेत्रमा विकासको लागि काम गरिरहेका छन्"
        
        response = requests.post(
            "http://localhost:8000/predict",
            json={"text": sample_text},
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Prediction successful!")
            print(f"   Category: {data['category']}")
            print(f"   Confidence: {data['confidence']:.2%}")
        else:
            print(f"❌ Prediction failed: {response.status_code}")
            error_detail = response.json().get('detail', 'Unknown error')
            print(f"   Error: {error_detail}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Prediction test failed: {e}")
        return False
    
    print()
    print("🎉 All tests passed! Backend is working correctly.")
    return True

def check_models_directory():
    """Check if model files exist"""
    print("📁 Checking Models Directory...")
    print("=" * 40)
    
    import os
    models_dir = "backend/app/models"
    
    if not os.path.exists(models_dir):
        print(f"❌ Models directory does not exist: {models_dir}")
        return False
    
    print(f"✅ Models directory exists: {models_dir}")
    
    # Check for required model files
    required_files = [
        "svm_model.pkl",
        "tfidf_vectorizer.pkl", 
        "label_encoder.pkl"
    ]
    
    missing_files = []
    for file in required_files:
        file_path = os.path.join(models_dir, file)
        if os.path.exists(file_path):
            size = os.path.getsize(file_path)
            print(f"✅ {file}: {size:,} bytes")
        else:
            print(f"❌ {file}: MISSING")
            missing_files.append(file)
    
    if missing_files:
        print(f"\n⚠️  Missing model files: {', '.join(missing_files)}")
        print("   Please place your trained ML models in the models directory.")
        return False
    else:
        print("\n✅ All required model files are present!")
        return True

def main():
    """Main debug function"""
    print("🐛 Nepali News Classifier Backend Debug Tool")
    print("=" * 50)
    print()
    
    # Check models directory first
    models_ok = check_models_directory()
    print()
    
    if not models_ok:
        print("❌ Model files are missing. Please add them before testing the backend.")
        return 1
    
    # Check backend status
    backend_ok = check_backend_status()
    
    if backend_ok:
        return 0
    else:
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⏹️  Debug interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 