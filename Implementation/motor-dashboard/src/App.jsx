import { useState, useEffect } from 'react'
import Header from './components/Header'
import MotorGrid from './components/MotorGrid'
import { getMotorStates } from './services/api'
import './App.css'

function App() {
  const [motorStates, setMotorStates] = useState([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState(null)

  useEffect(() => {
    fetchMotorStates()
    
    // Refresh every 30 seconds
    const interval = setInterval(fetchMotorStates, 30000)
    return () => clearInterval(interval)
  }, [])

  const fetchMotorStates = async () => {
    try {
      const data = await getMotorStates()
      setMotorStates(data.states)
      setLoading(false)
    } catch (err) {
      setError('Failed to fetch motor data')
      setLoading(false)
    }
  }

  return (
    <div className="app">
      <Header onRefresh={fetchMotorStates} loading={loading} />
      <main className="main-content">
        {error ? (
          <div className="error-message">
            <p>{error}</p>
            <button onClick={fetchMotorStates}>Retry</button>
          </div>
        ) : (
          <MotorGrid motors={motorStates} loading={loading} />
        )}
      </main>
    </div>
  )
}

export default App