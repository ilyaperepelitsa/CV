import React from "react";
import Value from "./Value"
import ValueForm from "./ValueForm"


class ValueList extends React.Component{
  count = 0
  state = {
    values: [],
    value_name: "Value label",
    value_description: "Value description",
  };

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
    fetch('http://127.0.0.1:8000/api/add/', {
      method: 'POST',
      body: JSON.stringify({"value_name": event.value_name,
              "value_description": event.value_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {
            this.state.values.unshift(responseAddedEntry)
            this.setState({
              value_name : "Value label",
              value_description : "Value description",
            })
          })
  }

  handleClick = (event) => {
    console.log(event)
    if (this.timeout) clearTimeout(this.timeout)
    this.count++
    this.timeout = setTimeout(() => {
      if (this.count === 2) {
        const newState = this.state;
        const index = newState.values.findIndex(a => a.id === event.id);

        event.value_name ?
              newState.values[index].edit_value = true
              :
              newState.values[index].edit_description = true;
        this.setState(newState);
      }
      this.count = 0
    }, 250) // 250 ms
  }

  handleDeleteValue = (event) => {
    // console.log(event.id)
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === event.id);
    newState.values.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/' + event.id, {
      method: 'delete'})
  }

  handleUpdate = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === event.id);

    event.value_name ?
          (newState.values[index].value_name === event.value
              ? newState.values[index].edited_value = null
              : newState.values[index].edited_value = event.value)
            :
            (newState.values[index].value_description === event.value
              ? newState.values[index].edited_description = null
              : (newState.values[index].edited_description = event.value)
            )

    this.setState(newState);
  }


  handleBlur = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === event.id);

    event.value_name ?
          newState.values[index].edit_value = false
          :
          newState.values[index].edit_description = false;
    this.setState(newState);
  }

  handleUpdateValue = (event) => {
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === event.id);
    event.value_name ?
        this.setState({
          value_name: event.value_name,
        })
          :
        this.setState({
          value_description: event.value_description,
        })

    newState.values[index] = event;
    this.setState(newState);
  }

  submitChangeFunc = (event) => {

    // console.log(event)
   fetch('http://127.0.0.1:8000/api/' + event.id + "/", {
     method: 'put',
     body: JSON.stringify({
             "id": event.id,
             "value_name": event.edited_value ? event.edited_value : event.value_name,
             "value_description": event.edited_description ? event.edited_description : event.value_description,}),
     headers: {
         'content-type': 'application/json'},
 }).then(response => response.json()).then(responseUpdatedEntry => {
   const newState = this.state;
   const index = newState.values.findIndex(a => a.id === responseUpdatedEntry.id);
   newState.values[index] = responseUpdatedEntry;
   this.setState(newState);
 })
}

 discardChangeFunc = (event) => {
   const newState = this.state;
   const index = newState.values.findIndex(a => a.id === event.id);
   event.value_name ?
       newState.values[index].edited_value = null
         :
       newState.values[index].edited_description = null

   this.setState(newState);
  }

  componentDidMount() {
        fetch('http://127.0.0.1:8000/api/')
        .then(response => response.json())
        .then(responseData => {

      responseData.map((element) => {
        element.edit_value = false;
        element.edit_description = false;
        element.edited_value = null;
        element.edited_description = null;
        element.handleDeleteValue = this.handleDeleteValue;
        element.handleUpdate = this.handleUpdate;
        element.handleClick = this.handleClick;
        element.handleBlur = this.handleBlur;
        element.discardChangeFunc = this.discardChangeFunc;
        element.submitChangeFunc = this.submitChangeFunc;
        return element
      });

      this.setState({
        values: responseData
      });
        })
        .catch(error => {
          console.log('Fetching and parsing data error', error);
        });
      }
  componentWillUpdate () {
    if (this.timeout) clearTimeout(this.timeout)
  }

  render(){
    return(
      <div>
          <ValueForm props={{"value_name": this.state.value_name,
                              "value_description": this.state.value_description,
                              "handleUpdateForm": this.handleUpdateForm,
                              "handleAddValue": this.handleAddValue}}/>
          <div className="row">
            {this.state.values.map(list_value =>
              <Value props = {list_value}
                      key ={list_value.id}/>)}
           </div>
      </div>

  )}

  }

export default ValueList
  // <div class="row">
  //       {this.state.values.map(list_value =>
  //         <Value value_props = {list_value}
  //                 handleDeleteValue={this.handleDeleteValue}
  //                 key ={list_value.id}/>)}
  // </div>
