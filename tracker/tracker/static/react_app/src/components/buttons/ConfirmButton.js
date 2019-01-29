import React from "react";

import Confirm from '../../images/confirm.svg'

const ConfirmButton = (props) => (

  (props.props.id ?
    (props.props.target?
      <Confirm className="confirmButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Confirm>
      :
      <Confirm className="confirmButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Confirm>
    )

  :
  <Confirm className="confirmButton"
    onClick={props.props.button_function}>
  </Confirm>)
)

// <use xlinkHref={'static/images/add.svg'}></use>
export default ConfirmButton;
