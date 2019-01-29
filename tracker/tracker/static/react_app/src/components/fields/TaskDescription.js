import React from "react";
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const TaskDescription = (props) => {



return(
        (!props.props.edit_description
          && ((!props.props.edited_description
              &&
              <div className="row">
                <div className ="col h5">{props.props.task_description}</div>
                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "task_description",}}/>

              </div>)
              ||(!!props.props.edited_description
                &&
                props.props.edited_description !== props.props.task_description
              &&
              <div>
                  <div className="col h5 mt-2">Your provided a new task description:</div>
                  <div className="row col mt-2">
                      <div className ="col alert alert-success">{props.props.edited_description}</div>

                          <EditButton props={{id: props.props.id,
                                              button_function: props.props.handleEdit,
                                              target: "task_description",}}/>

                          <ConfirmButton props={{id: props.props.id,
                                              button_function: props.props.submitChangeFunc,
                                              target: "task_description",}}/>

                          <DiscardButton props={{id: props.props.id,
                                              button_function: props.props.discardChangeFunc,
                                              target: "task_description",}}/>

                  </div>




                      <div className="col h5 mt-2">Original description of this task was:</div>
                  <div className="alert alert-warning">{props.props.task_description}</div>

              </div>))
          )
        ||
          ((
            !!props.props.edited_description
            &&
            <form>
            <div className="form-group">
                <div className="col h5 mt-2">Original description of this task was:</div>
                <div className="col alert alert-warning">{props.props.task_description}</div>


                  <textarea value={props.props.edited_description}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              task_description : props.props.task_description,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              task_description : props.props.task_description})
                                        }}
                                      className="form-control"
                                      rows="3"
                                      id="valueDescriptionCreate"/>


            </div>
          </form>)
            ||
            (!props.props.edited_description
              &&
              <form>
              <div className="form-group">
                  <div className="col h5 mt-2">You can edit this task description:</div>
                  <div className="col alert alert-warning">{props.props.task_description}</div>
                    <textarea value={props.props.task_description}
                                        onChange={(event) => {
                                          props.props.handleUpdate({
                                                id : props.props.id,
                                                task_description : props.props.task_description,
                                                value: event.target.value})
                                          }}
                                        autoFocus
                                        onBlur={(event) => {
                                          props.props.handleBlur({
                                                id : props.props.id,
                                                task_description : props.props.task_description})
                                          }}
                                        className="form-control"
                                        rows="3"
                                        id="valueDescriptionCreate"/>
              </div>
            </form>))

)


    }


export default TaskDescription;
