import React from "react";

const TaskDescriptionSmall = (props) => {



return(
  <div className="row">
    <div className = "col"></div>
          <div className="col-auto alert alert-success h6 align-self-end"
                key={props.props.id}>{props.props.goal.goal_name}</div>
  </div>
)}


export default TaskDescriptionSmall;

// <div className="col"></div>
