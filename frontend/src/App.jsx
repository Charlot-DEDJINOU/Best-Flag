import React from "react"
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"
import { UserProvider } from "./context/UserProvider"
import Footer from "./components/Footer"
import Header from "./components/Header"
import Home from "./views/Home"
import Substitution from "./views/Substitution"
import Ascii from "./views/Ascii"
import Aes from "./views/Aes"
import Offset from "./views/Offset"
import Rotn from "./views/Rotn"
import NotFound from "./views/NotFound"

function App() {
  return (
    <React.StrictMode>
      <Router>
        <UserProvider>
          <div className="flex flex-col min-h-screen">
            <Header />
            <main className="flex-grow">
              <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/substitution" element={<Substitution />} />
                <Route path="/ascii" element={<Ascii />} />
                <Route path="/aes" element={<Aes />} />
                <Route path="/offset" element={<Offset />} />
                <Route path="/rotn" element={<Rotn />} />
                <Route path="*" element={<NotFound />} />
              </Routes>
            </main>
            <Footer />
          </div>
        </UserProvider>
      </Router>
    </React.StrictMode>
  )
}

export default App