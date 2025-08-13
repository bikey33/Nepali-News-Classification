@echo off
chcp 65001 >nul
echo 🚀 Setting up Nepali News Classifier for Local Development
echo ========================================================
echo.

REM Check if Node.js is installed
node --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Node.js is not installed. Please install Node.js 18+ and try again.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python is not installed. Please install Python 3.11+ and try again.
    pause
    exit /b 1
)

echo ✅ Prerequisites check passed
echo.

echo 🔧 Setting up Frontend...
cd frontend
echo 📦 Installing npm dependencies...
npm install
if %errorlevel% neq 0 (
    echo ❌ Frontend setup failed
    pause
    exit /b 1
)
echo ✅ Frontend setup complete
cd ..

echo.
echo 🔧 Setting up Backend...
cd backend
echo 📦 Installing Python dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo ❌ Backend setup failed
    pause
    exit /b 1
)
echo ✅ Backend setup complete
cd ..

echo.
echo 🎉 Setup complete! You can now:
echo.
echo 📱 Run Frontend: cd frontend && npm start
echo 🔧 Run Backend: cd backend && python -m uvicorn app.main:app --reload
echo 🐳 Or use Docker: docker-compose up --build
echo.
echo 📍 Frontend will be at: http://localhost:3000
echo 📍 Backend will be at: http://localhost:8000
echo.
pause 