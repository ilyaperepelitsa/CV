import React from "react";
import ReactDOM from "react-dom";


import "./styles/styles.scss"
import "normalize.css/normalize.css"


import RouterUrls from "./components/pages/RouterUrls"


var destination_list = document.getElementById("app");
// REACT PART
// ReactDOM.render(
//
//     <ValueList/>
//   ,
//
//   destination_list
// );

ReactDOM.render(

    <RouterUrls/>
    // <ControllerValues/>
  ,

  destination_list
);
