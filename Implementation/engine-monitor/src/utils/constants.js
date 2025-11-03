export const DEFAULT_CONFIG = {
  threshold: 50,
  step: 10,
  interval: 2000
};

export const STATUS_COLORS = {
  critical: '#dc3545',
  warning: '#ffc107',
  normal: '#28a745'
};

// API configuration
export const API_CONFIG = {
  // This will be populated from environment variables
  BASE_URL: process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000/api',
  TIMEOUT: 10000
};