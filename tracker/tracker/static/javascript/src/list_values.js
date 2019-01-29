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
  }

  handleChangeDescription(event){
    this.setState({
      value_description: event.target.value,
    })
  }

  handleSubmit(event){
    // console.log(this.props.value_props.id);
    fetch('http://127.0.0.1:8000/api/add/', {
      method: 'POST',
      body: JSON.stringify({"value_name": this.state.value_name,
              "value_description": this.state.value_description}),
      headers: {
          'content-type': 'application/json'},
  }).then(response => response.json()).then(responseAddedEntry => this.props.addValue(responseAddedEntry))
    event.preventDefault();
    this.setState({
      value_name : this.props.value_name,
      value_description : this.props.value_description
    })
  }

  render(){


    return(
      <div className="container border border-dark rounded card text-white bg-dark mb-3 mainFormValue"
            style={{width: "30rem"}}>
        <div className="card-body col-lg-1-auto">
          <div className="row">
            <h1 className="card-title">Create new value</h1>
          </div>

          <form onSubmit={this.handleSubmit}>
            <div className="form-group row">
                <label>How would you like to name the value?
                  <input type="text"
                        value={this.state.value_name}
                        onChange={this.handleChangeValue}
                        className="form-control"/>
                </label>
            </div>

            <div className="form-group row">
              <label for="valueDescriptionCreate">Provide a concise descprition of the value
                  <textarea value={this.state.value_description}
                        onChange={this.handleChangeDescription}
                        className="form-control"
                        rows="3"
                        id="valueDescriptionCreate"/>
              </label>
            </div>

            <div className="row">
                <input type="submit"
                        value="Create"
                        onSubmit={this.handleSubmit}
                        className="btn btn-success btn-lg"/>
            </div>
          </form>
          </div>
    </div>
    )
  }
}


class Value extends React.Component{
  constructor(props){
    super(props);
    this.count = 0
    this.state = {
      ...this.props.value_props,
      edit: false,
      edited: false,
    };
    // console.log(this.state);
    this.deleteFunc = this.deleteFunc.bind(this);
    this.submitChangeFunc = this.submitChangeFunc.bind(this);
    this.discardChangeFunc = this.discardChangeFunc.bind(this);


    this.handleClick = this.handleClick.bind(this);
    this.handleBlur = this.handleBlur.bind(this);
    this.handleChangeValue = this.handleChangeValue.bind(this);
  }

  componentWillUnmount () {
    // cancel click callback
    if (this.timeout) clearTimeout(this.timeout)
  }

  handleClick(event) {
    if (this.timeout) clearTimeout(this.timeout)
    this.count++
    this.timeout = setTimeout(() => {
      if (this.count === 2) {
        this.setState({
          edit: true,
        })
      }
      this.count = 0
    }, 250) // 250 ms
  }

  handleBlur(event) {
    // handle saving here
    if (this.props.value_props.value_name !== this.state.value_name){
      this.setState({
        edited: true
      })
    }

    // close edit mode
    this.setState({
      edit: false,
    })
  }

  handleChangeValue(event){
    this.setState({
      value_name: event.target.value,
    })
  }

  deleteFunc(event) {
      this.props.deleteValue(this.props.value_props.id);
      fetch('http://127.0.0.1:8000/api/' + this.props.value_props.id, {
        method: 'delete'})
   }

   submitChangeFunc(event){
    // console.log(this.props.value_props.id);
    console.log({
              "id": this.state.id,
              "value_name": this.state.value_name,
              "value_description": this.state.value_description,
              "created_date": this.state.created_date});
    fetch('http://127.0.0.1:8000/api/' + this.props.value_props.id + "/", {
      method: 'put',
      body: JSON.stringify({
              "id": this.state.id,
              "value_name": this.state.value_name,
              "value_description": this.state.value_description,
              "created_date": this.state.created_date}),
      headers: {
          'content-type': 'application/json'},
  }).then(response => response.json()).then(responseUpdatedEntry => this.props.updateValue(responseUpdatedEntry))
    event.preventDefault();
    this.setState({
      edited: false
    })
  }

  discardChangeFunc(event) {
    this.setState({
      value_name: this.props.value_props.value_name,
      edited: false
    })
   }




