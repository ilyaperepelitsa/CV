import React from "react";

const Footer = (props) => {

const timeStamp = new Date(props.props.created_date);

return(
  <div className="row bg-dark clearfix text-white rounded-bottom">
                <div className="col align-items-center">
                  {timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}
                </div>

            </div>


    )}


export default Footer;

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
//                     <p><strong className="card-title">{this.props.value_props.value_name}</strong></p>
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
//                   <p>Original name of this value was: <strong>{this.props.value_props.value_name}</strong></p>
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
