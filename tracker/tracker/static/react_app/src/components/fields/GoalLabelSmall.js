import React from "react";

import {Link} from "react-router-dom";

const GoalLabelSmall = (props) => {

// console.log("values/" + props.props.id)

return(
  <div className="row h4 ">

      <Link to={"/goals/" + props.props.id} className = "col">
      <div>{props.props.goal_name}</div>
      </Link>

    <div className = "col-auto align-self-end">{props.children}</div>



  </div>
)}


export default GoalLabelSmall;

// {props.children.map(list_value =>
//   <div className = "col">{list_value}</div>
// )}
