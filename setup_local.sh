#!/bin/bash

echo "🚀 Setting up Nepali News Classifier for Local Development"
echo "========================================================"
echo

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js 18+ and try again."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3.11+ and try again."
    exit 1
fi

echo "✅ Prerequisites check passed"
echo

echo "🔧 Setting up Frontend..."
cd frontend
echo "📦 Installing npm dependencies..."
npm install
if [ $? -ne 0 ]; then
    echo "❌ Frontend setup failed"
    exit 1
fi
echo "✅ Frontend setup complete"
cd ..

echo
echo "🔧 Setting up Backend..."
cd backend
echo "📦 Installing Python dependencies..."
python3 -m pip install -r requirements.txt 2>/dev/null || python -m pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "❌ Backend setup failed"
    exit 1
fi
echo "✅ Backend setup complete"
cd ..

echo
echo "🎉 Setup complete! You can now:"
echo
echo "📱 Run Frontend: cd frontend && npm start"
echo "🔧 Run Backend: cd backend && python -m uvicorn app.main:app --reload"
echo "🐳 Or use Docker: docker-compose up --build"
echo
echo "📍 Frontend will be at: http://localhost:3000"
echo "📍 Backend will be at: http://localhost:8000"
echo 