import React from "react";

const CompanyName = (props) => {
    // console.log();

    let display_company;
    let display_company_provided;
    if (props.edited_company_name) {
      display_company = props.edited_company_name;
      display_company_provided = null;
    }else if (props.display_company_name) {
      display_company = props.display_company_name;
      display_company_provided = true;
    } else {
      display_company = props.company_name;
      display_company_provided = false;
    };

    // Not edited, was provided
    // Not edited, was filled by default
    // Edited by changing company name
    // Edited previously blank company name
    // Currently editing
    // console.log(props.hangleClick);
    return(
      <div>
          <div className="row customRow align-items-center">
              <p className="col h4 text-center" >{props.company_name}</p>
          </div>

          {(!props.edited_company_name
            && !props.edit_company_name
            && display_company_provided
            &&
            <div className="row customRow align-items-center">
                <div className="col-sm-2 alert alert-secondary p-0 m-0 text-center">Provided</div>
                <div onClick={(event) => {
                            props.handleClick({job_id : props.job_id,
                                                      company_name : props.company_name,
                                                      display_company_name : props.display_company_name})
                            }
                          }
                          className="col">{display_company} </div>

             </div>)
          ||
          (!props.edited_company_name
            && !props.edit_company_name
            && !display_company_provided
            &&
            <div className="row customRow align-items-center">
                <div className="col-sm-2 alert alert-warning p-0 m-0 text-center">Filled</div>
                <div onClick={(event) => {
                            props.handleClick({job_id : props.job_id,
                                                      company_name : props.company_name,
                                                      display_company_name : props.display_company_name})
                            }
                          }
                    className="col">{display_company}</div>
             </div>)
          ||
            (props.edited_company_name
              && (props.edited_company_name !== display_company_provided)
            && !props.edit_company_name
            && display_company_provided
            &&
            <div className="row customRow align-items-center">
                <div className="col-sm-2 alert alert-dark p-0 m-0 text-center">Old</div>
                <div className="col">{props.edited_company_name}</div>
                <div className="col-sm-2 alert alert-success p-0 m-0 text-center">Edited</div>
                <div onClick={(event) => {
                            props.handleClick({job_id : props.job_id,
                                                      company_name : props.company_name,
                                                      display_company_name : props.display_company_name})
                            }
                          }
                    className="col">{display_company}</div>
             </div>)
          ||
            (props.edited_company_name
              && (props.edited_company_name !== display_company_provided)
            && !props.edit_company_name
            &&
            <div className="row customRow align-items-center">
                <div className="col-sm-2 alert alert-success p-0 m-0 text-center">New</div>
                <div onClick={(event) => {
                            props.handleClick({job_id : props.job_id,
                                                      company_name : props.company_name,
                                                      display_company_name : props.display_company_name})
                            }
                          }
                    className="col">{display_company}</div>
                    <div className="col-md-4-auto">
                              <button onClick={(event) => {
                                          props.handleDiscard({job_id : props.job_id,
                                                                    company_name : props.company_name})
                                          }
                                        } className="btn btn-danger btn-sm">
                                Discard Changes
                              </button>
                          </div>
             </div>)
          ||
          (  props.edit_company_name
            && <div className="form-group">
                    <div className="row align-items-center">
                          <div className="col-sm-2 alert alert-info p-0 m-0 text-center">
                            Original:
                          </div>
                          <div className="col">{display_company}</div>

                          <div className="col-sm-5 p-0 m-0">


                            <input type="text" value={display_company}
                                                onChange={(event) => {
                                                          props.handleChange({job_id : props.job_id,
                                                                company_name : props.company_name,
                                                                value : event.target.value})
                                                            }}
                                                autoFocus
                                                onBlur={(event) => {
                                                          props.handleBlur({job_id : props.job_id,
                                                                company_name : props.company_name,
                                                                display_company_name : props.display_company_name})
                                                            }}
                                                className="input-sm"/>
                          </div>
                      </div>
                      </div>)}


      </div>
    )
}



export default CompanyName;
