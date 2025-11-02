import axios from 'axios'

// Runtime configuration - will be set from window environment
const getApiBaseUrl = () => {
  // Use window environment variable if available (set by Docker)
  if (window._env_ && window._env_.VITE_API_URL) {
    return window._env_.VITE_API_URL
  }
  // Fallback to build-time environment variable
  return import.meta.env.VITE_API_URL || 'http://localhost:3001/api'
}

const api = axios.create({
  baseURL: getApiBaseUrl(),
  timeout: 10000,
})

export const getMotorStates = async () => {
  try {
    const response = await api.get('/states/all')
    return response.data
  } catch (error) {
    console.error('API Error:', error)
    throw new Error('Failed to fetch motor data: ' + error.message)
  }
}

export default api