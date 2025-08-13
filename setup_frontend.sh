#!/bin/bash

echo "🔧 Setting up Frontend Dependencies..."
echo

cd frontend

echo "📦 Installing npm dependencies..."
npm install

echo
echo "✅ Frontend setup complete!"
echo "📄 package-lock.json has been generated"
echo
echo "🚀 You can now run: docker-compose up --build" 