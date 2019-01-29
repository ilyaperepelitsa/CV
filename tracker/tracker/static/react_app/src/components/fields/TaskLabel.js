import React from "react";

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const TaskLabel = (props) => {



return(
        (!props.props.edit_task
          && ((!props.props.edited_task
              &&
              <div className="row bg-dark clearfix text-white rounded-top">
                <div className="col card-title h4 text-center m-2">{props.props.task_name}</div>

                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "task_name",}}/>

              </div>)
              ||(!!props.props.edited_task
                &&
                props.props.edited_task !== props.props.task_name
              &&
              <div>
                  <div className="row bg-dark clearfix text-white rounded-top ">
                    <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_task}</div>

                      <EditButton props={{id: props.props.id,
                                          button_function: props.props.handleEdit,
                                          target: "task_name",}}/>

                      <ConfirmButton props={{id: props.props.id,
                                          button_function: props.props.submitChangeFunc,
                                          target: "task_name",}}/>

                      <DiscardButton props={{id: props.props.id,
                                          button_function: props.props.discardChangeFunc,
                                          target: "task_name",}}/>

                  </div>
                    <div className="col h5 mt-2">Original name of this task was:</div>
                    <div className="col alert alert-warning">{props.props.task_name}</div>


              </div>
            ))
          )
        ||
          ((
            !!props.props.edited_task
            &&
            <div>
            <div className="row bg-dark clearfix text-white rounded-top ">
              <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_task}</div>
            </div>
            <form onSubmit ={(event) => {
              event.preventDefault();
              props.props.handleBlur({
                    id : props.props.id,
                    task_name : props.props.task_name})
              }}>

            <div className="form-group">
                <div className="col h5 mt-2">Original name of this task was:</div>
                <div className="col alert alert-warning">{props.props.task_name}</div>

                  <input type="text" value={props.props.edited_task}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              task_name : props.props.task_name,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              task_name : props.props.task_name})
                                        }}
                                      className="form-control"
                                      id="valueEditForm"/>
            </div>

          </form>
          </div>)
            ||
            (!props.props.edited_task
              &&
              <div>
              <div className="row bg-dark clearfix text-white rounded-top ">
                <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.task_name}</div>
              </div>
              <form onSubmit ={(event) => {
                   event.preventDefault();
                   props.props.handleBlur({
                         id : props.props.id,
                         task_name : props.props.task_name})
                   }}>
               <div className="form-group">

                   <div className="col h5 mt-2">You can edit this task name:</div>
                   <div className="col alert alert-warning">{props.props.task_name}</div>

                     <input type="text" value={props.props.task_name}
                                         onChange={(event) => {
                                           props.props.handleUpdate({
                                                 id : props.props.id,
                                                 task_name : props.props.task_name,
                                                 value: event.target.value})
                                           }}

                                         autoFocus
                                         onBlur={(event) => {
                                           props.props.handleBlur({
                                                 id : props.props.id,
                                                 task_name : props.props.task_name})
                                           }}
                                         className="form-control"
                                         id="valueEditForm"/>
               </div>

               </form>
             </div>))

)


    }


export default TaskLabel;
