import React from "react";

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const ValueLabel = (props) => {



return(
        (!props.props.edit_value
          && ((!props.props.edited_value
              &&
              <div className="row bg-dark clearfix text-white rounded-top">
                <div className="col card-title h4 text-center m-2">{props.props.value_name}</div>

                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "value_name",}}/>

              </div>)
              ||(!!props.props.edited_value
                &&
                props.props.edited_value !== props.props.value_name
              &&
              <div>
                  <div className="row bg-dark clearfix text-white rounded-top ">
                    <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_value}</div>

                      <EditButton props={{id: props.props.id,
                                          button_function: props.props.handleEdit,
                                          target: "value_name",}}/>

                      <ConfirmButton props={{id: props.props.id,
                                          button_function: props.props.submitChangeFunc,
                                          target: "value_name",}}/>

                      <DiscardButton props={{id: props.props.id,
                                          button_function: props.props.discardChangeFunc,
                                          target: "value_name",}}/>

                  </div>
                    <div className="col h5 mt-2">Original name of this value was:</div>
                    <div className="col alert alert-warning">{props.props.value_name}</div>


              </div>
            ))
          )
        ||
          ((
            !!props.props.edited_value
            &&
            <div>
            <div className="row bg-dark clearfix text-white rounded-top ">
              <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.edited_value}</div>
            </div>
            <form onSubmit ={(event) => {
              event.preventDefault();
              props.props.handleBlur({
                    id : props.props.id,
                    value_name : props.props.value_name})
              }}>

            <div className="form-group">
                <div className="col h5 mt-2">Original name of this value was:</div>
                <div className="col alert alert-warning">{props.props.value_name}</div>

                  <input type="text" value={props.props.edited_value}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              value_name : props.props.value_name,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              value_name : props.props.value_name})
                                        }}
                                      className="form-control"
                                      id="valueEditForm"/>
            </div>

          </form>
          </div>)
            ||
            (!props.props.edited_value
              &&
              <div>
              <div className="row bg-dark clearfix text-white rounded-top ">
                <div className="col card-title h4 text-center m-2 alert alert-success">{props.props.value_name}</div>
              </div>
              <form onSubmit ={(event) => {
                   event.preventDefault();
                   props.props.handleBlur({
                         id : props.props.id,
                         value_name : props.props.value_name})
                   }}>
               <div className="form-group">

                   <div className="col h5 mt-2">You can edit this value name:</div>
                   <div className="col alert alert-warning">{props.props.value_name}</div>

                     <input type="text" value={props.props.value_name}
                                         onChange={(event) => {
                                           props.props.handleUpdate({
                                                 id : props.props.id,
                                                 value_name : props.props.value_name,
                                                 value: event.target.value})
                                           }}

                                         autoFocus
                                         onBlur={(event) => {
                                           props.props.handleBlur({
                                                 id : props.props.id,
                                                 value_name : props.props.value_name})
                                           }}
                                         className="form-control"
                                         id="valueEditForm"/>
               </div>

               </form>
             </div>))

)


    }


export default ValueLabel;
