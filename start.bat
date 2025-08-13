@echo off
chcp 65001 >nul
echo 🚀 Starting Nepali News Classifier...

REM Check if Docker is running
docker info >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker is not running. Please start Docker and try again.
    pause
    exit /b 1
)

REM Check if Docker Compose is available
docker-compose --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Docker Compose is not installed. Please install Docker Compose and try again.
    pause
    exit /b 1
)

REM Check if models directory exists and has files
if not exist "backend\app\models\*.pkl" (
    echo ⚠️  Warning: No ML model files found in backend\app\models\
    echo    Please place your trained models (.pkl files) in the models directory:
    echo    - svm_model.pkl
    echo    - tfidf_vectorizer.pkl
    echo    - label_encoder.pkl
    echo.
    set /p "continue=Continue anyway? (y/N): "
    if /i not "%continue%"=="y" (
        echo ❌ Startup cancelled.
        pause
        exit /b 1
    )
)

echo 🔧 Building and starting services...
docker-compose up --build -d

REM Wait for services to be ready
echo ⏳ Waiting for services to be ready...
timeout /t 10 /nobreak >nul

REM Check service health
echo 🏥 Checking service health...

REM Check backend
curl -f http://localhost:8000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Backend is healthy
) else (
    echo ❌ Backend health check failed
)

REM Check frontend
curl -f http://localhost:3000/health >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Frontend is healthy
) else (
    echo ❌ Frontend health check failed
)

echo.
echo 🎉 Nepali News Classifier is starting up!
echo.
echo 📱 Frontend: http://localhost:3000
echo 🔧 Backend API: http://localhost:8000
echo 📚 API Documentation: http://localhost:8000/docs
echo.
echo 📋 Useful commands:
echo    View logs: docker-compose logs -f
echo    Stop services: docker-compose down
echo    Restart: docker-compose restart
echo.
echo 🚀 Happy classifying!
pause 