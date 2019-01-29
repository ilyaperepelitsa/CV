import React from "react";

import View from '../../images/view.svg'

const ViewButton = (props) => (


  (props.props.id ?
    (props.props.target?
      <View className="viewButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id,
                                                      target: props.props.target})}
                      }>
      </View>
      :
      <View className="viewButton"
            onClick={(event) => {
                        props.props.button_function({id : props.props.id})}
                      }>
      </View>
    )

  :
  <View className="viewButton"
    onClick={props.props.button_function}>
  </View>)
)

// <use xlinkHref={'static/images/add.svg'}></use>
export default ViewButton;
