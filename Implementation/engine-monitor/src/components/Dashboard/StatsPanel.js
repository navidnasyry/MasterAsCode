import React from 'react';

const StatsPanel = ({ totalEngines, criticalCount, warningCount, currentClock, threshold }) => {
  const criticalThreshold = threshold / 2;

  return (
    <div className="stats-panel">
      <div className="stat-item">
        <div className="stat-value">{totalEngines}</div>
        <div className="stat-label">Total at Risk</div>
      </div>
      
      <div className="stat-item critical">
        <div className="stat-value">{criticalCount}</div>
        <div className="stat-label">Below {criticalThreshold.toFixed(1)}</div>
      </div>
      
      <div className="stat-item warning">
        <div className="stat-value">{warningCount}</div>
        <div className="stat-label">Below {threshold}</div>
      </div>
      
      <div className="stat-item">
        <div className="stat-value">{currentClock}</div>
        <div className="stat-label">Current TimeInCycles</div>
      </div>
    </div>
  );
};

export default StatsPanel;