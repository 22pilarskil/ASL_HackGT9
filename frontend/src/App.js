
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
