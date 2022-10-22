
import './App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function App() {
  const [getMessage, setGetMessage] = useState({})

  useEffect(()=>{
    axios.post('http://localhost:5000/flask/hello', {write:0}).then(response => {
      console.log("SUCCESS", response)
      setGetMessage(response)
    }).catch(error => {
      console.log(error)
    })

  }, [])
  return (
    <div className="App">
      <header className="App-header">
        <img src="http://localhost:5000/video_feed" className="App-logo" alt="logo" />
        <img src="http://localhost:5000/image_feed" className="App-logo" alt="logo" width="450" height="550" margin-top="1000px"/>
      </header>
    </div>
  );
}

export default App;
