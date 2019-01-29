import React from "react";

const TrackerDescriptionSmall = (props) => {



return(
  <div className="row">
    <div className = "col">{props.props.task_name}</div>



          <div className="col-auto alert alert-success h6 align-self-end"
                key={props.props.id}>{props.props.goal.goal_name}</div>

  </div>
)}


export default TrackerDescriptionSmall;

// <div className="col"></div>
