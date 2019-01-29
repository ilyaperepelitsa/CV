import React from "react";
import {BrowserRouter, Route, Switch} from "react-router-dom"

import ControllerHome from "./ControllerHome"

import ControllerValues from "./ControllerValues"
import ControllerSingleValue from "./ControllerSingleValue"

import ControllerGoals from "./ControllerGoals"
import ControllerSingleGoal from "./ControllerSingleGoal"

import ControllerTasks from "./ControllerTasks"
import ControllerSingleTask from "./ControllerSingleTask"

import Header from "./Header"



const RouterUrls = () => (

<BrowserRouter>
  <div>
    <Header/>
    <Switch>
      <Route path="/" component={ControllerHome} exact={true}/>
      <Route path="/values/" component={ControllerValues} exact={true}/>
      <Route path="/values/:id" component={ControllerSingleValue}/>
      <Route path="/goals/" component={ControllerGoals} exact={true}/>
      <Route path="/goals/:id" component={ControllerSingleGoal} exact={true}/>
      <Route path="/tasks/" component={ControllerTasks} exact={true}/>
      <Route path="/tasks/:id" component={ControllerSingleTask} exact={true}/>
    </Switch>
  </div>
</BrowserRouter>

)


export default RouterUrls
