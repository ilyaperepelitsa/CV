import React from "react";
import Job from "./Job"
import JobModal from "./JobModal"

class JobList extends React.Component{
  count = 0
  selectedJob: undefined;
  state = {
    values : []
  }

  handleClick = (event) => {
    if (this.timeout) clearTimeout(this.timeout)
    this.count++
    this.timeout = setTimeout(() => {
      if (this.count === 2) {
        const newState = this.state;
        const index = newState.values.findIndex(a => a.job_id === event.job_id);

        event.company_name ?
              newState.values[index].edit_company_name = true
              :
              newState.values[index].edit_title = true;
        this.setState(newState);
      }
      this.count = 0
    }, 250) // 250 ms
  }

  handleBlur = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.values.findIndex(a => a.job_id === event.job_id);

    event.company_name ?
          newState.values[index].edit_company_name = false
          :
          newState.values[index].edit_title = false;
    this.setState(newState);
  }

  handleDiscard = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.values.findIndex(a => a.job_id === event.job_id);

    if (event.company_name){
          newState.values[index].edit_company_name = false
          newState.values[index].edited_company_name = null
        } else{
          newState.values[index].edit_title = false;
          newState.values[index].edited_title = null;}
    this.setState(newState);
  }

  handleChange = (event) => {
    // handle saving here
    const newState = this.state;
    const index = newState.values.findIndex(a => a.job_id === event.job_id);

    event.company_name ?
          ((newState.values[index].display_company_name
            &&
            newState.values[index].display_company_name === event.value)
              ? newState.values[index].edited_company_name = null
              : (newState.values[index].company_name === event.value
                 ? newState.values[index].edited_company_name = null
                 : newState.values[index].edited_company_name = event.value)
            )
            :
            ((newState.values[index].display_job_title
            &&
            newState.values[index].display_job_title === event.value)
              ? newState.values[index].edited_title = null
              : (newState.values[index].job_title === event.value
                 ? newState.values[index].edited_title = null
                 : newState.values[index].edited_title = event.value)
            )

    this.setState(newState);
  }

  handleSkillSelect = (event) => {
    const newState = this.state;
    const index = newState.values.findIndex(a => a.job_id === event.job_id);

    event.skill_1 ?
          (newState.values[index].skill_1 == event.skill_id
            ?
            newState.values[index].skill_1 = null
            :
            newState.values[index].skill_1 = event.skill_id
          )
          :
          (newState.values[index].skill_2 == event.skill_id
            ?
            newState.values[index].skill_2 = null
            :
            newState.values[index].skill_2 = event.skill_id
          );
    this.setState(newState);
  }


  handleModal = (event) => {
    console.log(event);
    // this.setState({
    //   selectedJob: event
    // });
  }

  componentWillUpdate () {
  if (this.timeout) clearTimeout(this.timeout)
}


  componentWillMount() {
      fetch('http://127.0.0.1:8000/api/get/all_joined_jobs/', {
        headers: {
          'content-type': 'application/json'}
      })
      .then(response => response.json())
      .then(responseData => {

        responseData.map((element) => {
          element.edited_company_name = null;
          element.edited_title = null;
          element.edit_company_name = false;
          element.edit_title = false;
          element.handleClick = this.handleClick;
          element.handleBlur = this.handleBlur;
          element.handleChange = this.handleChange;
          element.handleDiscard = this.handleDiscard;
          element.handleSkillSelect = this.handleSkillSelect;
          element.skill_1 = null;
          element.skill_2 = null;
          element.handleModal = this.handleModal;
          return element
        });

        this.setState({
          values: responseData
        });

        fetch('http://127.0.0.1:8000/api/get/skills/', {
        headers: {
          'content-type': 'application/json'}
            })
            .then(responseSkillset => responseSkillset.json())
            .then(responseSkillsetData => {
              const newState = this.state;
              // console.log(responseData)
              // console.log(this.state)
              newState.values.map((element) => {
                element.skillset = responseSkillsetData;
                // return element
              });

              this.setState(newState);
            })
            .catch(error => {
              console.log('Fetching and parsing data error', error);
            })
      })
      .catch(error => {
        console.log('Fetching and parsing data error', error);
      });



    }



    render(){
      // console.log(this.state.skills);
      return(
        <div>
            <div className="row">
                  {this.state.values.slice(0, 10).map(list_value =>
                    <Job value_props={list_value}
                            key ={list_value.job_id}/>)}
            </div>
        </div>

      )}

}
export default JobList;
