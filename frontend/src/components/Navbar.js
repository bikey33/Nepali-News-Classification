import React, { useState } from 'react';
import './Navbar.css';

const Navbar = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Brand/Logo */}
        <div className="navbar-brand">
          <h1 className="brand-name">Nepal Daily</h1>
          <span className="brand-tagline">AI-Powered News Intelligence</span>
        </div>

        {/* Navigation Menu */}
        <div className={`navbar-menu ${isMenuOpen ? 'active' : ''}`}>
          <ul className="nav-links">
            <li className="nav-item">
              <a href="#news-summary" className="nav-link">
                <span className="nav-icon">📰</span>
                News Summary
              </a>
            </li>
            <li className="nav-item">
              <a href="#categories" className="nav-link">
                <span className="nav-icon">🏷️</span>
                Categories
              </a>
            </li>
            <li className="nav-item">
              <a href="#subscriptions" className="nav-link">
                <span className="nav-icon">🔔</span>
                Subscriptions
              </a>
            </li>
          </ul>
        </div>

        {/* Mobile Menu Toggle */}
        <div className="navbar-toggle" onClick={toggleMenu}>
          <span className={`hamburger ${isMenuOpen ? 'active' : ''}`}></span>
        </div>
      </div>
    </nav>
  );
};

export default Navbar; 