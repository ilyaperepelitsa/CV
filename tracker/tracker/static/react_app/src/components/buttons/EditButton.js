import React from "react";

import Edit from '../../images/edit.svg'

const EditButton = (props) => (

  (props.props.id ?
    (props.props.target?
      <Edit className="editButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Edit>
      :
      <Edit className="editButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Edit>
    )

  :
  <Edit className="editButton"
    onClick={props.props.button_function}>
  </Edit>)

)

// <use xlinkHref={'static/images/add.svg'}></use>
export default EditButton;
