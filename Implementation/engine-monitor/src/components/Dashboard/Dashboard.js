import React from 'react';
import EngineCard from './EngineCard';
import StatsPanel from './StatsPanel';

const Dashboard = ({ engines, isRunning, onStart, onStop, currentClock, threshold }) => {
  const criticalEngines = engines.filter(engine => engine.predicted_rul < (threshold / 2));
  const warningEngines = engines.filter(engine => 
    engine.predicted_rul >= (threshold / 2) && engine.predicted_rul < threshold
  );

  return (
    <div className="dashboard">
      <div className="dashboard-controls">
        <div className="control-buttons">
          <button 
            className={`btn-start ${isRunning ? 'active' : ''}`}
            onClick={onStart}
            disabled={isRunning}
          >
            ▶️ Start Monitoring
          </button>
          <button 
            className={`btn-stop ${!isRunning ? 'active' : ''}`}
            onClick={onStop}
            disabled={!isRunning}
          >
            ⏹️ Stop
          </button>
        </div>
        
        <StatsPanel 
          totalEngines={engines.length}
          criticalCount={criticalEngines.length}
          warningCount={warningEngines.length}
          currentClock={currentClock}
          threshold={threshold}
        />
      </div>

      <div className="alerts-section">
        {criticalEngines.length > 0 && (
          <div className="alert critical-alert">
            ⚠️ CRITICAL: {criticalEngines.length} engines below {threshold / 2} RUL - Immediate maintenance required!
          </div>
        )}
        {warningEngines.length > 0 && (
          <div className="alert warning-alert">
            🔔 WARNING: {warningEngines.length} engines below {threshold} RUL - Approaching critical condition
          </div>
        )}
      </div>

      <div className="engines-grid">
        {engines.length === 0 ? (
          <div className="no-engines">
            <h3>No engines below RUL threshold of {threshold}</h3>
            <p>Start monitoring to see engine status</p>
          </div>
        ) : (
          engines.map(engine => (
            <EngineCard 
              key={`${engine.engine_number}-${engine.data_until_clock}`}
              engine={engine}
              threshold={threshold}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default Dashboard;