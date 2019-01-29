import React from "react";

const DateFooter = (props) => (
      <div className="row bg-dark clearfix align-items-center text-white rounded">
        <div className="col-sm-2 bg-dark clearfix rounded p-0 m-0 text-center">Published: </div>
        <div className="col text-center bg-info rounded"> {props.date_published} </div>

        <div className="col-sm-2 bg-dark clearfix rounded p-0 m-0 text-center">Scraped: </div>
        <div className="col text-center bg-info rounded"> {props.date_scraped} </div>
      </div>
    )



export default DateFooter;
