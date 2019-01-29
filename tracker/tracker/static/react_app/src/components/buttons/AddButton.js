import React from "react";
// import Add from '../../images/add.svg';

// import Add from 'svg-react-loader?name=Add!../../images/add.svg';
import Add from '../../images/add.svg'

const AddButton = (props) =>((props.props.id ?
    (props.props.target?
      <Add className="addButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Add>
      :
      <Add className="addButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Add>
    )

  :
  <Add className="addButton"
    onClick={props.props.button_function}>
  </Add>))



// <use xlinkHref={'static/images/add.svg'}></use>
export default AddButton;
