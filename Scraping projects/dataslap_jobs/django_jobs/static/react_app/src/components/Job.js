import React from "react";
import CompanyName from "./fields/CompanyName"
import JobTitle from "./fields/JobTitle"
import DateFooter from "./fields/DateFooter"
import LocationHeader from "./fields/LocationHeader"
import SourceHeader from "./fields/SourceHeader"
import Links from "./fields/Links"
import SkillFields from "./fields/SkillFields"

// class Job extends React.Component{
//   constructor(props){
//     super(props);
//     this.count = 0
//     if (this.props.value_props.display_job_title) {
//       var display_title = this.props.value_props.display_job_title;
//       var display_title_provided = true;
//     } else {
//       var display_title = this.props.value_props.job_title;
//       var display_title_provided = false;
//     }
//
//     this.state = {
//       job_id: this.props.value_props.job_id,
//       company_name: this.props.value_props.company_name,
//       job_title: this.props.value_props.job_title,
//       url: this.props.value_props.url,
//       external_url: this.props.value_props.external_url,
//       location_name: this.props.value_props.location_name,
//       display_company_name: this.props.value_props.display_company_name,
//       display_job_title: display_title,
//       display_title_provided,
//       date_published: this.props.value_props.date_published,
//       date_scraped: this.props.value_props.date_scraped,
//     };
//   }
//
//   render() {
//
//
//     return(
//       <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0">
//
//         <div className="card-body">
//
//             <div className="row">
//               <p>{this.state.company_name}</p>
//             </div>
//
//             <div className="row">
//               <p>{this.display_title_provided && <h1>PEW</h1>} {this.state.display_company_name}</p>
//             </div>
//
//             <div className="row">
//               <p>{this.state.job_title}</p>
//             </div>
//
//             <div className="row">
//               <p>{this.state.display_job_title}</p>
//             </div>
//
//         </div>
//
//           </div>
//     )
//
//           }
//
//   }



const Job = (props) => {
  // let display_title;
  // let display_title_provided;
  // if (props.props.display_job_title) {
  //   display_title = props.props.display_job_title;
  //   display_title_provided = true;
  // } else {
  //   display_title = props.props.job_title;
  //   display_title_provided = false;
  // }

    // console.log(display_title);
    // console.log(display_title_provided);

    // console.log(props.value_props);
    // console.log(display_title_provided);
    // console.log(props.value_props.skillset);

    return(
      <div className="col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0"
        onClick={(event) => {
                  props.handleModal({props})}}>
          <DateFooter props = {props.value_props}/>


          <div className="card-body">

              <SourceHeader props = {props.value_props.props}/>
              <CompanyName props = {props.value_props.props}/>
              <JobTitle props = {props.value_props.props}/>
              <Links props = {props.value_props.props}/>
              <SkillFields props = {props.value_props}/>
          </div>
          <LocationHeader props = {props.value_props.props}/>

      </div>
    )

          }



export default Job;
