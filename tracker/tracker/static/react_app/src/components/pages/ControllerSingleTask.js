import React from "react";

import TaskLabel from "../fields/TaskLabel"
import TaskDescription from "../fields/TaskDescription"
import Footer from "../fields/Footer"

import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

//ss
import TrackerSmall from "../TrackerSmall"
import TrackerForm from "../TrackerForm"
//

class ControllerSingleTask extends React.Component{

  state = {
    task: false,
    tracker_form: false,
    form_visible: false,
    trackers: [],
    tracker: false
    //
    // task_name: "Task label",
    // task_description: "Task description",

  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })

  }

  // handleAddTracker = (event) => {
  //   fetch('http://127.0.0.1:8000/api/trackers/add', {
  //     method: 'POST',
  //     body: JSON.stringify({
  //             "task_name": event.task_name,
  //             "task": this.state.task.id}),
  //     headers: {
  //         'content-type': 'application/json'}}).
  //         then(response => response.json()).
  //         then(responseAddedEntry => {
  //
  //           responseAddedEntry.goal = this.state.goal
  //           responseAddedEntry.handleDeleteTask = this.handleDeleteTask;
  //           console.log(responseAddedEntry)
  //           this.state.tasks.unshift(responseAddedEntry)
  //           this.setState({
  //             goal_name: "Goal label",
  //             goal_description: "Goal description",
  //           })
  //
  //
  //         })
  // }

  // handleDeleteTask = (event) => {
  //   // console.log(event.id)
  //   // const csrftoken = Cookies.get('csrftoken')
  //   const newState = this.state;
  //   const index = newState.tasks.findIndex(a => a.id === event.id);
  //   newState.tasks.splice(index, 1);
  //   this.setState(newState);
  //   fetch('http://127.0.0.1:8000/api/tasks/' + event.id, {
  //     method: 'delete',
  //     body: JSON.stringify({"id": event.id}),
  //     headers: {
  //       'content-type': 'application/json'
  //     }
  //   })
  // }
  //
  // handleEdit = (event) => {
  //     if (event.target === "goal_name"){
  //       const old_goal = this.state.goal
  //       old_goal.edit_goal = true
  //       this.setState({
  //           goal: old_goal
  //         })
  //     } else if (event.target === "goal_description"){
  //       const old_goal = this.state.goal
  //       old_goal.edit_description = true
  //       this.setState({
  //           goal: old_goal
  //         })
  //     }
  // }
  //
  // handleBlur = (event) => {
  //   // handle saving here
  //   const newState = this.state;
  //
  //   event.goal_name ?
  //         newState.goal.edit_goal = false
  //         :
  //         newState.goal.edit_description = false;
  //
  //   if (event.goal_name){
  //     newState.goal.edit_goal = false
  //     if (newState.goal.goal_name === newState.goal.edited_goal){
  //       newState.goal.edited_goal = false
  //     }
  //
  //   } else if (event.goal_description){
  //     newState.goal.edit_description = false
  //     if (newState.goal.goal_description === newState.goal.edited_description){
  //       newState.goal.edited_description = false
  //     }
  //
  //   }
  //
  //   this.setState({
  //       goal: newState.goal
  //     })
  // }

  // handleUpdateForm = (event) => {
  //   event.goal_name ?
  //       this.setState({
  //         goal_name: event.goal_name,
  //       })
  //         :
  //       this.setState({
  //         goal_description: event.goal_description,
  //       })
  // }

