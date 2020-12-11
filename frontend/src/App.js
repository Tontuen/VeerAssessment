import React from 'react';
import { BrowserRouter } from 'react-router-dom';
import './App.css';
import history from './history.js';
import Routes from './Routes'


function App() {
    return (
        <BrowserRouter histroy={history}>
            <div className="App">
                <Routes />
            </div>
        </BrowserRouter>
    );
}

export default App;
