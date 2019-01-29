import React from "react";

const GoalBubble = (props) => {



return(
    <div>
          <div className="col-auto alert alert-success h6 align-self-end"
                key={props.props.id}>{props.props.goal.goal_name}</div>
    </div>
)}


export default GoalBubble;

// <div className="col"></div>
