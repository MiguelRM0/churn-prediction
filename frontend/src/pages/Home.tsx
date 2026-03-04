import { Link } from 'react-router-dom'
import './Home.css'

function Home() {
  return (
    <div className="home-container">
      <header className="hero-section">
        <h1>Customer Churn Analytics Platform</h1>
        <p className="subtitle">
          End-to-end machine learning system for predicting and analyzing customer churn
        </p>
      </header>

      <section className="overview-section">
        <h2>Project Overview</h2>
        <p>
          This platform addresses customer churn prediction using real-world telecom data. 
          It combines data engineering, backend development, and machine learning to identify 
          high-risk customers before they leave, enabling proactive retention strategies.
        </p>
      </section>

      <section className="features-grid">
        <div className="feature-card">
          <h3>📊 Data Engineering</h3>
          <ul>
            <li>ETL pipeline with Pandas</li>
            <li>PostgreSQL data warehouse</li>
            <li>Cleaned & normalized dataset</li>
            <li>Schema validation</li>
          </ul>
        </div>

        <div className="feature-card">
          <h3>🔌 Backend API</h3>
          <ul>
            <li>FastAPI REST endpoints</li>
            <li>Docker containerization</li>
            <li>Real-time database queries</li>
            <li>Structured JSON responses</li>
          </ul>
        </div>

        <div className="feature-card">
          <h3>🧠 Machine Learning</h3>
          <ul>
            <li>Logistic Regression model</li>
            <li>K-Fold cross-validation</li>
            <li>Feature engineering pipeline</li>
            <li>Class imbalance handling</li>
          </ul>
        </div>

        <div className="feature-card">
          <h3>💻 Interactive Interface</h3>
          <ul>
            <li>React + TypeScript</li>
            <li>SQL query interface</li>
            <li>Data exploration tools</li>
            <li>Real-time results</li>
          </ul>
        </div>
      </section>

      <section className="tech-stack">
        <h2>Technology Stack</h2>
        <div className="tech-tags">
          <span className="tech-tag">Python</span>
          <span className="tech-tag">FastAPI</span>
          <span className="tech-tag">PostgreSQL</span>
          <span className="tech-tag">React</span>
          <span className="tech-tag">TypeScript</span>
          <span className="tech-tag">Docker</span>
          <span className="tech-tag">Scikit-learn</span>
          <span className="tech-tag">Pandas</span>
        </div>
      </section>

      <section className="cta-section">
        <h2>Explore the Platform</h2>
        <div className="cta-buttons">
          <Link to="/query" className="cta-button primary">
            SQL Query Interface
          </Link>
          <div className="cta-button secondary disabled" title="Coming Soon">
            Model Predictions (Coming Soon)
          </div>
        </div>
      </section>

      <section className="dataset-info">
        <h3>Dataset Information</h3>
        <p>
          <strong>Source:</strong> Telco Customer Churn Dataset<br />
          <strong>Target Variable:</strong> Churn (Yes / No)<br />
          <strong>Problem Type:</strong> Binary Classification<br />
          <strong>Features:</strong> Customer demographics, services, contract details, billing information
        </p>
      </section>
    </div>
  )
}

export default Home
