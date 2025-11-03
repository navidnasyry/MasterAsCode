import React from 'react';

const EngineCard = ({ engine, threshold }) => {
  const getStatus = (rul) => {
    const criticalThreshold = threshold / 2;
    if (rul < criticalThreshold) return 'critical';
    if (rul < threshold) return 'warning';
    return 'normal';
  };

  const status = getStatus(engine.predicted_rul);
  const criticalThreshold = threshold / 2;
  
  const statusIcons = {
    critical: '🔴',
    warning: '🟡',
    normal: '🟢'
  };

  const statusMessages = {
    critical: `CRITICAL: RUL < ${criticalThreshold.toFixed(1)}`,
    warning: `WARNING: RUL < ${threshold}`,
    normal: `NORMAL: RUL >= ${threshold}`
  };

  return (
    <div className={`engine-card ${status}`}>
      <div className="card-header">
        <h3>Engine #{engine.engine_number}</h3>
        <span className="status-icon">{statusIcons[status]}</span>
      </div>
      
      <div className="card-content">
        <div className="metric">
          <label>Predicted RUL:</label>
          <span className={`rul-value ${status}`}>
            {engine.predicted_rul.toFixed(2)} cycles
          </span>
        </div>
        
        <div className="metric">
          <label>Data Until Clock:</label>
          <span>{engine.data_until_clock}</span>
        </div>
        
        <div className="metric">
          <label>Status:</label>
          <span className={`status-badge ${status}`}>
            {status.toUpperCase()}
          </span>
        </div>

        <div className="metric">
          <label>Threshold:</label>
          <span>{threshold} cycles</span>
        </div>

        <div className="metric">
          <label>Critical Level:</label>
          <span>{criticalThreshold.toFixed(1)} cycles</span>
        </div>
      </div>
      
      <div className="status-message">
        {statusMessages[status]}
      </div>
      
      {status === 'critical' && (
        <div className="critical-warning">
          ⚠️ IMMEDIATE MAINTENANCE REQUIRED
        </div>
      )}
    </div>
  );
};

export default EngineCard;