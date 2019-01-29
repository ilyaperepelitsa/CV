import React from "react";

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const GoalLabel = (props) => {



return(
        (!props.props.edit_goal
          && ((!props.props.edited_goal
              &&
              <div className="row bg-dark clearfix text-white rounded-top">
                <div className="col card-title h4 text-center m-2">{props.props.goal_name}</div>

                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "goal_name",}}/>

              </div>)
              ||(!!props.props.edited_goal
                &&
                props.props.edited_goal !== props.props.goal_name
              &&
              <div>
                  <div className="row bg-dark clearfix text-white rounded-top ">
                    <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_goal}</div>

                      <EditButton props={{id: props.props.id,
                                          button_function: props.props.handleEdit,
                                          target: "goal_name",}}/>

                      <ConfirmButton props={{id: props.props.id,
                                          button_function: props.props.submitChangeFunc,
                                          target: "goal_name",}}/>

                      <DiscardButton props={{id: props.props.id,
                                          button_function: props.props.discardChangeFunc,
                                          target: "goal_name",}}/>

                  </div>
                    <div className="col h5 mt-2">Original name of this goal was:</div>
                    <div className="col alert alert-warning">{props.props.goal_name}</div>


              </div>
            ))
          )
        ||
          ((
            !!props.props.edited_goal
            &&
            <div>
            <div className="row bg-dark clearfix text-white rounded-top ">
              <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_goal}</div>
            </div>
            <form onSubmit ={(event) => {
              event.preventDefault();
              props.props.handleBlur({
                    id : props.props.id,
                    goal_name : props.props.goal_name})
              }}>

            <div className="form-group">
                <div className="col h5 mt-2">Original name of this goal was:</div>
                <div className="col alert alert-warning">{props.props.goal_name}</div>

                  <input type="text" value={props.props.edited_goal}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              goal_name : props.props.goal_name,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              goal_name : props.props.goal_name})
                                        }}
                                      className="form-control"
                                      id="valueEditForm"/>
            </div>

          </form>
          </div>)
            ||
            (!props.props.edited_goal
              &&
              <div>
              <div className="row bg-dark clearfix text-white rounded-top ">
                <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.goal_name}</div>
              </div>
              <form onSubmit ={(event) => {
                   event.preventDefault();
                   props.props.handleBlur({
                         id : props.props.id,
                         goal_name : props.props.goal_name})
                   }}>
               <div className="form-group">

                   <div className="col h5 mt-2">You can edit this goal name:</div>
                   <div className="col alert alert-warning">{props.props.goal_name}</div>

                     <input type="text" value={props.props.goal_name}
                                         onChange={(event) => {
                                           props.props.handleUpdate({
                                                 id : props.props.id,
                                                 goal_name : props.props.goal_name,
                                                 value: event.target.value})
                                           }}

                                         autoFocus
                                         onBlur={(event) => {
                                           props.props.handleBlur({
                                                 id : props.props.id,
                                                 goal_name : props.props.goal_name})
                                           }}
                                         className="form-control"
                                         id="valueEditForm"/>
               </div>

               </form>
             </div>))

)


    }


export default GoalLabel;
