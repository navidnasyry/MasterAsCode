import './MotorCard.css'

const MotorCard = ({ engine_number, state }) => {
  const isOnline = state === 'ON'
  
  return (
    <div className={`motor-card ${isOnline ? 'online' : 'offline'}`}>
      <div className="motor-icon">
        {isOnline ? '⚡' : '🔴'}
      </div>
      <div className="motor-info">
        <h3 className="motor-title">Motor #{engine_number}</h3>
        <div className="motor-status">
          <span className={`status-badge ${isOnline ? 'online' : 'offline'}`}>
            {isOnline ? 'RUNNING' : 'STOPPED'}
          </span>
        </div>
      </div>
      <div className="motor-indicator">
        <div className={`indicator ${isOnline ? 'online' : 'offline'}`}></div>
      </div>
    </div>
  )
}

export default MotorCard