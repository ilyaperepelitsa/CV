import React from "react";

const Links = (props) => (
      <div>
        <div className="row clearfix align-items-center rounded mt-2">
          <div className="col"></div>
          <a className="col-2 bg-dark text-center rounded text-info align-self-end" href={props.url}>Posting</a>
        </div>
            {(props.external_url
              &&
              <div className="row clearfix align-items-center rounded mt-2">
                  <div className="col"></div>
                  <a className="col-2 bg-dark text-center rounded text-info align-self-end" href={props.external_url}>External url</a>
              </div>

          )}
      </div>
    )



export default Links;
