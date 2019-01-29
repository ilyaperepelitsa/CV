import React from "react";

import $ from "jquery"

// const ValueForm = (props) => {
class ValueForm extends React.Component{
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
            <h1 className="card-title col">Create new value</h1>
            <div className = "col-auto align-self-center">{this.props.children}</div>
          </div>

          <form >
            <div className="form-group row">
                <label className="col">How would you like to name the value?
                  <input type="text"
                        name="value_name"
                        value = {this.props.props.value_name}
                        onChange={(event) => {
                                  this.props.props.handleUpdateForm({
                                    value_name: event.target.value,
                                    })}
                                  }
                        className="form-control"/>
                </label>
            </div>

            <div className="form-group row">
              <label className="col" htmlFor="valueDescriptionCreate">Provide a concise descprition of the value
                  <textarea
                        name="value_description"
                        value={this.props.props.value_description}
                        onChange={(event) => {
                                  this.props.props.handleUpdateForm({
                                    value_description: event.target.value,
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
                              value_name: this.props.props.value_name,
                              value_description: this.props.props.value_description,
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

export default ValueForm;