//   submitChangeFunc = (event) => {
//
//     // console.log(event)
//    fetch('http://127.0.0.1:8000/api/goals/' + event.id + "/", {
//      method: 'put',
//      body: JSON.stringify({
//              "id": event.id,
//              "goal_name": event.target === "goal_name" ? this.state.goal.edited_goal : this.state.goal.goal_name,
//              "goal_description": event.target === "goal_description" ? this.state.goal.edited_description : this.state.goal.goal_description,}),
//      headers: {
//          'content-type': 'application/json'},
//  }).then(response => response.json()).then(responseUpdatedEntry => {
//    const newState = this.state;
//    newState.goal = responseUpdatedEntry;
//    newState.goal.edited_goal = false;
//    newState.goal.edited_description = false;
//    newState.goal.handleEdit = this.handleEdit;
//    newState.goal.handleBlur = this.handleBlur;
//    newState.goal.handleUpdate = this.handleUpdate;
//
//    newState.goal.submitChangeFunc = this.submitChangeFunc;
//    newState.goal.discardChangeFunc = this.discardChangeFunc;
//
//    newState.goal.edit_goal = false;
//    newState.goal.edit_description = false;
//    this.setState(newState);
//  })
//    $("html svg").children("title").remove();
//    $("html svg").children("desc").remove();
// }
//
//  discardChangeFunc = (event) => {
//    const newState = this.state;
//    event.target === "goal_name" ?
//        newState.goal.edited_goal = false
//          :
//        newState.goal.edited_description = false
//
//    this.setState(newState);
//   }



  // handleDeleteTask = (event) => {
  //   const newState = this.state;
  //   const index = newState.tasks.findIndex(a => a.id === event.id);
  //   newState.tasks.splice(index, 1);
  //   this.setState(newState);
  //   fetch('http://127.0.0.1:8000/api/tasks/' + event.id, {
  //     method: 'delete',
  //     body: JSON.stringify({"id": event.id}),
  //     headers: {
  //       'content-type': 'application/json'
  //     }
  //   })
  // }


  componentDidMount() {
        fetch('http://127.0.0.1:8000/api/tasks/' + this.props.match.params.id)
        .then(response => response.json())
        .then(responseData => {
          responseData.edited_task = false;
          responseData.edited_description = false;
          // responseData.handleEdit = this.handleEdit;
          // responseData.handleBlur = this.handleBlur;
          // responseData.handleUpdate = this.handleUpdate;
          // responseData.submitChangeFunc = this.submitChangeFunc;
          // responseData.discardChangeFunc = this.discardChangeFunc;
          responseData.edit_task = false;
          responseData.edit_description = false;


      fetch('http://127.0.0.1:8000/api/tracker/?task='+ this.props.match.params.id, {
        headers: {
        'content-type': 'application/json'}
          })
          .then(responseTrackers => responseTrackers.json())
          .then(responseTrackersData => {
            // responseTrackersData.map((element) => {
            //   element.handleDeleteTask = this.handleDeleteTask;
            //   return element
            // });

            // console.log(responseGoalsData)
            this.setState({
              task: responseData,
            });

            this.setState({
              trackers: responseTrackersData,
            });
            responseTrackersData.length > 0 ?
            this.setState({
              tracker_form: responseTrackersData[0]
            })
            :
            this.setState({
              tracker_form: {
                "task": this.state.task.id,
                "counter_enabled": false,
                "counter_word": "units, plural",
                "counter": 0,
                "notes": "comment"
              }
            })
          })
          .catch(error => {
            console.log('Fetching and parsing data error', error);
          })
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
        <TaskLabel props = {this.state.task}/>
        <Footer props = {this.state.task}/>
        </div>

        <div className="row mb-2 mt-2">
          <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
            Want to add new tasks?
          </div>
          <div className = "float-left col">
            <AddButton props={{button_function: this.handleEnableForm}}/>
          </div>
        </div>





        <div className="list-group mt-4">
        {this.state.trackers.map(list_tracker =>
          /**/
            <TrackerSmall props = {list_tracker} key ={list_tracker.id}/>



        )}
        </div>

      </div>
  )}}

export default ControllerSingleTask

/*<Modal isOpen={this.state.form_visible}
        onRequestClose={this.handleEnableForm}
        closeTimeoutMS={100}
        ariaHideApp={false}
        className="modal"
        >
    <TrackerForm props={{"task_name": this.state.task_name,
                        "task_description": this.state.task_description,
                        "handleUpdateForm": this.handleUpdateForm,
                        "handleAddTask": this.handleAddTask}}>
          <CloseButton props={{button_function: this.handleEnableForm}}/>
    </TrackerForm>
</Modal>*/
