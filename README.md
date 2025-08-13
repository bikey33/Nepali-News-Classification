# Nepali News Classifier

A complete web application for classifying Nepali news articles using machine learning. Built with React frontend, FastAPI backend, and Docker deployment.

## 🚀 Features

- **AI-Powered Classification**: Uses trained SVM model for accurate news categorization
- **Beautiful UI**: Modern, dark-mode animated interface with particle effects
- **Real-time Processing**: Instant classification with confidence scores
- **Easy Model Updates**: Hot-swappable ML models without code changes
- **Production Ready**: Docker-based deployment with health checks
- **Responsive Design**: Works seamlessly on all devices

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   React Frontend│    │  FastAPI Backend│    │  ML Models      │
│   (Port 3000)   │◄──►│   (Port 8000)   │◄──►│  (.pkl files)  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.11+ (for local development)
- Node.js 18+ (for local development)
- Trained ML models (.pkl files)

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <repository-url>
cd News-Classification
```

### 2. Prepare ML Models
Place your trained ML model files in `backend/app/models/`:
- `svm_model.pkl` - Trained SVM classifier
- `tfidf_vectorizer.pkl` - TF-IDF vectorizer
- `label_encoder.pkl` - Label encoder

### 3. Run with Docker
```bash
# Build and start all services
docker-compose up --build

# Or run in background
docker-compose up -d --build
```

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

## 🛠️ Development Setup

### Backend Development
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

### Frontend Development
```bash
cd frontend
npm install
npm start
```

## 📁 Project Structure

```
News-Classification/
├── backend/                 # FastAPI backend
│   ├── app/
│   │   ├── main.py         # Main FastAPI application
│   │   ├── models/         # ML model files directory
│   │   └── __init__.py
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile         # Backend container
├── frontend/               # React frontend
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── App.js          # Main app component
│   │   └── index.js        # Entry point
│   ├── package.json        # Node.js dependencies
│   ├── Dockerfile          # Frontend container
│   └── nginx.conf          # Nginx configuration
├── docker-compose.yml      # Service orchestration
└── README.md               # This file
```

## 🔧 API Endpoints

### Backend API (FastAPI)

- `GET /` - Health check and status
- `GET /health` - Detailed health status
- `POST /predict` - Classify news text
- `POST /reload-models` - Reload ML models

### Request Format
```json
{
  "text": "Your Nepali news text here..."
}
```

### Response Format
```json
{
  "category": "predicted_category",
  "confidence": 0.95
}
```

## 🎨 Frontend Features

- **Particle Animation**: Smooth, looping particle effects
- **Responsive Design**: Mobile-first approach
- **Dark Theme**: Modern, eye-friendly interface
- **Smooth Animations**: CSS transitions and transforms
- **Error Handling**: User-friendly error messages
- **Loading States**: Visual feedback during processing

## 🔄 Model Updates

### Automatic Updates
1. Place new `.pkl` files in `backend/app/models/`
2. Restart the backend service:
   ```bash
   docker-compose restart backend
   ```

### Manual Reload
Call the reload endpoint:
```bash
curl -X POST http://localhost:8000/reload-models
```

## 🐳 Docker Commands

### Useful Commands
```bash
# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Rebuild and restart
docker-compose up --build

# View running containers
docker-compose ps

# Access backend container
docker-compose exec backend bash

# Access frontend container
docker-compose exec frontend sh
```

### Health Checks
- Backend: http://localhost:8000/health
- Frontend: http://localhost:3000/health

## 🧪 Testing

### Backend Testing
```bash
cd backend
python -m pytest tests/
```

### Frontend Testing
```bash
cd frontend
npm test
```

## 📊 Performance

- **Backend**: Optimized for concurrent requests
- **Frontend**: Lazy loading and code splitting
- **Models**: Efficient loading and caching
- **Docker**: Multi-stage builds for optimization

## 🔒 Security

- CORS configuration for frontend access
- Input validation and sanitization
- Secure headers in nginx
- Environment variable management

## 🚀 Deployment

### Production Deployment
1. Update environment variables
2. Use production Docker images
3. Configure reverse proxy
4. Set up SSL certificates
5. Monitor with health checks

### Environment Variables
```bash
# Backend
PYTHONPATH=/app
PYTHONUNBUFFERED=1

# Frontend
REACT_APP_API_URL=https://your-api-domain.com
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License.

## 🆘 Support

For issues and questions:
1. Check the documentation
2. Review existing issues
3. Create a new issue with details

## 🔮 Future Enhancements

- [ ] User authentication
- [ ] Batch processing
- [ ] Model versioning
- [ ] Performance metrics
- [ ] Multi-language support
- [ ] Advanced analytics dashboard

---

**Built with ❤️ using React, FastAPI, and Docker** 