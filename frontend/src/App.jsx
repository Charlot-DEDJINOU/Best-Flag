import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { UserProvider } from "./context/UserProvider"
import Footer from "./components/Footer"
import Header from "./components/Header"
import Home from "./views/Home"
import Substitution from "./views/Substitution"
import Ascii from "./views/Ascii"
import Aes from "./views/Aes"

function App() {

  return (
    <React.StrictMode>
        <Router>
            <UserProvider>
              <Header />
              <Routes>
                  <Route path="/" element={ <Home /> } />
                  <Route path="/substitution" element={ <Substitution /> } />
                  <Route path="/ascii" element={ <Ascii /> } />
                  <Route path="/aes" element={ <Aes /> } />
              </Routes>
              <Footer />
            </UserProvider>
        </Router>
    </React.StrictMode>
  )
}

export default App