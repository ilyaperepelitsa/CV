"use strict";

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _defineProperty(obj, key, value) { if (key in obj) { Object.defineProperty(obj, key, { value: value, enumerable: true, configurable: true, writable: true }); } else { obj[key] = value; } return obj; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var ValueForm = function ValueForm(props) {

  var formFieldUpdate = function formFieldUpdate(event) {
    var form_value = event.target;
    props.handleUpdateForm(form_value);
  };

  var formSubmit = function formSubmit(event) {
    event.preventDefault();
    props.handleAddValue(props.form_fields);
  };

  return React.createElement(
    "div",
    { className: "container border border-dark rounded card text-white bg-dark mb-3 mainFormValue" },
    React.createElement(
      "div",
      { className: "card-body col-lg-1-auto" },
      React.createElement(
        "div",
        { className: "row" },
        React.createElement(
          "h1",
          { className: "card-title" },
          "Create new value"
        )
      ),
      React.createElement(
        "form",
        {

          onSubmit: formSubmit },
        React.createElement(
          "div",
          { className: "form-group row" },
          React.createElement(
            "label",
            null,
            "How would you like to name the value?",
            React.createElement("input", { type: "text",
              name: "value_name",
              value: props.form_fields.value_name,
              onChange: formFieldUpdate,
              className: "form-control" })
          )
        ),
        React.createElement(
          "div",
          { className: "form-group row" },
          React.createElement(
            "label",
            { "for": "valueDescriptionCreate" },
            "Provide a concise descprition of the value",
            React.createElement("textarea", {
              name: "value_description",
              value: props.form_fields.value_description,
              onChange: formFieldUpdate,
              className: "form-control",
              rows: "3",
              id: "valueDescriptionCreate" })
          )
        ),
        React.createElement(
          "div",
          { className: "row" },
          React.createElement("input", { type: "submit",
            value: "Create",
            className: "btn btn-success btn-lg" })
        )
      )
    )
  );
};
// }


var Value = function (_React$Component) {
  _inherits(Value, _React$Component);

  function Value(props) {
    _classCallCheck(this, Value);

    var _this = _possibleConstructorReturn(this, (Value.__proto__ || Object.getPrototypeOf(Value)).call(this, props));

    _this.count = 0;
    _this.state = {
      id: _this.props.value_props.id,
      value_name: _this.props.value_props.value_name,
      value_description: _this.props.value_props.value_description,
      created_date: _this.props.value_props.created_date,
      edit: false,
      edited: false
    };
    // console.log(this.state);
    // this.deleteFunc = this.deleteFunc.bind(this);
    _this.submitChangeFunc = _this.submitChangeFunc.bind(_this);
    _this.discardChangeFunc = _this.discardChangeFunc.bind(_this);

    _this.handleClick = _this.handleClick.bind(_this);
    _this.handleBlur = _this.handleBlur.bind(_this);
    _this.handleChangeValue = _this.handleChangeValue.bind(_this);
    return _this;
  }

  _createClass(Value, [{
    key: "componentWillUnmount",
    value: function componentWillUnmount() {
      // cancel click callback
      if (this.timeout) clearTimeout(this.timeout);
    }
  }, {
    key: "handleClick",
    value: function handleClick(event) {
      var _this2 = this;

      if (this.timeout) clearTimeout(this.timeout);
      this.count++;
      this.timeout = setTimeout(function () {
        if (_this2.count === 2) {
          // this.setState({
          //   edit: true,
          // })
        }
        _this2.count = 0;
      }, 250); // 250 ms
    }
  }, {
    key: "handleBlur",
    value: function handleBlur(event) {
      // handle saving here
      if (this.props.value_props.value_name !== this.state.value_name) {
        this.setState({
          edited: true
        });
      }

      // close edit mode
      this.setState({
        edit: false
      });
    }
  }, {
    key: "handleChangeValue",
    value: function handleChangeValue(event) {
      this.setState(_defineProperty({}, event.event.target, event.target.value));
    }
  }, {
    key: "submitChangeFunc",
    value: function submitChangeFunc(event) {
      var _this3 = this;

      fetch('http://127.0.0.1:8000/api/' + this.props.value_props.id + "/", {
        method: 'put',
        body: JSON.stringify({
          "id": this.state.id,
          "value_name": this.state.value_name,
          "value_description": this.state.value_description,
          "created_date": this.state.created_date }),
        headers: {
          'content-type': 'application/json' }
      }).then(function (response) {
        return response.json();
      }).then(function (responseUpdatedEntry) {
        return _this3.props.updateValue(responseUpdatedEntry);
      });
      event.preventDefault();
      this.setState({
        edited: false
      });
    }
  }, {
    key: "discardChangeFunc",
    value: function discardChangeFunc(event) {
      this.setState({
        value_name: this.props.value_props.value_name,
        edited: false
      });
    }
  }, {
    key: "render",
    value: function render() {
      // console.log(this.state)
      var timeStamp = new Date(this.props.value_props.created_date);
      var divStyle = {
        maxWidth: "20rem",
        height: "20rem",
        margin: 10
      };

      return React.createElement(
        "div",
        { className: "col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0",
          style: divStyle },
        React.createElement("div", { className: "card-body" })
      );
    }
  }]);

  return Value;
}(React.Component);

var ValueList = function (_React$Component2) {
  _inherits(ValueList, _React$Component2);

  function ValueList(props) {
    _classCallCheck(this, ValueList);

    var _this4 = _possibleConstructorReturn(this, (ValueList.__proto__ || Object.getPrototypeOf(ValueList)).call(this, props));

    _this4.state = {
      values: [],
      value_name: "Value label",
      value_description: "Value description"
    };
    // this.deleteValue = this.deleteValue.bind(this);
    _this4.handleDeleteValue = _this4.handleDeleteValue.bind(_this4);
    _this4.handleAddValue = _this4.handleAddValue.bind(_this4);
    _this4.handleUpdateForm = _this4.handleUpdateForm.bind(_this4);
    // this.addValue = this.addValue.bind(this);
    _this4.updateValue = _this4.updateValue.bind(_this4);
    return _this4;
  }

  _createClass(ValueList, [{
    key: "componentDidMount",
    value: function componentDidMount() {
      var _this5 = this;

      fetch('http://127.0.0.1:8000/api/').then(function (response) {
        return response.json();
      }).then(function (responseData) {
        responseData = responseData.map(function (value) {
          value.edit_value = false;return value;
        });
        responseData = responseData.map(function (value) {
          value.edit_description = false;return value;
        });
        responseData = responseData.map(function (value) {
          value.edited_value = false;return value;
        });
        responseData = responseData.map(function (value) {
          value.edited_description = false;return value;
        });
        _this5.setState({
          values: responseData
        });
      }).catch(function (error) {
        console.log('Fetching and parsing data error', error);
      });
    }
  }, {
    key: "handleAddValue",
    value: function handleAddValue(value) {
      var _this6 = this;

      // console.log(value)
      fetch('http://127.0.0.1:8000/api/add/', {
        method: 'POST',
        body: JSON.stringify({ "value_name": value.value_name,
          "value_description": value.value_description }),
        headers: {
          'content-type': 'application/json' } }).then(function (response) {
        return response.json();
      }).then(function (responseAddedEntry) {
        var newState = _this6.state;
        newState.values.unshift(responseAddedEntry);
        _this6.setState(newState);
      });
    }
  }, {
    key: "handleUpdateForm",
    value: function handleUpdateForm(value_returned) {
      this.setState(_defineProperty({}, value_returned.name, value_returned.value));
    }
  }, {
    key: "handleEdit",
    value: function handleEdit(value_entry) {
      var newState = this.state;
      var index = newState.values.findIndex(function (a) {
        return a.id === value_entry.id;
      });
      newState.values[index] = value_entry;
      this.setState(newState);
    }
  }, {
    key: "updateValue",
    value: function updateValue(value_entry) {
      var newState = this.state;
      var index = newState.values.findIndex(function (a) {
        return a.id === value_entry.id;
      });
      newState.values[index] = value_entry;
      this.setState(newState);
    }
  }, {
    key: "render",
    value: function render() {
      var _this7 = this;

      console.log(this.state.values);
      return React.createElement(
        "div",
        null,
        React.createElement(ValueForm, { form_fields: { "value_name": this.state.value_name,
            "value_description": this.state.value_description },
          handleUpdateForm: this.handleUpdateForm,
          handleAddValue: this.handleAddValue
        }),
        React.createElement(
          "div",
          { "class": "row" },
          this.state.values.map(function (list_value) {
            return React.createElement(Value, { value_props: list_value,
              handleDeleteValue: _this7.handleDeleteValue,
              key: list_value.id });
          })
        )
      );
    }
  }]);

  return ValueList;
}(React.Component);

var defaultValues = {
  value_name: "Value label",
  value_description: "Value description"
};

var destination_list = document.getElementById("app");
// REACT PART
ReactDOM.render(
// REACT WHAT

React.createElement(ValueList, null),

// REACT WHERE - div id of the app
destination_list);
