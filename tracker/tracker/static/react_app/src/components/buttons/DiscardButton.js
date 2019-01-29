import React from "react";

import Discard from '../../images/close.svg'

const DiscardButton = (props) => (

  (props.props.id ?
    (props.props.target?
      <Discard className="discardButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Discard>
      :
      <Discard className="discardButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Discard>
    )

  :
  <Discard className="discardButton"
    onClick={props.props.button_function}>
  </Discard>)
)

// <use xlinkHref={'static/images/add.svg'}></use>
export default DiscardButton;
