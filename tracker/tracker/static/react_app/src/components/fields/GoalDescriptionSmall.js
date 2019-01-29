import React from "react";

const GoalDescriptionSmall = (props) => {



return(
  <div className="row">
    <div className = "col">{props.props.goal_description}</div>


      {props.props.values.map(value =>
          <div className="col-auto alert alert-success h6 align-self-end"
                key={value.id}>{value.value_name}</div>
        )}
  </div>
)}


export default GoalDescriptionSmall;

// <div className="col"></div>
