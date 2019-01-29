import React from "react";

import Hide from '../../images/hide.svg'

const HideButton = (props) => (


  (props.props.id ?
    (props.props.target?
      <Hide className="hideButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Hide>
      :
      <Hide className="hideButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Hide>
    )

  :
  <Hide className="hideButton"
    onClick={props.props.button_function}>
  </Hide>)
)

// <use xlinkHref={'static/images/add.svg'}></use>
export default HideButton;
