import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import Home from "./views/Home"
import Footer from "./components/Footer"
import Substitution from "./views/Substitution"

function App() {

  return (
    <React.StrictMode>
        <Router>
            <Routes>
                <Route path="/" element={ <Home /> } />
                <Route path="/substitution" element={ <Substitution /> } />
            </Routes>
            <Footer />
        </Router>
    </React.StrictMode>
  )
}

export default App