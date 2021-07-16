
import {compose} from "redux";
import React from "react";
import PropTypes from "prop-types";
import { Route, Switch } from "react-router";
import { withRouter } from "react-router-dom";
import "./styles.module.scss";

import Main from "../Main";

const App = props => [
  <Routes key={1} />,
  ];

  const Routes = props => (
    <Switch>
	      <Route exact path="/" component={Main}/>
		    </Switch>
			);

			App.propTypes = {

			};


export default withRouter((App))
