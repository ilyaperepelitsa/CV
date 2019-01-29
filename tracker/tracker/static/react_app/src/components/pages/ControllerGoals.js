import React from "react";
import GoalSmall from "../GoalSmall"
import GoalForm from "../GoalForm"
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

import Cookies from "js-cookie"

class ControllerGoals extends React.Component{

  state = {
    goals: [],
    form_visible: false,
    goal_name: "Goal label",
    goal_description: "Goal description",
  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })

  }

  handleUpdateForm = (event) => {
    event.goal_name ?
        this.setState({
          goal_name: event.goal_name,
        })
          :
        this.setState({
          goal_description: event.goal_description,
        })
  }

  handleAddGoal = (event) => {
    fetch('http://127.0.0.1:8000/api/goals/add/', {
      method: 'POST',
      body: JSON.stringify({"goal_name": event.goal_name,
              "goal_description": event.goal_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {
            responseAddedEntry.handleDeleteGoal = this.handleDeleteGoal
            this.state.goals.unshift(responseAddedEntry)
            this.setState({
              goal_name : "Value label",
              goal_description : "Value description",
            })
          })
  }


  handleDeleteGoal = (event) => {
    // console.log(event.id)
    // const csrftoken = Cookies.get('csrftoken')
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);
    newState.goals.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/goals/' + event.id, {
      method: 'delete',
      headers: {
        'content-type': 'application/json'
      }
    })
  }



  componentDidMount() {

    // console.log(Cookies.get('csrftoken'))

        fetch('http://127.0.0.1:8000/api/goals/')
        .then(response => response.json())
        .then(responseData => {

      responseData.map((element) => {
        element.handleDeleteGoal = this.handleDeleteGoal;
        return element
      });

      this.setState({
        goals: responseData
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
    console.log(this.state.goals)
    return(
      <div>
        <div className="jumbotron pt-4">



          <div className="list-group">
          {this.state.goals.map(list_value =>
            <GoalSmall props = {list_value} key ={list_value.id}/>)}
          </div>

        </div>


      </div>

  )}

  }
//
// <div className="row mb-2">
//   <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
//     Want to add new goals?
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
//     <GoalForm props={{"goal_name": this.state.goal_name,
//                         "goal_description": this.state.goal_description,
//                         "handleUpdateForm": this.handleUpdateForm,
//                         "handleAddGoal": this.handleAddGoal}}>
//           <CloseButton props={{button_function: this.handleEnableForm}}/>
//     </GoalForm>
// </Modal>
//

//

export default ControllerGoals
