import React from "react";
import Goal from "./Goal"
import GoalForm from "./GoalForm"


class GoalList extends React.Component{
  count = 0
  state = {
    goals: [],
    goal_name: "Goal label",
    goal_description: "Goal description",
  };

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

  handleAddValue = (event) => {
    fetch('http://127.0.0.1:8000/api/add/', {
      method: 'POST',
      body: JSON.stringify({"goal_name": event.goal_name,
              "goal_description": event.goal_description}),
      headers: {
          'content-type': 'application/json'}}).
          then(response => response.json()).
          then(responseAddedEntry => {
            this.state.goals.unshift(responseAddedEntry)
            this.setState({
              goal_name : "Value label",
              goal_description : "Value description",
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
        const index = newState.goals.findIndex(a => a.id === event.id);

        event.goal_name ?
              newState.goals[index].edit_value = true
              :
              newState.goals[index].edit_description = true;
        this.setState(newState);
      }
      this.count = 0
    }, 250) // 250 ms
  }

  handleDeleteValue = (event) => {
    // console.log(event.id)
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);
    newState.goals.splice(index, 1);
    this.setState(newState);
    fetch('http://127.0.0.1:8000/api/' + event.id, {
      method: 'delete'})
  }

  handleUpdate = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);

    event.goal_name ?
          (newState.goals[index].goal_name === event.value
              ? newState.goals[index].edited_value = null
              : newState.goals[index].edited_value = event.value)
            :
            (newState.goals[index].goal_description === event.value
              ? newState.goals[index].edited_description = null
              : (newState.goals[index].edited_description = event.value)
            )

    this.setState(newState);
  }


  handleBlur = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);

    event.goal_name ?
          newState.goals[index].edit_value = false
          :
          newState.goals[index].edit_description = false;
    this.setState(newState);
  }

  handleUpdateValue = (event) => {
    const newState = this.state;
    const index = newState.goals.findIndex(a => a.id === event.id);
    event.goal_name ?
        this.setState({
          goal_name: event.goal_name,
        })
          :
        this.setState({
          goal_description: event.goal_description,
        })

    newState.goals[index] = event;
    this.setState(newState);
  }

  submitChangeFunc = (event) => {

    // console.log(event)
   fetch('http://127.0.0.1:8000/api/' + event.id + "/", {
     method: 'put',
     body: JSON.stringify({
             "id": event.id,
             "goal_name": event.edited_value ? event.edited_value : event.goal_name,
             "goal_description": event.edited_description ? event.edited_description : event.goal_description,}),
     headers: {
         'content-type': 'application/json'},
 }).then(response => response.json()).then(responseUpdatedEntry => {
   const newState = this.state;
   const index = newState.goals.findIndex(a => a.id === responseUpdatedEntry.id);
   newState.goals[index] = responseUpdatedEntry;
   this.setState(newState);
 })
}

 discardChangeFunc = (event) => {
   const newState = this.state;
   const index = newState.goals.findIndex(a => a.id === event.id);
   event.goal_name ?
       newState.goals[index].edited_value = null
         :
       newState.goals[index].edited_description = null

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
        goals: responseData
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
          <GoalForm props={{"goal_name": this.state.goal_name,
                              "goal_description": this.state.goal_description,
                              "handleUpdateForm": this.handleUpdateForm,
                              "handleAddValue": this.handleAddValue}}/>
          <div className="row">
            {this.state.goals.map(list_value =>
              <Goal props = {list_value}
                      key ={list_value.id}/>)}
           </div>
      </div>

  )}

  }

export default GoalList
