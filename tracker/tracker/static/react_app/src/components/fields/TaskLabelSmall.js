import React from "react";

import {Link} from "react-router-dom";

const TaskLabelSmall = (props) => {

// console.log("values/" + props.props.id)

return(
  <div className="row h4 ">

      <Link to={"/tasks/" + props.props.id} className = "col">
      <div>{props.props.task_name}</div>
      </Link>

    {props.children.map(list_child =>
      <div className = "col-auto align-self-start">{list_child}</div>
                        )
    }

  </div>
)}


export default TaskLabelSmall;

// {props.children.map(list_value =>
//   <div className = "col">{list_value}</div>
// )}
