class ValueForm extends React.Component{

  constructor(props){
    super(props);
    this.state = {
      value_name : this.props.value_name,
      value_description : this.props.value_description
    };
    this.handleChangeValue = this.handleChangeValue.bind(this);
    this.handleChangeDescription = this.handleChangeDescription.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);

  }

  handleChangeValue(event){
    this.setState({
      value_name: event.target.value,
    })
    console.log(this.state.value_name)
  }

  handleChangeDescription(event){
    this.setState({
      value_description: event.target.value,
    })
  }

  handleSubmit(event){
    alert("A name was submitted: " + this.state.value_name)
    event.preventDefault();
  }

  render(){


    return(
      <form onSubmit={this.handleSubmit}>
        <label>How would you like to name the value?
          <input type="text" value={this.state.value_name} onChange={this.handleChangeValue}/>
        </label>

        <label>Provide a concise descprition of the value
          <input type="text" value={this.state.value_description} onChange={this.handleChangeDescription}/>
        </label>

        <input type="submit" value="Submit"/>
        <h2>{this.state.value_name}</h2>
      </form>
    )
  }
}

let defaultValues = {
value_name : "Value label",
value_description : "Value description"
}

var destination = document.getElementById("app");
// REACT PART
ReactDOM.render(
  // REACT WHAT

    <ValueForm {...defaultValues}/>

  ,

  // REACT WHERE - div id of the app
  destination
);
