import './../App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

function Translate() {
    const [getMessage, setGetMessage] = useState({})

    useEffect(()=>{
      axios.post('http://localhost:5000/flask/hello', {write:1}).then(response => {
        console.log("SUCCESS", response)
        setGetMessage(response)
      }).catch(error => {
        console.log(error)
      })
  
    }, [])
    return (
        <div>
            <h1>TRANSLATE</h1>
            <img src="http://localhost:5000/video_feed" className="App-logo handSign" alt="logo"/>
        </div>
    );
}

export default Translate;