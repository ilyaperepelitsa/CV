import React from "react";

import Delete from '../../images/close.svg'

const DeleteButton = (props) => (


  (props.props.id ?
    (props.props.target?
      <Delete className="deleteButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Delete>
      :
      <Delete className="deleteButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Delete>
    )

  :
  <Delete className="deleteButton"
    onClick={props.props.button_function}>
  </Delete>)



  )

// <use xlinkHref={'static/images/add.svg'}></use>
export default DeleteButton;
