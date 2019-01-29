class JobList extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      values: []
    };
  }
  componentDidMount() {
      fetch('http://127.0.0.1:8000/api/get/all_joined_jobs/', {
        headers: {
          'content-type': 'application/json'}
      })
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
      console.log(this.state.values)
      return(
        <div class="row">
              {this.state.values.slice(0, 4).map(list_value =>
                <Job value_props = {list_value}
                        key ={list_value.job_id}/>)}
          </div>
      )}

}


class Job extends React.Component{
  constructor(props){
    super(props);
    this.count = 0
    if (this.props.value_props.display_job_title) {
      var display_title = this.props.value_props.display_job_title;
      var display_title_provided = true;
    } else {
      var display_title = this.props.value_props.job_title;
      var display_title_provided = false;
    }

    this.state = {
      job_id: this.props.value_props.job_id,
      company_name: this.props.value_props.company_name,
      job_title: this.props.value_props.job_title,
      url: this.props.value_props.url,
      external_url: this.props.value_props.external_url,
      location_name: this.props.value_props.location_name,
      display_company_name: this.props.value_props.display_company_name,
      display_job_title: display_title,
      display_title_provided,
      date_published: this.props.value_props.date_published,
      date_scraped: this.props.value_props.date_scraped,
    };
  }

  render() {


    return(
      <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0">

        <div className="card-body">

            <div className="row">
              <p>{this.state.company_name}</p>
            </div>

            <div className="row">
              <p>{this.display_title_provided && <h1>PEW</h1>} {this.state.display_company_name}</p>
            </div>

            <div className="row">
              <p>{this.state.job_title}</p>
            </div>

            <div className="row">
              <p>{this.state.display_job_title}</p>
            </div>

        </div>

          </div>
    )

          }

  }


var destination_list = document.getElementById("app");
ReactDOM.render(
    <JobList/>
  ,
  destination_list
);
