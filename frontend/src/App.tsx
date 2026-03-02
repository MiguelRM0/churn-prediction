import { useState } from 'react'
import './App.css'

function App() {
  const [query, setQuery]= useState("")
  // typical return ["", functiontoUpdateIt]
  // typle unpacking 
  // const query = returnedArray[0]
  // const setQuery = retunedArray[1]
  const [result, setResult] = useState("")
  const submitQuery = async (e: React.FormEvent) => {
    e.preventDefault()
    // Stops page reload 

    setResult(`You entered:\n${query}`)
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
          onChange={(e) => setQuery(e.target.value)}/>
          <br/>
          <button type="submit">Submit</button>

      </form>
       <pre>{result}</pre>
    </div>
    </>
  )
}

export default App
