import axios from 'axios';

// Get API base URL from runtime config or environment variable
const getApiBaseUrl = () => {
  // First check if we have runtime config (for production)
  if (window.RUNTIME_CONFIG && window.RUNTIME_CONFIG.REACT_APP_API_BASE_URL) {
    return window.RUNTIME_CONFIG.REACT_APP_API_BASE_URL;
  }
  // Then check for build-time environment variable (for development)
  return process.env.REACT_APP_API_BASE_URL || 'http://192.168.100.43:8000/api';
};

const API_BASE_URL = getApiBaseUrl();

// Create axios instance with default config
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 60000,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor for logging
apiClient.interceptors.request.use(
  (config) => {
    console.log(`Making API call to: ${config.baseURL}${config.url}`);
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for error handling
apiClient.interceptors.response.use(
  (response) => {
    return response;
  },
  (error) => {
    console.error('API Error:', error);
    
    if (error.response) {
      // Server responded with error status
      console.error('Response data:', error.response.data);
      console.error('Response status:', error.response.status);
    } else if (error.request) {
      // Request made but no response received
      console.error('No response received:', error.request);
    } else {
      // Something else happened
      console.error('Error:', error.message);
    }
    
    throw error;
  }
);

export const fetchEngineData = async (threshold, untilClock) => {
  try {
    console.log(`Fetching engine data with threshold=${threshold}, until_clock=${untilClock}`);
    
    const response = await apiClient.get(
      '/predict/engines_with_low_rul/',
      {
        params: {
          threshold,
          until_clock: untilClock
        }
      }
    );
    
    console.log('API Response:', response.data);
    return response.data;
  } catch (error) {
    console.error('Error fetching engine data:', error);
    
    // Provide fallback data for demo purposes if API is not available
    if (error.code === 'NETWORK_ERROR' || error.message.includes('Network Error')) {
      console.warn('API not available, using demo data');
      return generateDemoData(threshold, untilClock);
    }
    
    throw error;
  }
};

// Demo data generator for when API is not available
const generateDemoData = (threshold, untilClock) => {
  const demoEngines = [];
  const numEngines = Math.min(Math.floor(untilClock / 50), 10); // Max 10 demo engines
  
  for (let i = 1; i <= numEngines; i++) {
    const predictedRul = Math.random() * threshold;
    if (predictedRul < threshold) {
      demoEngines.push({
        engine_number: i,
        predicted_rul: predictedRul,
        data_until_clock: untilClock
      });
    }
  }
  
  return {
    low_rul_engines: demoEngines,
    result_number: demoEngines.length,
    threshold: threshold,
    until_clock: untilClock
  };
};

// Health check function to verify API connectivity
export const checkApiHealth = async () => {
  try {
    const response = await apiClient.get('/health');
    return {
      status: 'healthy',
      data: response.data
    };
  } catch (error) {
    return {
      status: 'unhealthy',
      error: error.message
    };
  }
};