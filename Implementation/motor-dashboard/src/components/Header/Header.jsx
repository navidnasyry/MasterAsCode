import './Header.css'

const Header = ({ onRefresh, loading }) => {
  return (
    <header className="header">
      <div className="header-content">
        <h1 className="header-title">
          🏭 Motor Monitoring Dashboard
        </h1>
        <div className="header-stats">
          <span className="status-indicator online">
            <span className="dot"></span>
            Real-time Monitoring
          </span>
          <button 
            className="refresh-btn"
            onClick={onRefresh}
            disabled={loading}
          >
            {loading ? '🔄 Refreshing...' : '🔄 Refresh'}
          </button>
        </div>
      </div>
    </header>
  )
}

export default Header