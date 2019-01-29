import React from "react";
import ValueLabelSmall from "./fields/ValueLabelSmall"
import ValueDescriptionSmall from "./fields/ValueDescriptionSmall"
import Footer from "./fields/Footer"

import DeleteButton from "./buttons/DeleteButton"


const ValueSmall = (props) => {


  const divStyle = {
    maxWidth: "20rem",
    height: "20rem",
    margin: 10
  };
  // console.log(props)

return(
    <div className="list-group-item">

        
        <ValueLabelSmall props={props.props}>
            <DeleteButton props={{id: props.props.id,
                                  button_function: props.props.handleDeleteValue}}/>
        </ValueLabelSmall>

        <ValueDescriptionSmall props={props.props}/>

    </div>
  )}


export default ValueSmall;
