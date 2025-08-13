import React, { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import './App.css';
import ParticleBackground from './components/ParticleBackground';
import NewsClassifierCard from './components/NewsClassifierCard';
import Navbar from './components/Navbar';

function App() {
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  // Function to classify news text
  const classifyNews = async (newsText) => {
    setIsLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await axios.post('/predict', {
        text: newsText
      });

      setResult(response.data);
    } catch (err) {
      console.error('Classification error:', err);
      setError(
        err.response?.data?.detail || 
        'An error occurred while classifying the news. Please try again.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      {/* Animated particle background */}
      <ParticleBackground />
      
      {/* Navigation Bar */}
      <Navbar />
      
      {/* Main content */}
      <div className="app-container">
        <NewsClassifierCard 
          onClassify={classifyNews}
          isLoading={isLoading}
          result={result}
          error={error}
        />
      </div>
    </div>
  );
}

export default App; 