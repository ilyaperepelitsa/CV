import React from "react";
import TaskSmall from "../TaskSmall"
import TaskForm from "../TaskForm"
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

import Cookies from "js-cookie"

class ControllerTasks extends React.Component{

  state = {
    tasks: [],
    form_visible: false,
    task_name: "Task label",
    task_description: "Task description",
  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })

  }

  handleUpdateForm = (event) => {
    event.task_name ?
        this.setState({
          task_name: event.task_name,
        })
          :
        this.setState({
          task_description: event.task_description,
        })
  }

  handleAddTask = (event) => {
    fetch('http://127.0.0.1:8000/api/tasks/add/', {
      method: 'POST',
      body: JSON.stringify({"task_name": event.task_name,
              "task_description": event.task_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {
            responseAddedEntry.handleDeleteTask = this.handleDeleteTask
            this.state.tasks.unshift(responseAddedEntry)
            this.setState({
              task_name : "Task label",
              task_description : "Task description",
            })
          })
  }


  handleDeleteTask = (event) => {
    // console.log(event.id)
    // const csrftoken = Cookies.get('csrftoken')
    const newState = this.state;
    const index = newState.tasks.findIndex(a => a.id === event.id);
    newState.tasks.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/tasks/' + event.id, {
      method: 'delete',
      headers: {
        'content-type': 'application/json'
      }
    })
  }



  componentDidMount() {

    // console.log(Cookies.get('csrftoken'))

        fetch('http://127.0.0.1:8000/api/tasks/')
        .then(response => response.json())
        .then(responseData => {

      responseData.map((element) => {
        element.handleDeleteTask = this.handleDeleteTask;
        return element
      });
      console.log(responseData);
      this.setState({
        tasks: responseData
      });
        })
        .catch(error => {
          console.log('Fetching and parsing data error', error);
        });
        $("html svg").children("title").remove();
        $("html svg").children("desc").remove();

      }
  componentDidlUpdate(){
    $("html svg").children("title").remove();
    $("html svg").children("desc").remove();
  }



  render(){
    console.log(this.state.tasks)
    return(
      <div>
        <div className="jumbotron pt-4">


          <div className="list-group">
          {this.state.tasks.map(list_goal =>
            <TaskSmall props = {list_goal} key ={list_goal.id}/>)}
          </div>

        </div>


      </div>

  )}

  }

//

// 
// <div className="row mb-2">
//   <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
//     Want to add new tasks?
//   </div>
//   <div className = "float-left col">
//     <AddButton props={{button_function: this.handleEnableForm}}/>
//   </div>
// </div>
//
// <Modal isOpen={this.state.form_visible}
//         onRequestClose={this.handleEnableForm}
//         closeTimeoutMS={100}
//         ariaHideApp={false}
//         className="modal"
//         >
//     <TaskForm props={{"task_name": this.state.task_name,
//                         "task_description": this.state.task_description,
//                         "handleUpdateForm": this.handleUpdateForm,
//                         "handleAddTask": this.handleAddTask}}>
//           <CloseButton props={{button_function: this.handleEnableForm}}/>
//     </TaskForm>
// </Modal>
//

// body: JSON.stringify({"id": event.id}),

export default ControllerTasks
