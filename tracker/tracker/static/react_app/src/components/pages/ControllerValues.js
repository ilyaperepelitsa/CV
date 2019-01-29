import React from "react";
import ValueSmall from "../ValueSmall"
import ValueForm from "../ValueForm"
import AddButton from "../buttons/AddButton"
import CloseButton from "../buttons/CloseButton"
import Modal from "react-modal"
import $ from "jquery";

import Cookies from "js-cookie"

class ControllerValues extends React.Component{

  state = {
    values: [],
    form_visible: false,
    value_name: "Value label",
    value_description: "Value description",
  };

  handleEnableForm = (event) => {
        this.setState({
          form_visible: !this.state.form_visible,
        })

  }

  handleUpdateForm = (event) => {
    event.value_name ?
        this.setState({
          value_name: event.value_name,
        })
          :
        this.setState({
          value_description: event.value_description,
        })
  }

  handleAddValue = (event) => {
    fetch('http://127.0.0.1:8000/api/values/add/', {
      method: 'POST',
      body: JSON.stringify({"value_name": event.value_name,
              "value_description": event.value_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {
            responseAddedEntry.handleDeleteValue = this.handleDeleteValue
            this.state.values.unshift(responseAddedEntry)
            this.setState({
              value_name : "Value label",
              value_description : "Value description",
            })
          })
  }


  handleDeleteValue = (event) => {
    // console.log(event.id)
    // const csrftoken = Cookies.get('csrftoken')
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === event.id);
    newState.values.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/values/' + event.id, {
      method: 'delete',
      headers: {
        'content-type': 'application/json'
      }
    })
  }



  componentDidMount() {

    // console.log(Cookies.get('csrftoken'))

        fetch('http://127.0.0.1:8000/api/values/')
        .then(response => response.json())
        .then(responseData => {

      responseData.map((element) => {
        element.handleDeleteValue = this.handleDeleteValue;
        return element
      });

      this.setState({
        values: responseData
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
    return(
      <div>
        <div className="jumbotron pt-4">
          <div className="row mb-2">
            <div className = "col-auto justify-content-start ml-2 mr-4 mt-0 mb-0 h4 align-items-center">
              Want to add new values?
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
              <ValueForm props={{"value_name": this.state.value_name,
                                  "value_description": this.state.value_description,
                                  "handleUpdateForm": this.handleUpdateForm,
                                  "handleAddValue": this.handleAddValue}}>
                    <CloseButton props={{button_function: this.handleEnableForm}}/>
              </ValueForm>
          </Modal>

          <div className="list-group">
          {this.state.values.map(list_value =>
            <ValueSmall props = {list_value} key ={list_value.id}/>)}
          </div>

        </div>


      </div>

  )}

  }

//

export default ControllerValues
  // <div class="row">
  //       {this.state.values.map(list_value =>
  //         <Value value_props = {list_value}
  //                 handleDeleteValue={this.handleDeleteValue}
  //                 key ={list_value.id}/>)}
  // </div>
