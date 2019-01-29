import React from "react";
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"

import EditButton from "../buttons/EditButton"
import ConfirmButton from "../buttons/ConfirmButton"
import DiscardButton from "../buttons/DiscardButton"

const ValueDescription = (props) => {



return(
        (!props.props.edit_description
          && ((!props.props.edited_description
              &&
              <div className="row">
                <div className ="col h5">{props.props.value_description}</div>
                <EditButton props={{id: props.props.id,
                                    button_function: props.props.handleEdit,
                                    target: "value_description",}}/>

              </div>)
              ||(!!props.props.edited_description
                &&
                props.props.edited_description !== props.props.value_description
              &&
              <div>
                  <div className="col h5 mt-2">Your provided a new value description:</div>
                  <div className="row col mt-2">
                      <div className ="col alert alert-success">{props.props.edited_description}</div>

                          <EditButton props={{id: props.props.id,
                                              button_function: props.props.handleEdit,
                                              target: "value_description",}}/>

                          <ConfirmButton props={{id: props.props.id,
                                              button_function: props.props.submitChangeFunc,
                                              target: "value_description",}}/>

                          <DiscardButton props={{id: props.props.id,
                                              button_function: props.props.discardChangeFunc,
                                              target: "value_description",}}/>

                  </div>




                      <div className="col h5 mt-2">Original description of this value was:</div>
                  <div className="alert alert-warning">{props.props.value_description}</div>

              </div>))
          )
        ||
          ((
            !!props.props.edited_description
            &&
            <form>
            <div className="form-group">
                <div className="col h5 mt-2">Original description of this value was:</div>
                <div className="col alert alert-warning">{props.props.value_description}</div>


                  <textarea value={props.props.edited_description}
                                      onChange={(event) => {
                                        props.props.handleUpdate({
                                              id : props.props.id,
                                              value_description : props.props.value_description,
                                              value: event.target.value})
                                        }}
                                      autoFocus
                                      onBlur={(event) => {
                                        props.props.handleBlur({
                                              id : props.props.id,
                                              value_description : props.props.value_description})
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
                  <div className="col alert alert-warning">{props.props.value_description}</div>
                    <textarea value={props.props.value_description}
                                        onChange={(event) => {
                                          props.props.handleUpdate({
                                                id : props.props.id,
                                                value_description : props.props.value_description,
                                                value: event.target.value})
                                          }}
                                        autoFocus
                                        onBlur={(event) => {
                                          props.props.handleBlur({
                                                id : props.props.id,
                                                value_description : props.props.value_description})
                                          }}
                                        className="form-control"
                                        rows="3"
                                        id="valueDescriptionCreate"/>
              </div>
            </form>))

)


    }


export default ValueDescription;

//
// switch(true){
//   case this.state.edit && !this.state.edited:
//       return(
//         <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>
//
//           <div className="card-body">
//               <form>
//                 <div className="form-group">
//                     <p className="row">Original name of this value was:</p>
//                     <p><strong className="card-title">{this.props.value_props.value_description}</strong></p>
//                     <label for="valueEditForm">
//
//                       <input type="text" value={this.state.value_name}
//                                           onChange={this.handleChangeValue}
//                                           autoFocus
//                                           onBlur={this.handleBlur}
//                                           className="form-control"
//                                           id="valueEditForm"/>
//                     </label>
//                 </div>
//               </form>
//
//               <div className="row">
//                 <p>{this.state.value_description}</p>
//               </div>
//
//           </div>
//
//           <div className="row bg-dark clearfix align-items-center text-white rounded">
//               <div className="col">
//                 <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
//               </div>
//
//               <div className="col-2 delete-button-in-clearfix">
//                 <button onClick={this.deleteFunc} className="btn btn-danger float-right">
//                   Delete
//                 </button>
//               </div>
//
//           </div>
//             </div>
//       )
//   case !this.state.edit && this.state.edited:
//       return(
//         <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>
//             <div className="card-body">
//                 <div className="row">
//                   <h1 onClick={this.handleClick} className="card-title">{this.state.value_name}</h1>
//                   <p>Original name of this value was: <strong>{this.props.value_props.value_description}</strong></p>
//                 </div>
//
//                 <div className="row">
//                   <div className="col-md-4-auto">
//                       <button onClick={this.submitChangeFunc} className="btn btn-success btn-sm">
//                         Submit Edit
//                       </button>
//                   </div>
//
//                   <div className="col-md-4-auto">
//                       <button onClick={this.discardChangeFunc} className="btn btn-danger btn-sm">
//                         Discard Changes
//                       </button>
//                   </div>
//                 </div>
//
//                 <div className="row">
//                   <p>{this.state.value_description}</p>
//                 </div>
//             </div>
//
//             <div className="row bg-dark clearfix align-items-center text-white rounded">
//                 <div className="col">
//                   <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
//                 </div>
//
//                 <div className="col-2 delete-button-in-clearfix">
//                   <button onClick={this.deleteFunc} className="btn btn-danger float-right">
//                     Delete
//                   </button>
//                 </div>
//             </div>
//
//         </div>
//       )
//   default:
//       return(
//         <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>
//
//           <div className="card-body">
//
//               <div className="row">
//                 <h1 onClick={this.handleClick} className="card-title">{this.state.value_name}</h1>
//               </div>
//
//               <div className="row">
//                 <p>{this.state.value_description}</p>
//               </div>
//
//           </div>
//
//           <div className="row bg-dark clearfix align-items-center text-white rounded">
//               <div className="col">
//                 <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
//               </div>
//
//               <div className="col-2 delete-button-in-clearfix">
//                 <button
//                 // onClick={this.deleteFunc}
//                 onClick={
//                   (event) => {
//                     event.preventDefault();
//                     this.props.handleDeleteValue(this.state)}
//                           }
//                 className="btn btn-danger float-right">
//                   Delete
//                 </button>
//               </div>
//
//           </div>
//
//         </div>
//       )
// }
