import React from 'react';
import img from './hookah_logo.jpg';
import HookahList from './hookahs/hookahlist'
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={img} className="App-logo" alt="logo" />
        <p>
          Web App for Hookah Lovers
        </p>
        
          <h1>Hookah Places</h1>
          <HookahList/>
      </header>
    </div>
  );
}

export default App;
