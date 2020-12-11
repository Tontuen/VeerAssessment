import React, { useState } from 'react';
import history from './history.js';



// # 2. Create a React app that will have two pages, each with a button and a textbox:
// # - switching between pages should not reload the browser (i.e. a single-page application)
// # - the buttons should send a request with and without the required header to the endpoint above
// # - the textbox is where you can display the response


// Page2 is not supposed to link back to Page1
function Page2() {
    const [authorization, setAuthorization] = useState('');

    // Sends a request with headers and the "Authorization" parameter
    // If Authorization == Authorized, then allow access to Page1
    // Otherwise, display unauthorized message in textbox
    function handleClick() {
        fetch('/checkAuth')
            .then(response => response.json())
            .then(data => {
                if (data === true) {
                    history.push('/');
                } else {
                    setAuthorization('You are not authorized')
                }
            });
    };


    return (
        <div>
            <h1>Page 2</h1>
            <button onClick={handleClick}>Go To Page 1</button>
            <textarea value={authorization} />
        </div>
    );
}

export default Page2;
