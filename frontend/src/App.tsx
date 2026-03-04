import { useState } from 'react'
import './App.css'

interface QueryResult {
  [key: string]: string | number | boolean | null
}

function App() {
  const [query, setQuery]= useState("")
  const [results, setResults] = useState<QueryResult[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState("")

  const submitQuery = async (e: React.FormEvent) => {
    e.preventDefault()
    // Stops page reload 
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

  const renderResultsTable = () => {
    if (results.length === 0) return null

    const columns = Object.keys(results[0])

    return (
      <div style={{ marginTop: "20px", overflowX: "auto" }}>
        <h2 style={{ color: "#000" }}>Results ({results.length} rows)</h2>
        <table style={{
          borderCollapse: "collapse",
          width: "100%",
          border: "2px solid #333",
          fontSize: "14px",
          backgroundColor: "#fff"
        }}>
          <thead>
            <tr style={{ backgroundColor: "#2c3e50", color: "#fff" }}>
              {columns.map((col) => (
                <th key={col} style={{
                  border: "1px solid #555",
                  padding: "12px",
                  textAlign: "left",
                  fontWeight: "bold",
                  color: "#fff"
                }}>
                  {col}
                </th>
              ))}
            </tr>
          </thead>
          <tbody>
            {results.map((row, idx) => (
              <tr key={idx} style={{ backgroundColor: idx % 2 === 0 ? "#f8f9fa" : "#fff" }}>
                {columns.map((col) => (
                  <td key={`${idx}-${col}`} style={{
                    border: "1px solid #ddd",
                    padding: "10px",
                    color: "#000"
                  }}>
                    {String(row[col] ?? "")}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    )
  }

  return (
    <>
    <div>
      <h1>My Query Interface</h1>
      <form onSubmit={submitQuery}>
        <br />
        <textarea
          rows = {5}
          cols = {50}
          value ={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Enter your SQL query here..."/>
          <br/>
          <button type="submit" disabled={loading}>
            {loading ? "Executing..." : "Submit"}
          </button>
      </form>
      {error && <p style={{ color: "red" }}><strong>Error:</strong> {error}</p>}
      {renderResultsTable()}
    </div>
    </>
  )
}
export default App
