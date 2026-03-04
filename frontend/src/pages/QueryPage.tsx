import { useState } from 'react'
import './QueryPage.css'

interface QueryResult {
  [key: string]: string | number | boolean | null
}

function QueryPage() {
  const [query, setQuery] = useState("")
  const [results, setResults] = useState<QueryResult[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const submitQuery = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError("")
    setResults([])

    try {
      const apiUrl = `http://${window.location.hostname}:8080`;
      const response = await fetch(`${apiUrl}/api/query`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ query }),
      })

      if (!response.ok) {
        const errorData = await response.json()
        throw new Error(errorData.detail || "Query failed")
      }

      const data = await response.json()
      setResults(data.results)
    } catch (err) {
      setError(err instanceof Error ? err.message : "An error occurred")
    } finally {
      setLoading(false)
    }
  }

  const loadExampleQuery = () => {
    setQuery("SELECT * FROM churn_data LIMIT 10;")
  }

  const renderResultsTable = () => {
    if (results.length === 0) return null

    const columns = Object.keys(results[0])

    return (
      <div className="results-container">
        <h2>Results ({results.length} rows)</h2>
        <div className="table-wrapper">
          <table className="results-table">
            <thead>
              <tr>
                {columns.map((col) => (
                  <th key={col}>{col}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {results.map((row, idx) => (
                <tr key={idx}>
                  {columns.map((col) => (
                    <td key={`${idx}-${col}`}>
                      {String(row[col] ?? "")}
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>
    )
  }

  return (
    <div className="query-page">
      <div className="query-header">
        <h1>SQL Query Interface</h1>
        <p>Execute SQL queries directly on the customer churn database</p>
      </div>

      <div className="query-section">
        <form onSubmit={submitQuery} className="query-form">
          <div className="query-input-container">
            <label htmlFor="sql-query">SQL Query</label>
            <textarea
              id="sql-query"
              rows={8}
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              placeholder="SELECT * FROM churn_data WHERE churn = 'Yes' LIMIT 10;"
              className="query-textarea"
            />
          </div>
          
          <div className="button-group">
            <button type="submit" disabled={loading} className="submit-button">
              {loading ? "Executing..." : "Execute Query"}
            </button>
            <button type="button" onClick={loadExampleQuery} className="example-button">
              Load Example
            </button>
            <button 
              type="button" 
              onClick={() => {
                setQuery("")
                setResults([])
                setError("")
              }} 
              className="clear-button"
            >
              Clear
            </button>
          </div>
        </form>

        {error && (
          <div className="error-message">
            <strong>Error:</strong> {error}
          </div>
        )}

        {renderResultsTable()}
      </div>

      <div className="query-tips">
        <h3>💡 Query Tips</h3>
        <ul>
          <li>Use <code>SELECT * FROM churn_data LIMIT 10</code> to preview the data</li>
          <li>Filter churned customers: <code>WHERE churn = 'Yes'</code></li>
          <li>Aggregate data: <code>SELECT contract, COUNT(*) FROM churn_data GROUP BY contract</code></li>
          <li>Always use <code>LIMIT</code> to avoid retrieving too many rows</li>
        </ul>
      </div>
    </div>
  )
}

export default QueryPage
