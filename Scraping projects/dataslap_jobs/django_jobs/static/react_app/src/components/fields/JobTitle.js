import React from "react";

const JobTitle = (props) => {
    // console.log(props);

        let display_title;
        let display_title_provided;
        if (props.edited_title) {
          display_title = props.edited_title;
          display_title_provided = null;
        }else if (props.display_job_title) {
          display_title = props.display_job_title;
          display_title_provided = true;
        } else {
          display_title = props.job_title;
          display_title_provided = false;
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
                  <div className="col-sm-2 p-0 m-0 text-center"></div>
                  <div className="col" >{props.job_title}</div>
              </div>

              {(!props.edited_title
                && !props.edit_title
                && display_title_provided
                &&
                <div className="row customRow align-items-center">
                    <div className="col-sm-2 alert alert-secondary p-0 m-0 text-center">Provided</div>
                    <div onClick={(event) => {
                                props.handleClick({job_id : props.job_id,
                                                          job_title : props.job_title,
                                                          display_job_title : props.display_job_title})
                                }
                              }
                              className="col">{display_title} </div>
                 </div>)
              ||
              (!props.edited_title
                && !props.edit_title
                && !display_title_provided
                &&
                <div className="row customRow align-items-center">
                    <div className="col-sm-2 alert alert-warning p-0 m-0 text-center">Filled</div>
                    <div onClick={(event) => {
                                props.handleClick({job_id : props.job_id,
                                                          job_title : props.job_title,
                                                          display_job_title : props.display_job_title})
                                }
                              }
                        className="col">{display_title}</div>
                 </div>)
              ||
                (props.edited_title
                  && (props.edited_title !== display_title_provided)
                && !props.edit_title
                && display_title_provided
                &&
                <div className="row customRow align-items-center">
                    <div className="col-sm-2 alert alert-dark p-0 m-0 text-center">Old</div>
                    <div className="col">{props.edited_title}</div>
                    <div className="col-sm-2 alert alert-success p-0 m-0 text-center">Edited</div>
                    <div onClick={(event) => {
                                props.handleClick({job_id : props.job_id,
                                                          job_title : props.job_title,
                                                          display_job_title : props.display_job_title})
                                }
                              }
                        className="col">{display_title}</div>
                 </div>)
              ||
                (props.edited_title
                  && (props.edited_title !== display_title_provided)
                && !props.edit_title
                &&
                <div className="row customRow align-items-center">
                    <div className="col-sm-2 alert alert-success p-0 m-0 text-center">New</div>
                    <div onClick={(event) => {
                                props.handleClick({job_id : props.job_id,
                                                          job_title : props.job_title,
                                                          display_job_title : props.display_job_title})
                                }
                              }
                        className="col">{display_title}</div>
                        <div className="col-md-4-auto">
                                  <button onClick={(event) => {
                                              props.handleDiscard({job_id : props.job_id,
                                                                        job_title : props.job_title})
                                              }
                                            } className="btn btn-danger btn-sm">
                                    Discard Changes
                                  </button>
                              </div>
                 </div>)
              ||
              (  props.edit_title
                && <div className="form-group">
                        <div className="row align-items-center">
                              <div className="col-sm-2 alert alert-info p-0 m-0 text-center">
                                Original:
                              </div>
                              <div className="col">{display_title}</div>

                              <div className="col-sm-5 p-0 m-0">

                                <input type="text" value={display_title}
                                                    onChange={(event) => {
                                                              props.handleChange({job_id : props.job_id,
                                                                    job_title : props.job_title,
                                                                    value : event.target.value})
                                                                }}
                                                    autoFocus
                                                    onBlur={(event) => {
                                                              props.handleBlur({job_id : props.job_id,
                                                                    job_title : props.job_title,
                                                                    display_job_title : props.display_job_title})
                                                                }}
                                                    className="input-sm"/>

                              </div>
                          </div>
                          </div>)}


          </div>
        )
    }




export default JobTitle;
