import React from "react";

const CompanyName = (props) => {
    console.log(props);
    let display_title;
    let display_title_provided;
    if (props.display_job_title) {
      display_title = props.display_job_title;
      display_title_provided = true;
    } else {
      display_title = props.job_title;
      display_title_provided = false;
    }
    // console.log(display_title);
    // console.log(display_title_provided);

    // console.log(props.company_name);
    // console.log(display_title_provided);
    // console.log(display_title_provided);

    // Not edited, was provided
    // Not edited, was filled by default
    // Edited by changing company name
    // Edited previously blank company name
    // Currently editing
    return(
        "pew"
    )

    //   <div>
    //
    //       <div className="row">
    //         <p className="h4">{props.company_name}</p>
    //       </div>
    //
    //       <div>
    //
    //             {!props.edited_company_name
    //               && !props.edit_company_name
    //               && display_title_provided
    //               && <div>{display_title}</div>}
    //             ||
    //             {!props.edited_company_name
    //               && !props.edit_company_name
    //               && !display_title_provided
    //               &&
    //               <div className="row">
    //                   <div className="col-sm-2">Filled</div>
    //                   <div className="col">{display_title}</div>
    //                </div>}
    //             ||
    //               {props.edited_company_name
    //                 && (props.edited_company_name !== display_title_provided)
    //               && !props.edit_company_name
    //               && display_title_provided
    //               &&
    //               <div className="row">
    //                   <div className="col-sm-2">Old</div>
    //                   <div className="col">{props.edited_company_name}</div>
    //                   <div className="col-sm-2">Edited</div>
    //                   <div className="col">{display_title}</div>
    //                </div>}
    //             ||
    //               {props.edited_company_name
    //                 && (props.edited_company_name !== display_title_provided)
    //               && !props.edit_company_name
    //               && !display_title_provided
    //               &&
    //               <div className="row">
    //                   <div className="col-sm-2">New</div>
    //                   <div className="col">{display_title}</div>
    //                </div>}
    //             ||
    //               {props.edit_company_name
    //               && <div>{display_title}</div>}
    //
    //       </div>
    //
    //   </div>
    //
    // )
    //
    //       }



export default CompanyName;
