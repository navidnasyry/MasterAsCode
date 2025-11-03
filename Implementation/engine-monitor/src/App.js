import React, { useState, useEffect } from 'react';
import Header from './components/Layout/Header';
import Dashboard from './components/Dashboard/Dashboard';
import ConfigModal from './components/Config/ConfigModal';
import { fetchEngineData } from './services/api';
import { DEFAULT_CONFIG } from './utils/constants';

function App() {
  const [config, setConfig] = useState(DEFAULT_CONFIG);
  const [engines, setEngines] = useState([]);
  const [isRunning, setIsRunning] = useState(false);
  const [showConfig, setShowConfig] = useState(false);
  const [currentClock, setCurrentClock] = useState(0);

  useEffect(() => {
    let intervalId;

    if (isRunning) {
      intervalId = setInterval(async () => {
        try {
          const data = await fetchEngineData(config.threshold, currentClock);
          setEngines(data.low_rul_engines);
          setCurrentClock(prev => prev + config.step);
        } catch (error) {
          console.error('Error fetching engine data:', error);
        }
      }, config.interval);
    }

    return () => clearInterval(intervalId);
  }, [isRunning, config, currentClock]);

  const handleStart = () => {
    setCurrentClock(0);
    setIsRunning(true);
  };

  const handleStop = () => {
    setIsRunning(false);
  };

  const handleConfigSave = (newConfig) => {
    setConfig(newConfig);
    setShowConfig(false);
    if (isRunning) {
      setIsRunning(false);
    }
  };

  return (
    <div className="app">
      <Header 
        onConfigClick={() => setShowConfig(true)}
        isRunning={isRunning}
        currentClock={currentClock}
        threshold={config.threshold}
      />
      
      <Dashboard 
        engines={engines}
        isRunning={isRunning}
        onStart={handleStart}
        onStop={handleStop}
        currentClock={currentClock}
        threshold={config.threshold}
      />

      <ConfigModal 
        show={showConfig}
        config={config}
        onSave={handleConfigSave}
        onClose={() => setShowConfig(false)}
      />
    </div>
  );
}

export default App;