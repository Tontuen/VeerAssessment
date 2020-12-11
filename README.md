# VeerAssessment
Requirements:
1. Create a REST API endpoint (preferably using a Python backend, but can be Node as well) that will look for some parameter in the header of the request and deny access if that parameter's value is incorrect or missing (you can call the parameter whatever you like)
2. Create a React app that will have two pages, each with a button and a textbox:
- switching between pages should not reload the browser (i.e. a single-page application)
- the buttons should send a request with and without the required header to the endpoint above
- the textbox is where you can display the response
3. Create another REST API endpoint that will fetch a result from any public API and save the response as a file.

Requirements 1 and 3:<br />
flask-api/flask_backend contains the REST APIs for requirements 1 and 3. It is hosted on localhost:5000.<br />
flask-api/backend_tests contains the unit tests used for testing the APIs in flask_backend.<br />
I decided not to throw errors in check_authorization() because we're looking for a specific parameter and should prohibit access if the parameter is incorrect or missing.<br />
Since I don't know how the API for requirement 3 (saveAPIResponse()) will be called, I threw exceptions when required parameters were missing or invalid.<br />

Requirement 2:<br />
frontend/src contains the components used for the frontend.<br />
App.js only contains the routes which links Page 1 and Page 2.<br />
Page 1 is set up so that the user can get to Page 2, but Page 2 cannot go back to Page 1.<br />
Page 1 sends a request with the required header value, which returns true from check_authorization() and allows navigation to Page 2.<br />
Page 2 does not send the required header, or any header with its request, causing check_authorization() to return false. This updates the state of 'authorization' and displays the message 'You are not authorized'.
