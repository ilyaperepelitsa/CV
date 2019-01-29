import React from "react";

import Expand from '../../images/expand.svg'

const ExpandButton = (props) => (


  (props.props.id ?
    (props.props.target?
      <Expand className="expandButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </Expand>
      :
      <Expand className="expandButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </Expand>
    )

  :
  <Expand className="expandButton"
    onClick={props.props.button_function}>
  </Expand>)
)

// <use xlinkHref={'static/images/add.svg'}></use>
export default ExpandButton;
