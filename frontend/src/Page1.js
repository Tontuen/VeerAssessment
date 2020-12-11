import React, { useState } from 'react';
import history from './history.js';


// # 2. Create a React app that will have two pages, each with a button and a textbox:
// # - switching between pages should not reload the browser (i.e. a single-page application)
// # - the buttons should send a request with and without the required header to the endpoint above
// # - the textbox is where you can display the response


// Page1 is allowed to progress to Page2
function Page1() {
    const [authorization, setAuthorization] = useState('');

    // Sends a request with headers and the "Authorization" parameter
    // If Authorization == Authorized, then allow access to Page2
    // Otherwise, display unauthorized message in textbox
    function handleClick() {
        fetch('/checkAuth', {headers: {'Authorization': 'Authorized'}})
            .then(response => response.json())
            .then(data => {
                if (data === true) {
                    history.push('/Page2');
                } else {
                    setAuthorization('You are not authorized')
                }
            });
    };


    return (
        <div>
            <h1>Page 1</h1>
            <button onClick={handleClick}>Go To Page 2</button>
            <textarea value={authorization} />
        </div>
    );
}

export default Page1;
