import React from "react";
import GoalLabelSmall from "./fields/GoalLabelSmall"
import GoalDescriptionSmall from "./fields/GoalDescriptionSmall"
import Footer from "./fields/Footer"

import DeleteButton from "./buttons/DeleteButton"


const GoalSmall = (props) => {


  const divStyle = {
    maxWidth: "20rem",
    height: "20rem",
    margin: 10
  };
  // console.log(props)

return(
    <div className="list-group-item">


        <GoalLabelSmall props={props.props}>
            <DeleteButton props={{id: props.props.id,
                                  button_function: props.props.handleDeleteGoal}}/>
        </GoalLabelSmall>

        <GoalDescriptionSmall props={props.props}/>


    </div>
  )}


export default GoalSmall;
