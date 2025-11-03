import React, { useState, useEffect } from 'react';
import { checkApiHealth } from '../../services/api';

const Header = ({ onConfigClick, isRunning, currentClock, threshold }) => {
  const [apiStatus, setApiStatus] = useState('checking');

  useEffect(() => {
    const checkStatus = async () => {
      try {
        const health = await checkApiHealth();
        setApiStatus(health.status);
      } catch (error) {
        setApiStatus('unhealthy');
      }
    };

    checkStatus();
    const interval = setInterval(checkStatus, 30000);

    return () => clearInterval(interval);
  }, []);

  const getApiStatusColor = () => {
    switch (apiStatus) {
      case 'healthy': return '#27ae60';
      case 'unhealthy': return '#e74c3c';
      default: return '#f39c12';
    }
  };

  const getApiStatusText = () => {
    switch (apiStatus) {
      case 'healthy': return 'API Connected';
      case 'unhealthy': return 'API Disconnected';
      default: return 'Checking API...';
    }
  };

  return (
    <header className="header">
      <div className="header-content">
        <div className="header-title">
          <h1>🚀 Engine Health Monitor</h1>
          <p>Real-time Remaining Useful Life (RUL) Monitoring System</p>
        </div>
        
        <div className="header-status">
          <div className="api-status" style={{ color: getApiStatusColor() }}>
            ● {getApiStatusText()}
          </div>
          <div className="threshold-display">
            📊 RUL Threshold: {threshold}
          </div>
          <div className={`status-indicator ${isRunning ? 'running' : 'stopped'}`}>
            <span className="status-dot"></span>
            {isRunning ? 'Monitoring' : 'Stopped'}
          </div>
          <div className="clock-display">
            ⏰ Current Clock: {currentClock}
          </div>
          <button 
            className="config-btn"
            onClick={onConfigClick}
          >
            ⚙️ Configuration
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;