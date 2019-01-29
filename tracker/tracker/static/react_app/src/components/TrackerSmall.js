import React from "react";
import TrackerLabelSmall from "./fields/TrackerLabelSmall"
import TrackerDescriptionSmall from "./fields/TrackerDescriptionSmall"
import Footer from "./fields/Footer"

import DeleteButton from "./buttons/DeleteButton"


const TrackerSmall = (props) => {


  const divStyle = {
    maxWidth: "20rem",
    height: "20rem",
    margin: 10
  };
  // console.log(props)

return(
    <div className="list-group-item">


        <TaskLabelSmall props={props.props}>
            <DeleteButton props={{id: props.props.id,
                                  button_function: props.props.handleDeleteTask}}/>
        </TaskLabelSmall>

        <TaskDescriptionSmall props={props.props}/>


    </div>
  )}


export default TrackerSmall;
