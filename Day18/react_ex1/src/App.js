// import './App.css';
// import Header from './components/Header.js'
// import Body from './components/Body'
// import Footer from './components/Footer'
// import InterestCalculator from './components/InterestCalculator'

// function App() {
//   return (
//     <div className="App">
//       {/* <h1>Hello</h1> */}
//       {/* <Header/>
//       <Body/>
//       <Footer/> */}
//       <InterestCalculator/>
//     </div>
//   );
// }

// export default App;

import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

// Simple components
const Home = () => <h2>Home Page</h2>;
const About = () => <h2>About Page</h2>;

export default function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/about">About</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/about" element={<About />} />
      </Routes>
    </Router>
  );
}
