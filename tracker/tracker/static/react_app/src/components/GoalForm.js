import React from "react";

import $ from "jquery"

// const ValueForm = (props) => {
class GoalForm extends React.Component{
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
    return(
      <div className="container border border-dark rounded card text-white bg-dark mb-3 mainFormValue">
        <div className="card-body col-lg-3-auto">
          <div className="row">
            <h1 className="card-title col">Create new goal</h1>
            <div className = "col-auto align-self-center">{this.props.children}</div>
          </div>

          <form >
            <div className="form-group row">
                <label className="col">How would you like to name the goal?
                  <input type="text"
                        name="goal_name"
                        value = {this.props.props.goal_name}
                        onChange={(event) => {
                                  this.props.props.handleUpdateForm({
                                    goal_name: event.target.value,
                                    })}
                                  }
                        className="form-control"/>
                </label>
            </div>

            <div className="form-group row">
              <label className="col" htmlFor="valueDescriptionCreate">Provide a concise descprition of the goal
                  <textarea
                        name="goal_description"
                        value={this.props.props.goal_description}
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
                            this.props.props.handleAddValue({
                              goal_name: this.props.props.goal_name,
                              goal_description: this.props.props.goal_description,
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

export default GoalForm;
