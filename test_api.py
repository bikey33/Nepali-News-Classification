#!/usr/bin/env python3
"""
Test script for Nepali News Classifier API
Run this script to test the backend API endpoints
"""

import requests
import json
import time
import sys

# API base URL
BASE_URL = "http://localhost:8000"

def test_health_endpoint():
    """Test the health check endpoint"""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data['status']}")
            print(f"   Models loaded: {data['models']}")
            return True
        else:
            print(f"❌ Health check failed with status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_root_endpoint():
    """Test the root endpoint"""
    print("🏠 Testing root endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Root endpoint working: {data['message']}")
            return True
        else:
            print(f"❌ Root endpoint failed with status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Root endpoint failed: {e}")
        return False

def test_prediction_endpoint():
    """Test the prediction endpoint with sample Nepali text"""
    print("🔮 Testing prediction endpoint...")
    
    # Sample Nepali news text (you can replace this with actual text)
    sample_text = """
    नेपालमा आजको दिन विभिन्न क्षेत्रमा विकासको लागि काम गरिरहेका छन्। 
    सरकारले नयाँ योजनाहरू सुरु गरेको छ र जनताले यसको लाभ लिन सुरु गरेका छन्। 
    यो विकासले देशको अर्थतन्त्रलाई मजबुत बनाउनेछ।
    """
    
    payload = {"text": sample_text.strip()}
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            json=payload,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Prediction successful!")
            print(f"   Category: {data['category']}")
            print(f"   Confidence: {data['confidence']:.2%}")
            return True
        else:
            print(f"❌ Prediction failed with status {response.status_code}")
            if response.status_code == 500:
                print(f"   Error: {response.json().get('detail', 'Unknown error')}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Prediction failed: {e}")
        return False

def test_reload_models():
    """Test the model reload endpoint"""
    print("🔄 Testing model reload endpoint...")
    try:
        response = requests.post(f"{BASE_URL}/reload-models")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Model reload successful: {data['message']}")
            return True
        else:
            print(f"❌ Model reload failed with status {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"❌ Model reload failed: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Nepali News Classifier API Test Suite")
    print("=" * 50)
    
    # Wait a bit for services to start
    print("⏳ Waiting for API to be ready...")
    time.sleep(2)
    
    tests = [
        test_root_endpoint,
        test_health_endpoint,
        test_prediction_endpoint,
        test_reload_models
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
            print()
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! API is working correctly.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the API logs.")
        return 1

if __name__ == "__main__":
    try:
        exit_code = main()
        sys.exit(exit_code)
    except KeyboardInterrupt:
        print("\n\n⏹️  Testing interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1) 