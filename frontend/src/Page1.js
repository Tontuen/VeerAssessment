import React, { useState } from 'react';
import history from './history.js';


// # 1. Create a REST API endpoint (preferably using a Python backend, but can be Node as well) that will look for some
// # parameter in the header of the request and deny access if that parameter's value is incorrect or missing
// # (you can call the parameter whatever you like)
// # 2. Create a React app that will have two pages, each with a button and a textbox:
// # - switching between pages should not reload the browser (i.e. a single-page application)
// # - the buttons should send a request with and without the required header to the endpoint above
// # - the textbox is where you can display the response
// # 3. Create another REST API endpoint that will fetch a result from any public API and save the response as a file.


function Page1() {
    const [authorization, setAuthorization] = useState('');

    function handleClick() {
        fetch('/checkAuth', {headers: {'Authorization': 'Authorized'}})
            .then(response => response.json())
            .then(data => {
                setAuthorization(data.authorization);
                if (data.authorization === 'Passed') {
                    history.push('/Page2');
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