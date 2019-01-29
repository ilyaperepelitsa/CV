import {Link, NavLink} from "react-router-dom"
import React from "react";

const Header = () => (

  <div className="bg-light">
    <NavLink
      to="/"
      activeClassName="is_active nav-item h3 mr-3 ml-3"
      className="nav-item h3 mr-3 ml-3"
      exact={true}>

      Home

    </NavLink>

    <NavLink
      to="/values"
      activeClassName="is_active nav-item h3 mr-3 ml-3"
      className="nav-item h3 mr-3 ml-3">


      Values

    </NavLink>

    <NavLink
      to="/goals"
      activeClassName="is_active nav-item h3 mr-3 ml-3"
      className="nav-item h3 mr-3 ml-3">

      Goals

    </NavLink>

    <NavLink
      to="/tasks"
      activeClassName="is_active nav-item h3 mr-3 ml-3"
      className="nav-item h3 mr-3 ml-3">

      Tasks

    </NavLink>

  </div>

)





export default Header
