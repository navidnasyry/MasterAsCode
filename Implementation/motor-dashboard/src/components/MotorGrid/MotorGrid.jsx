import { useState, useMemo } from 'react'
import MotorCard from '../MotorCard'
import './MotorGrid.css'

const MotorGrid = ({ motors, loading }) => {
  const [filter, setFilter] = useState('ALL')

  const filteredMotors = useMemo(() => {
    if (filter === 'ALL') return motors
    return motors.filter(motor => 
      filter === 'ONLINE' ? motor.state === 'ON' : motor.state === 'OFF'
    )
  }, [motors, filter])

  const stats = useMemo(() => {
    const online = motors.filter(m => m.state === 'ON').length
    const offline = motors.filter(m => m.state === 'OFF').length
    return { online, offline, total: motors.length }
  }, [motors])

  if (loading && motors.length === 0) {
    return (
      <div className="loading-container">
        <div className="loading-spinner"></div>
        <p>Loading motor data...</p>
      </div>
    )
  }

  return (
    <div className="motor-grid-container">
      <div className="grid-header">
        <div className="stats-container">
          <div className="stat-card">
            <span className="stat-number">{stats.total}</span>
            <span className="stat-label">Total Motors</span>
          </div>
          <div className="stat-card online">
            <span className="stat-number">{stats.online}</span>
            <span className="stat-label">Online</span>
          </div>
          <div className="stat-card offline">
            <span className="stat-number">{stats.offline}</span>
            <span className="stat-label">Offline</span>
          </div>
        </div>
        
        <div className="filter-controls">
          <button 
            className={`filter-btn ${filter === 'ALL' ? 'active' : ''}`}
            onClick={() => setFilter('ALL')}
          >
            All
          </button>
          <button 
            className={`filter-btn ${filter === 'ONLINE' ? 'active' : ''}`}
            onClick={() => setFilter('ONLINE')}
          >
            Online
          </button>
          <button 
            className={`filter-btn ${filter === 'OFFLINE' ? 'active' : ''}`}
            onClick={() => setFilter('OFFLINE')}
          >
            Offline
          </button>
        </div>
      </div>

      <div className="motor-grid">
        {filteredMotors.map(motor => (
          <MotorCard
            key={motor.engine_number}
            engine_number={motor.engine_number}
            state={motor.state}
          />
        ))}
      </div>

      {filteredMotors.length === 0 && (
        <div className="empty-state">
          <p>No motors found with the selected filter.</p>
        </div>
      )}
    </div>
  )
}

export default MotorGrid