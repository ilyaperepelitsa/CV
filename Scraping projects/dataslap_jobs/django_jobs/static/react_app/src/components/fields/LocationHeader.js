import React from "react";

const LocationHeader = (props) => (
      <div className="row bg-secondary clearfix align-items-center text-white rounded">
        <div className="col-sm-2 clearfix rounded p-0 m-0 text-center">Country: </div>
        <div className="col text-center bg-info rounded"> {props.country_name} </div>

        <div className="col-sm-2 clearfix rounded p-0 m-0 text-center">Location: </div>
        <div className="col text-center bg-info rounded"> {props.location_name} </div>
      </div>
  )




export default LocationHeader;
