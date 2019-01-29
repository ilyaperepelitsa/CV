import React from "react";

import ValueLabel from "../fields//ValueLabel"
import ValueDescription from "../fields//ValueDescription"
import Footer from "../fields//Footer"

import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

import GoalSmall from "../GoalSmall"


import GoalForm from "../GoalForm"


class ControllerSingleValue extends React.Component{

  state = {
    value: false,
    form_visible: false,
    goals: [],
    goal_name: "Goal label",
    goal_description: "Goal description",

  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })


  }

  handleAddValue = (event) => {
    fetch('http://127.0.0.1:8000/api/goals/add', {
      method: 'POST',
      body: JSON.stringify({"goal_name": event.goal_name,
              "values": [this.state.value.id],
              "goal_description": event.goal_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {

            responseAddedEntry.values = [this.state.value]
            this.state.goals.unshift(responseAddedEntry)
            this.setState({
              goal_name: "Goal label",
              goal_description: "Goal description",
            })


          })
  }

  handleDeleteValue = (event) => {
    // console.log(event.id)
    // const csrftoken = Cookies.get('csrftoken')
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);
    newState.goals.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/goals/' + event.id, {
      method: 'delete',
      body: JSON.stringify({"id": event.id}),
      headers: {
        'content-type': 'application/json'
      }
    })

  }

  handleEdit = (event) => {
      if (event.target === "value_name"){
        const old_value = this.state.value
        old_value.edit_value = true
        this.setState({
            value: old_value
          })
      } else if (event.target === "value_description"){
        const old_value = this.state.value
        old_value.edit_description = true
        this.setState({
            value: old_value
          })
      }
  }

  handleBlur = (event) => {
    // handle saving here
    const newState = this.state;

    event.value_name ?
          newState.value.edit_value = false
          :
          newState.value.edit_description = false;

    if (event.value_name){
      newState.value.edit_value = false
      if (newState.value.value_name === newState.value.edited_value){
        newState.value.edited_value = false
      }

    } else if (event.value_description){
      newState.value.edit_description = false
      if (newState.value.value_descriptio === newState.value.edited_description){
        newState.value.edited_description = false
      }

    }

    this.setState({
        value: newState.value
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

  submitChangeFunc = (event) => {

    // console.log(event)
   fetch('http://127.0.0.1:8000/api/values/' + event.id + "/", {
     method: 'put',
     body: JSON.stringify({
             "id": event.id,
             "value_name": event.target === "value_name" ? this.state.value.edited_value : this.state.value.value_name,
             "value_description": event.target === "value_description" ? this.state.value.edited_description : this.state.value.value_description,}),
     headers: {
         'content-type': 'application/json'},
 }).then(response => response.json()).then(responseUpdatedEntry => {
   const newState = this.state;
   newState.value = responseUpdatedEntry;
   newState.value.edited_value = false;
   newState.value.edited_description = false;
   newState.value.handleEdit = this.handleEdit;
   newState.value.handleBlur = this.handleBlur;
   newState.value.handleUpdate = this.handleUpdate;

   newState.value.submitChangeFunc = this.submitChangeFunc;
   newState.value.discardChangeFunc = this.discardChangeFunc;

   newState.value.edit_value = false;
   newState.value.edit_description = false;
   this.setState(newState);
 })
   $("html svg").children("title").remove();
   $("html svg").children("desc").remove();
}

 discardChangeFunc = (event) => {
   const newState = this.state;
   event.target === "value_name" ?
       newState.value.edited_value = false
         :
       newState.value.edited_description = false

   this.setState(newState);
  }



  handleDeleteGoal = (event) => {
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);
    newState.goals.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/goals/' + event.id, {
      method: 'delete',
      body: JSON.stringify({"id": event.id}),
      headers: {
        'content-type': 'application/json'
      }
    })
  }


  componentDidMount() {
        fetch('http://127.0.0.1:8000/api/values/' + this.props.match.params.id)
        .then(response => response.json())
        .then(responseData => {
          responseData.edited_value = false;
          responseData.edited_description = false;
          responseData.handleEdit = this.handleEdit;
          responseData.handleBlur = this.handleBlur;
          responseData.handleUpdate = this.handleUpdate;

          responseData.submitChangeFunc = this.submitChangeFunc;
          responseData.discardChangeFunc = this.discardChangeFunc;

          responseData.edit_value = false;
          responseData.edit_description = false;





      fetch('http://127.0.0.1:8000/api/goals/?value=' + this.props.match.params.id, {
        headers: {
        'content-type': 'application/json'}
          })
          .then(responseGoals => responseGoals.json())
          .then(responseGoalsData => {
            // const newState = this.state;
            responseGoalsData.map((element) => {
              element.handleDeleteGoal = this.handleDeleteGoal;
              return element
            });

            // console.log(responseGoalsData)
            this.setState({
              goals: responseGoalsData,
            });
          })
          .catch(error => {
            console.log('Fetching and parsing data error', error);
          })
          // console.log(responseData)
          this.setState({
            value: responseData,
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
    // console.log(this.state.value)
    return(
      <div className="jumbotron pt-4">

        <div className="card col-7">
        <ValueLabel props = {this.state.value}/>
        <ValueDescription props = {this.state.value}/>
        <Footer props = {this.state.value}/>
        </div>

        <div className="row mb-2 mt-2">
          <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
            Want to add new goals?
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
            <GoalForm props={{"goal_name": this.state.goal_name,
                                "goal_description": this.state.goal_description,
                                "handleUpdateForm": this.handleUpdateForm,
                                "handleAddValue": this.handleAddValue}}>
                  <CloseButton props={{button_function: this.handleEnableForm}}/>
            </GoalForm>
        </Modal>

        <div className="list-group mt-4">
        {this.state.goals.map(list_goal =>
          /**/
          list_goal.values.map(value =>
            value.id === this.state.value.id ?
            <GoalSmall props = {list_goal} key ={list_goal.id}/>
            :
            void(0)
          )


        )}
        </div>

      </div>






  )}

  }




//

export default ControllerSingleValue
  // <div class="row">
  //       {this.state.values.map(list_value =>
  //         <Value value_props = {list_value}
  //                 handleDeleteValue={this.handleDeleteValue}
  //                 key ={list_value.id}/>)}
  // </div>
