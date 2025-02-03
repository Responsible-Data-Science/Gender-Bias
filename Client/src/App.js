import logo from './logo.svg';
import './App.css';
import HomePage from './HomePage';
import React, { useState, useEffect } from 'react';
function App() {
  useEffect(() => {
  const requestOptions = {
    method: "GET",
    redirect: "follow"
  };
  
  fetch("http://127.0.0.1:5000/", requestOptions)
    .then((response) => response.text())
    .then((result) => console.log(result))
    .catch((error) => console.error(error));
},[])
  return (
    <div className="App">
      <header className="App-header">
        <HomePage/>
        {/* <img src={logo} className="App-logo" alt="logo" /> */}
          {/* <form>
          <label>
            Name:
            <input type="text" name="name" />
          </label>
          <input type="submit" value="Submit" />
        </form> */}
        {/* <p>
          Edit <code>src/App.js</code> and save to reload.
        </p> */}
        {/* <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a> */}
      </header>
    </div>
  );
}

export default App;
