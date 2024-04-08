import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Header from "./components/commons/Header"
import Home from "./views/Home"

function App() {

  return (
    <React.StrictMode>
        <Router>
            <Header />
            <Routes>
                <Route path="/" element={ <Home />} />
            </Routes>
            <Footer />
        </Router>
    </React.StrictMode>
  )
}

export default App
