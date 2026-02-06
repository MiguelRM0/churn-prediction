import { useState } from 'react'
import './App.css'

function Header() {
  return <h2>This is a header component</h2>
}
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <div>
      <Header />
      <h1>Welcome to Churn Prediction</h1>
      <h1>Frontend is alive. </h1>
    </div>
    </>
  )
}

export default App
