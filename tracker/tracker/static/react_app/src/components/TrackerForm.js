import React from "react";

import $ from "jquery"

// const ValueForm = (props) => {
class TrackerForm extends React.Component{
  // state = {
  //   values: [],
  //   form_visible: false,
  //   value_name: "Value label",
  //   value_description: "Value description",
  // };
    componentDidMount() {
      $("html svg").children("title").remove();
      $("html svg").children("desc").remove();
    }
    render(){
      // console.log(this.props)
    return(
      <div className="container border border-dark rounded card text-white bg-dark mb-3 mainFormValue">
        <div className="card-body col-lg-3-auto">
          <div className="row">
            <h1 className="card-title col">Start a new </h1>
            <div className = "col-auto align-self-center">{this.props.children}</div>
          </div>

          <form >
            <div className="form-group row">
                <label className="col">How would you like to name the task?
                  <input type="text"
                        name="task_name"
                        value = {this.props.props.task_name}
                        onChange={(event) => {
                                  this.props.props.handleUpdateForm({
                                    task_name: event.target.value,
                                    })}
                                  }
                        className="form-control"/>
                </label>
            </div>

            <div className="form-group row">
              <label className="col" htmlFor="valueDescriptionCreate">Provide a concise descprition of the task
                  <textarea
                        name="goal_description"
                        value={this.props.props.task_description}
                        onChange={(event) => {
                                  this.props.props.handleUpdateForm({
                                    goal_description: event.target.value,
                                    })}
                                  }
                        className="form-control"
                        rows="3"
                        id="valueDescriptionCreate"/>
              </label>
            </div>

            <div className="form-group row">
                <div className="col">
                <input type="submit"
                        value="Create"
                        onClick = {
                          (event) => {
                            event.preventDefault();
                            this.props.props.handleAddTask({
                              task_name: this.props.props.task_name,
                              goal_description: this.props.props.task_description,
                            });
                          }
                        }
                        className="btn btn-success btn-lg col"/>
                </div>
            </div>
          </form>
          </div>

      </div>
    )

  }
}

export default TrackerForm;
