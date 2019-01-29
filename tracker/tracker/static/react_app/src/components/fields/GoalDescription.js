import React from "react";
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const GoalDescription = (props) => {



return(
        (!props.props.edit_description
          && ((!props.props.edited_description
              &&
              <div className="row">
                <div className ="col h5">{props.props.goal_description}</div>
                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "goal_description",}}/>

              </div>)
              ||(!!props.props.edited_description
                &&
                props.props.edited_description !== props.props.goal_description
              &&
              <div>
                  <div className="col h5 mt-2">Your provided a new value description:</div>
                  <div className="row col mt-2">
                      <div className ="col alert alert-success">{props.props.edited_description}</div>

                          <EditButton props={{id: props.props.id,
                                              button_function: props.props.handleEdit,
                                              target: "goal_description",}}/>

                          <ConfirmButton props={{id: props.props.id,
                                              button_function: props.props.submitChangeFunc,
                                              target: "goal_description",}}/>

                          <DiscardButton props={{id: props.props.id,
                                              button_function: props.props.discardChangeFunc,
                                              target: "goal_description",}}/>

                  </div>




                      <div className="col h5 mt-2">Original description of this value was:</div>
                  <div className="alert alert-warning">{props.props.goal_description}</div>

              </div>))
          )
        ||
          ((
            !!props.props.edited_description
            &&
            <form>
            <div className="form-group">
                <div className="col h5 mt-2">Original description of this value was:</div>
                <div className="col alert alert-warning">{props.props.goal_description}</div>


                  <textarea value={props.props.edited_description}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              goal_description : props.props.goal_description,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              goal_description : props.props.goal_description})
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
                  <div className="col h5 mt-2">You can edit this value description:</div>
                  <div className="col alert alert-warning">{props.props.goal_description}</div>
                    <textarea value={props.props.goal_description}
                                        onChange={(event) => {
                                          props.props.handleUpdate({
                                                id : props.props.id,
                                                goal_description : props.props.goal_description,
                                                value: event.target.value})
                                          }}
                                        autoFocus
                                        onBlur={(event) => {
                                          props.props.handleBlur({
                                                id : props.props.id,
                                                goal_description : props.props.goal_description})
                                          }}
                                        className="form-control"
                                        rows="3"
                                        id="valueDescriptionCreate"/>
              </div>
            </form>))

)


    }


export default GoalDescription;
