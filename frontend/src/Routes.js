import React from "react";
import { Router, Switch, Route } from "react-router-dom";
import history from './history.js'
import Page1 from "./Page1";
import Page2 from './Page2';


function Routes() {
    return (
        <Router history={history}>
            <Switch>
                <Route path="/" exact component={Page1} />
                <Route path="/Page2" exact component={Page2} />
            </Switch>
        </Router>
    )
}

export default Routes;
