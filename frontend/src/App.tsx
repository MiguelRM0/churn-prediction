import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Navigation from './components/Navigation'
import Home from './pages/Home'
import QueryPage from './pages/QueryPage'
import './App.css'

function App() {
  return (
    <Router>
      <div className="app">
        <Navigation />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/query" element={<QueryPage />} />
          </Routes>
        </main>
      </div>
    </Router>
  )
}

export default App
