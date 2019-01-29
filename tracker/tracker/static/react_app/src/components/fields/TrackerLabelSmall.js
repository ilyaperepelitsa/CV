import React from "react";

import {Link} from "react-router-dom";

const TrackerLabelSmall = (props) => {

// console.log("values/" + props.props.id)

const diff = Math.abs(new Date(props.props.created_date) - new Date(props.props.updated_date));
const minutes = Math.floor((diff/1000)/60);

return(
  <div className="row h4 ">

    {props.props.counter_enabled ?
      <div className = "col">
        {props.props.counter} {props.props.counter_word}
      </div>:

      void(0)
    }

    {props.props.timer_enabled ?

       <div className = "col">
         {minutes} minutes
       </div>

      :
      void(0)
    }

    <div className = "col-auto align-self-end">{props.children}</div>



  </div>
)}


export default TrackerLabelSmall;

// {props.children.map(list_value =>
//   <div className = "col">{list_value}</div>
// )}
