import React from "react";

import Close from '../../images/close.svg'

const CloseButton = (props) => (

  (props.props.id ?
    (props.props.target?
      <Close className="closeButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Close>
      :
      <Close className="closeButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Close>
    )

  :
  <Close className="closeButton"
    onClick={props.props.button_function}>
  </Close>)

  )

// <use xlinkHref={'static/images/add.svg'}></use>
export default CloseButton;
