# Project Structure - Nepali News Classifier

This document shows the complete file structure of the Nepali News Classification application.

## 📁 Complete Project Structure

```
News-Classification/
├── 📁 backend/                          # FastAPI Backend
│   ├── 📁 app/
│   │   ├── 📁 models/                   # ML Models Directory
│   │   │   └── 📄 README.md            # Model placement instructions
│   │   ├── 📄 __init__.py              # Python package init
│   │   └── 📄 main.py                  # Main FastAPI application
│   ├── 📄 requirements.txt              # Python dependencies
│   └── 📄 Dockerfile                    # Backend container config
│
├── 📁 frontend/                         # React Frontend
│   ├── 📁 public/
│   │   └── 📄 index.html               # Main HTML file
│   ├── 📁 src/
│   │   ├── 📁 components/              # React components
│   │   │   ├── 📄 NewsClassifierCard.js    # Main classifier card
│   │   │   ├── 📄 NewsClassifierCard.css   # Card styling
│   │   │   ├── 📄 ParticleBackground.js    # Animated particles
│   │   │   └── 📄 ParticleBackground.css   # Particle styling
│   │   ├── 📄 App.js                   # Main app component
│   │   ├── 📄 App.css                  # App-level styling
│   │   ├── 📄 index.js                 # React entry point
│   │   └── 📄 index.css                # Global CSS
│   ├── 📄 package.json                 # Node.js dependencies
│   ├── 📄 Dockerfile                   # Frontend container config
│   └── 📄 nginx.conf                   # Nginx configuration
│
├── 📄 docker-compose.yml               # Service orchestration
├── 📄 README.md                        # Comprehensive documentation
├── 📄 config.env.example               # Environment configuration example
├── 📄 start.sh                         # Linux/Mac startup script
├── 📄 start.bat                        # Windows startup script
├── 📄 test_api.py                      # API testing script
└── 📄 PROJECT_STRUCTURE.md             # This file
```

## 🎯 File Purposes

### Backend Files
- **`backend/app/main.py`**: Core FastAPI application with prediction endpoints
- **`backend/requirements.txt`**: Python package dependencies
- **`backend/Dockerfile`**: Backend container configuration
- **`backend/app/models/README.md`**: Instructions for placing ML models

### Frontend Files
- **`frontend/src/App.js`**: Main React application component
- **`frontend/src/components/NewsClassifierCard.js`**: Main UI card component
- **`frontend/src/components/ParticleBackground.js`**: Animated particle background
- **`frontend/package.json`**: React dependencies and scripts
- **`frontend/Dockerfile`**: Multi-stage frontend container build
- **`frontend/nginx.conf`**: Nginx server configuration

### Configuration Files
- **`docker-compose.yml`**: Orchestrates all services
- **`config.env.example`**: Environment variable template
- **`start.sh`**: Unix/Linux startup script
- **`start.bat`**: Windows startup script

### Documentation
- **`README.md`**: Complete project documentation
- **`PROJECT_STRUCTURE.md`**: This file
- **`test_api.py`**: API testing utility

## 🔧 Key Features Implemented

### ✅ Backend (FastAPI)
- [x] RESTful API with `/predict` endpoint
- [x] Automatic model loading from `models/` directory
- [x] CORS middleware for frontend access
- [x] Health check endpoints
- [x] Model reload functionality
- [x] Comprehensive error handling
- [x] Input validation with Pydantic
- [x] Logging and monitoring

### ✅ Frontend (React)
- [x] Beautiful dark-mode UI with Apple-style design
- [x] Animated particle background with Canvas
- [x] Responsive design for all devices
- [x] Smooth hover effects and animations
- [x] Loading states and error handling
- [x] Axios integration for API calls
- [x] Modern CSS with backdrop blur effects

### ✅ Docker & Deployment
- [x] Multi-stage frontend build
- [x] Optimized backend container
- [x] Nginx reverse proxy for frontend
- [x] Volume mounts for model updates
- [x] Health checks for both services
- [x] Custom network configuration
- [x] Production-ready configuration

### ✅ Development & Testing
- [x] Startup scripts for multiple platforms
- [x] API testing utility
- [x] Comprehensive documentation
- [x] Environment configuration
- [x] Health monitoring
- [x] Easy model replacement

## 🚀 Getting Started

1. **Clone the repository**
2. **Place your ML models** in `backend/app/models/`
3. **Run the application**:
   - **Linux/Mac**: `./start.sh`
   - **Windows**: `start.bat`
   - **Manual**: `docker-compose up --build`

## 🔄 Model Updates

Simply replace the `.pkl` files in `backend/app/models/` and restart the backend:
```bash
docker-compose restart backend
```

## 📱 Access Points

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Health Checks**: 
  - Backend: http://localhost:8000/health
  - Frontend: http://localhost:3000/health

## 🧪 Testing

Run the API test suite:
```bash
python test_api.py
```

## 📊 System Requirements

- **Docker**: 20.10+
- **Docker Compose**: 2.0+
- **Memory**: 4GB+ RAM
- **Storage**: 2GB+ free space
- **Network**: Internet access for initial builds

---

**🎉 Your Nepali News Classifier is ready to use!** 