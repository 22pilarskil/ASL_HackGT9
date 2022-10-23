import './../App.css';
import React, { useEffect, useState } from 'react';
import axios from 'axios'

import PractCol1 from "../components/PractCol1";
import PractCol2 from "../components/PractCol2";
import Directions from "../components/Directions";

function Practice() {
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
        <div id="allPract">
            <div id="practHeading">
            <h1>PRACTICE</h1>
            </div>
            <div id="practice">
            <PractCol2/>
            <PractCol1/>
            </div>
        </div>
       
    );
}

export default Practice;