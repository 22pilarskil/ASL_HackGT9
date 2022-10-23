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
        <div id="HomeComponent">
            <h1>TRANSLATE</h1>
            <div id="translate">
            <div id="spacer"></div>
            <p className="pHome"><strong>Directions: </strong>
                Hold up a sign, and the corresponding letter will appear. To delete a letter, make a 
                thumbs down. To use the same sign twice in a row, hold up your open hand like a high-five.
            </p>
            <img src="http://localhost:5000/video_feed" className="App-logo webcam two" alt="logo"/>

            </div>
        </div>
    );
}

export default Translate;