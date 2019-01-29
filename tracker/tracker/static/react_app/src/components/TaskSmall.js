import React from "react";
import TaskLabelSmall from "./fields/TaskLabelSmall"
// import TaskDescriptionSmall from "./fields/TaskDescriptionSmall"
import GoalBubble from "./fields/GoalBubble"
import Footer from "./fields/Footer"

import DeleteButton from "./buttons/DeleteButton"


const TaskSmall = (props) => {


  const divStyle = {
    maxWidth: "20rem",
    height: "20rem",
    margin: 10
  };
  // console.log(props)

return(
    <div className="list-group-item">


          <TaskLabelSmall props={props.props}>
              <GoalBubble props={props.props}/>

              <DeleteButton props={{id: props.props.id,
                                    button_function: props.props.handleDeleteTask}}/>
          </TaskLabelSmall>



    </div>
  )}


export default TaskSmall;
