
// import './App.css';
// import React, { useEffect, useState } from 'react';
// import axios from 'axios'

// function App() {
//   const [getMessage, setGetMessage] = useState({})

//   useEffect(()=>{
//     axios.post('http://localhost:5000/flask/hello', {id:1}).then(response => {
//       console.log("SUCCESS", response)
//       setGetMessage(response)
//     }).catch(error => {
//       console.log(error)
//     })

//   }, [])
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src="http://localhost:5000/video_feed" className="App-logo" alt="logo" />
//         <p>React + Flask Tutorial</p>
//         <div>{getMessage.status === 200 ? 
//           <h3>{getMessage.data.message}</h3>
//           :
//           <h3>LOADING</h3>}</div>
//       </header>
//     </div>
//   );
// }

// export default App;

import './App.css';
import React, { useState, useEffect } from "react";
import { BrowserRouter, Routes, Route} from 'react-router-dom';
import Practice from './pages/Practice.js';
import Translate from './pages/Translate.js';
import Home from './pages/Home';
import Layout from './pages/Layout';

function App() {
  return (
    <div>
      <BrowserRouter>
        <Routes>
            <Route path="/" element={<Layout />}>
                <Route path="/Home" element={<Home />}/>
                <Route path="/Practice" element={<Practice />}/>
                <Route path="/Translate" element={<Translate />}/>
            </Route>
        </Routes>
        </BrowserRouter>
    </div>
  );
}

export default App;
