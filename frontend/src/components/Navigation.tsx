import { Link, useLocation } from 'react-router-dom'
import './Navigation.css'

function Navigation() {
  const location = useLocation()

  return (
    <nav className="navbar">
      <div className="nav-container">
        <Link to="/" className="nav-logo">
          🔮 Churn Analytics
        </Link>
        
        <ul className="nav-menu">
          <li className="nav-item">
            <Link 
              to="/" 
              className={`nav-link ${location.pathname === '/' ? 'active' : ''}`}
            >
              Home
            </Link>
          </li>

          <li className="nav-item">
            <Link 
              to="/query" 
              className={`nav-link ${location.pathname === '/query' ? 'active' : ''}`}
            >
              SQL Query
            </Link>
          </li>
          <li className="nav-item">
            <span className="nav-link disabled" title="Coming Soon">
              Dashboard
            </span>
          </li>
          <li className="nav-item">
          
            <span className="nav-link disabled" title="Coming Soon">
              Predictions
            </span>
          </li>
        </ul>
      </div>
    </nav>
  )
}

export default Navigation
