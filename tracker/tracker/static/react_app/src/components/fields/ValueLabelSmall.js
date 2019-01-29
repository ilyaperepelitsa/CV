import React from "react";

import {Link} from "react-router-dom";

const ValueLabelSmall = (props) => {

// console.log("values/" + props.props.id)

return(
  <div className="row h4">

      <Link to={"/values/" + props.props.id} className = "col">
      <div>{props.props.value_name}</div>
      </Link>



    <div className = "col-auto align-self-end">{props.children}</div>



  </div>
)}


export default ValueLabelSmall;

// {props.children.map(list_value =>
//   <div className = "col">{list_value}</div>
// )}
