import React, { useState } from 'react';
import './NewsClassifierCard.css';

const NewsClassifierCard = ({ onClassify, isLoading, result, error }) => {
  const [newsText, setNewsText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (newsText.trim()) {
      onClassify(newsText);
    }
  };

  const handleClear = () => {
    setNewsText('');
  };

  return (
    <div className="news-classifier-card">
      {/* Card container with backdrop blur and gradient */}
      <div className="card-container">
        {/* Title */}
        <div className="card-title">
          <h1>AI News Classifier</h1>
          <p>Powered by Nepal Daily - Intelligent news categorization</p>
        </div>

        {/* Form */}
        <form onSubmit={handleSubmit} className="classification-form">
          <div className="input-group">
            <label htmlFor="news-text">Enter Nepali News Text</label>
            <textarea
              id="news-text"
              value={newsText}
              onChange={(e) => setNewsText(e.target.value)}
              placeholder="Paste your Nepali news article here..."
              rows="8"
              required
              disabled={isLoading}
            />
          </div>

          {/* Action buttons */}
          <div className="button-group">
            <button
              type="submit"
              className="classify-btn"
              disabled={isLoading || !newsText.trim()}
            >
              {isLoading ? (
                <span className="loading-spinner">
                  <div className="spinner"></div>
                  Classifying...
                </span>
              ) : (
                'Classify with AI'
              )}
            </button>
            
            {newsText && (
              <button
                type="button"
                className="clear-btn"
                onClick={handleClear}
                disabled={isLoading}
              >
                Clear
              </button>
            )}
          </div>
        </form>

        {/* Results section */}
        {result && (
          <div className="results-section">
            <div className="result-card">
              <h3>Classification Result</h3>
              <div className="result-content">
                <div className="result-item">
                  <span className="label">Category:</span>
                  <span className="value category">{result.category}</span>
                </div>
                <div className="result-item">
                  <span className="label">Confidence:</span>
                  <span className="value confidence">
                    {(result.confidence * 100).toFixed(1)}%
                  </span>
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Error display */}
        {error && (
          <div className="error-section">
            <div className="error-card">
              <h3>Error</h3>
              <p className="error-message">{error}</p>
            </div>
          </div>
        )}

        {/* Instructions */}
        <div className="instructions">
          <p>
            <strong>Instructions:</strong> Paste your Nepali news text above and click "Classify with AI" 
            to automatically categorize the article using Nepal Daily's advanced AI model.
          </p>
        </div>
      </div>
    </div>
  );
};

export default NewsClassifierCard; 