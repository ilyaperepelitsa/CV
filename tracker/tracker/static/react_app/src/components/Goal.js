import React from "react";
import ValueLabel from "./fields/ValueLabel"
import ValueDescription from "./fields/ValueDescription"
import Footer from "./fields/Footer"

const Value = (props) => {


  // deleteFunc(event) {
  //     this.props.deleteValue(this.props.value_props.id);
  //     fetch('http://127.0.0.1:8000/api/' + this.props.value_props.id, {
  //       method: 'delete'})
  //  }
  // console.log(props)



  const divStyle = {
    maxWidth: "20rem",
    height: "20rem",
    margin: 10
  };
  // console.log(props)

return(
    <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>


        <ValueLabel props={props.props}/>

        <div className="card-body">
          <ValueDescription props={props.props}/>
        </div>
        <Footer props={props.props}/>
    </div>
)


    }


export default Value;

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
