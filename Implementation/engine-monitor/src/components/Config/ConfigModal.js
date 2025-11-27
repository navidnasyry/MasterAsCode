import React, { useState } from 'react';

const ConfigModal = ({ show, config, onSave, onClose }) => {
  const [formData, setFormData] = useState(config);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSave(formData);
  };

  const handleChange = (field, value) => {
    setFormData(prev => ({
      ...prev,
      [field]: parseInt(value) || 0
    }));
  };

  if (!show) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <div className="modal-header">
          <h2>⚙️ Monitoring Configuration</h2>
          <button className="close-btn" onClick={onClose}>×</button>
        </div>
        
        <form onSubmit={handleSubmit}>
          <div className="form-group">
            <label htmlFor="threshold">RUL Threshold:</label>
            <input
              type="number"
              id="threshold"
              value={formData.threshold}
              onChange={(e) => handleChange('threshold', e.target.value)}
              min="1"
              max="100"
            />
            <small>Engines with RUL below this value will be shown</small>
          </div>
          
          <div className="form-group">
            <label htmlFor="step">TimeInCycles Step:</label>
            <input
              type="number"
              id="step"
              value={formData.step}
              onChange={(e) => handleChange('step', e.target.value)}
              min="1"
              max="50"
            />
            <small>How much to increase TimeInCycles each iteration</small>
          </div>
          
          <div className="form-group">
            <label htmlFor="interval">Update Interval (ms):</label>
            <input
              type="number"
              id="interval"
              value={formData.interval}
              onChange={(e) => handleChange('interval', e.target.value)}
              min="500"
              max="100000"
              step="500"
            />
            <small>Time between API calls (milliseconds)</small>
          </div>
          
          <div className="form-actions">
            <button type="button" className="btn-cancel" onClick={onClose}>
              Cancel
            </button>
            <button type="submit" className="btn-save">
              Save Configuration
            </button>
          </div>
        </form>
      </div>
    </div>
  );
};

export default ConfigModal;