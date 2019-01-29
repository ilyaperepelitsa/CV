import React from "react";

import GoalLabel from "../fields/GoalLabel"
import GoalDescription from "../fields/GoalDescription"
import Footer from "../fields/Footer"

import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

import TaskSmall from "../TaskSmall"


import TaskForm from "../TaskForm"


class ControllerSingleGoal extends React.Component{

  state = {
    goal: false,
    form_visible: false,
    tasks: [],
    task_name: "Task label",
    task_description: "Task description",

  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })

  }

  handleAddTask = (event) => {
    fetch('http://127.0.0.1:8000/api/tasks/add', {
      method: 'POST',
      body: JSON.stringify({"task_name": event.task_name,
              "goal": this.state.goal.id}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {

            responseAddedEntry.goal = this.state.goal
            responseAddedEntry.handleDeleteTask = this.handleDeleteTask;
            console.log(responseAddedEntry)
            this.state.tasks.unshift(responseAddedEntry)
            this.setState({
              goal_name: "Goal label",
              goal_description: "Goal description",
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
      body: JSON.stringify({"id": event.id}),
      headers: {
        'content-type': 'application/json'
      }
    })
  }

  handleEdit = (event) => {
      if (event.target === "goal_name"){
        const old_goal = this.state.goal
        old_goal.edit_goal = true
        this.setState({
            goal: old_goal
          })
      } else if (event.target === "goal_description"){
        const old_goal = this.state.goal
        old_goal.edit_description = true
        this.setState({
            goal: old_goal
          })
      }
  }

  handleBlur = (event) => {
    // handle saving here
    const newState = this.state;

    event.goal_name ?
          newState.goal.edit_goal = false
          :
          newState.goal.edit_description = false;

    if (event.goal_name){
      newState.goal.edit_goal = false
      if (newState.goal.goal_name === newState.goal.edited_goal){
        newState.goal.edited_goal = false
      }

    } else if (event.goal_description){
      newState.goal.edit_description = false
      if (newState.goal.goal_description === newState.goal.edited_description){
        newState.goal.edited_description = false
      }

    }

    this.setState({
        goal: newState.goal
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

  submitChangeFunc = (event) => {

    // console.log(event)
   fetch('http://127.0.0.1:8000/api/goals/' + event.id + "/", {
     method: 'put',
     body: JSON.stringify({
             "id": event.id,
             "goal_name": event.target === "goal_name" ? this.state.goal.edited_goal : this.state.goal.goal_name,
             "goal_description": event.target === "goal_description" ? this.state.goal.edited_description : this.state.goal.goal_description,}),
     headers: {
         'content-type': 'application/json'},
 }).then(response => response.json()).then(responseUpdatedEntry => {
   const newState = this.state;
   newState.goal = responseUpdatedEntry;
   newState.goal.edited_goal = false;
   newState.goal.edited_description = false;
   newState.goal.handleEdit = this.handleEdit;
   newState.goal.handleBlur = this.handleBlur;
   newState.goal.handleUpdate = this.handleUpdate;

   newState.goal.submitChangeFunc = this.submitChangeFunc;
   newState.goal.discardChangeFunc = this.discardChangeFunc;

   newState.goal.edit_goal = false;
   newState.goal.edit_description = false;
   this.setState(newState);
 })
   $("html svg").children("title").remove();
   $("html svg").children("desc").remove();
}

 discardChangeFunc = (event) => {
   const newState = this.state;
   event.target === "goal_name" ?
       newState.goal.edited_goal = false
         :
       newState.goal.edited_description = false

   this.setState(newState);
  }



  handleDeleteTask = (event) => {
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
      // body: JSON.stringify({"id": event.id}),

  componentDidMount() {
        fetch('http://127.0.0.1:8000/api/goals/' + this.props.match.params.id)
        .then(response => response.json())
        .then(responseData => {
          responseData.edited_goal = false;
          responseData.edited_description = false;
          responseData.handleEdit = this.handleEdit;
          responseData.handleBlur = this.handleBlur;
          responseData.handleUpdate = this.handleUpdate;

          responseData.submitChangeFunc = this.submitChangeFunc;
          responseData.discardChangeFunc = this.discardChangeFunc;

          responseData.edit_goal = false;
          responseData.edit_description = false;






      fetch('http://127.0.0.1:8000/api/tasks/?goal='+ this.props.match.params.id, {
        headers: {
        'content-type': 'application/json'}
          })
          .then(responseGoals => responseGoals.json())
          .then(responseGoalsData => {
            // const newState = this.state;
            responseGoalsData.map((element) => {
              element.handleDeleteTask = this.handleDeleteTask;
              return element
            });

            // console.log(responseGoalsData)
            this.setState({
              tasks: responseGoalsData,
            });
          })
          .catch(error => {
            console.log('Fetching and parsing data error', error);
          })
          // console.log(responseData)
          this.setState({
            goal: responseData,
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
    // console.log(this.props.match.params.id);
    // console.log(this.state)
    return(
      <div className="jumbotron pt-4">

        <div className="card col-7">
        <GoalLabel props = {this.state.goal}/>
        <GoalDescription props = {this.state.goal}/>
        <Footer props = {this.state.goal}/>
        </div>

        <div className="row mb-2 mt-2">
          <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
            Want to add new tasks?
          </div>
          <div className = "float-left col">
            <AddButton props={{button_function: this.handleEnableForm}}/>
          </div>
        </div>



        <Modal isOpen={this.state.form_visible}
                onRequestClose={this.handleEnableForm}
                closeTimeoutMS={100}
                ariaHideApp={false}
                className="modal"
                >
            <TaskForm props={{"task_name": this.state.task_name,
                                "task_description": this.state.task_description,
                                "handleUpdateForm": this.handleUpdateForm,
                                "handleAddTask": this.handleAddTask}}>
                  <CloseButton props={{button_function: this.handleEnableForm}}/>
            </TaskForm>
        </Modal>

        <div className="list-group mt-4">
        {this.state.tasks.map(list_task =>
          /**/
            list_task.goal.id === this.state.goal.id ?
            <TaskSmall props = {list_task} key ={list_task.id}/>
            :
            void(0)



        )}
        </div>

      </div>






  )}

  }




//

export default ControllerSingleGoal
  // <div class="row">
  //       {this.state.values.map(list_value =>
  //         <Value value_props = {list_value}
  //                 handleDeleteValue={this.handleDeleteValue}
  //                 key ={list_value.id}/>)}
  // </div>