  render() {
      // console.log(this.state)
      var timeStamp = new Date(this.props.value_props.created_date);
      const divStyle = {
        maxWidth: "20rem",
        height: "20rem",
        margin: 10
      };

      switch(true){
        case this.state.edit && !this.state.edited:
            return(
              <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>

                <div className="card-body">
                    <form>
                      <div className="form-group">
                          <p className="row">Original name of this value was:</p>
                          <p><strong className="card-title">{this.props.value_props.value_name}</strong></p>
                          <label for="valueEditForm">

                            <input type="text" value={this.state.value_name}
                                                onChange={this.handleChangeValue}
                                                autoFocus
                                                onBlur={this.handleBlur}
                                                className="form-control"
                                                id="valueEditForm"/>
                          </label>
                      </div>
                    </form>

                    <div className="row">
                      <p>{this.state.value_description}</p>
                    </div>

                </div>

                <div className="row bg-dark clearfix align-items-center text-white rounded">
                    <div className="col">
                      <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
                    </div>

                    <div className="col-2 delete-button-in-clearfix">
                      <button onClick={this.deleteFunc} className="btn btn-danger float-right">
                        Delete
                      </button>
                    </div>

                </div>
                  </div>
            )
        case !this.state.edit && this.state.edited:
            return(
              <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>
                  <div className="card-body">
                      <div className="row">
                        <h1 onClick={this.handleClick} className="card-title">{this.state.value_name}</h1>
                        <p>Original name of this value was: <strong>{this.props.value_props.value_name}</strong></p>
                      </div>

                      <div className="row">
                        <div className="col-md-4-auto">
                            <button onClick={this.submitChangeFunc} className="btn btn-success btn-sm">
                              Submit Edit
                            </button>
                        </div>

                        <div className="col-md-4-auto">
                            <button onClick={this.discardChangeFunc} className="btn btn-danger btn-sm">
                              Discard Changes
                            </button>
                        </div>
                      </div>

                      <div className="row">
                        <p>{this.state.value_description}</p>
                      </div>
                  </div>

                  <div className="row bg-dark clearfix align-items-center text-white rounded">
                      <div className="col">
                        <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
                      </div>

                      <div className="col-2 delete-button-in-clearfix">
                        <button onClick={this.deleteFunc} className="btn btn-danger float-right">
                          Delete
                        </button>
                      </div>
                  </div>

              </div>
            )
        default:
            return(
              <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0" style = {divStyle}>

                <div className="card-body">

                    <div className="row">
                      <h1 onClick={this.handleClick} className="card-title">{this.state.value_name}</h1>
                    </div>

                    <div className="row">
                      <p>{this.state.value_description}</p>
                    </div>

                </div>

                <div className="row bg-dark clearfix align-items-center text-white rounded">
                    <div className="col">
                      <p>{timeStamp.toString().slice(16, 21)}  {timeStamp.toString().slice(0, 16)}</p>
                    </div>

                    <div className="col-2 delete-button-in-clearfix">
                      <button onClick={this.deleteFunc} className="btn btn-danger float-right">
                        Delete
                      </button>
                    </div>

                </div>

              </div>
            )
      }
    }
  }


class ValueList extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      values: []
    };
    this.deleteValue = this.deleteValue.bind(this);
    this.addValue = this.addValue.bind(this);
    this.updateValue = this.updateValue.bind(this);
  }

  deleteValue(id) {
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === id);
    newState.values.splice(index, 1);
    this.setState(newState);
  }

  updateValue(value_entry) {
    const newState = this.state;
    const index = newState.values.findIndex(a => a.id === value_entry.id);
    newState.values[index] = value_entry;
    this.setState(newState);
  }

  addValue(value_entry) {
    const newState = this.state;
    newState.values.unshift(value_entry);
    this.setState(newState);

  }

  componentDidMount() {
        fetch('http://127.0.0.1:8000/api/')
        .then(response => response.json())
        .then(responseData => {
          this.setState({
            values: responseData
          });
        })
        .catch(error => {
          console.log('Fetching and parsing data error', error);
        });
      }

  render(){
    return(
      <div>
          <ValueForm {...defaultValues}
                      addValue={this.addValue}/>
          <div class="row">
              {this.state.values.map(list_value =>
                <Value value_props = {list_value}
                        deleteValue={this.deleteValue}
                        updateValue={this.updateValue}
                        key ={list_value.id}/>)}
          </div>
      </div>

  )}

  }

let defaultValues = {
value_name : "Value label",
value_description : "Value description"
}

var destination_list = document.getElementById("app");
// REACT PART
ReactDOM.render(
  // REACT WHAT

    <ValueList/>

  ,

  // REACT WHERE - div id of the app
  destination_list
);
