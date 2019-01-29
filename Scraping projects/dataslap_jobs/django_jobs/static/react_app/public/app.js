'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var JobList = function (_React$Component) {
  _inherits(JobList, _React$Component);

  function JobList(props) {
    _classCallCheck(this, JobList);

    var _this = _possibleConstructorReturn(this, (JobList.__proto__ || Object.getPrototypeOf(JobList)).call(this, props));

    _this.state = {
      values: []
    };
    return _this;
  }

  _createClass(JobList, [{
    key: 'componentDidMount',
    value: function componentDidMount() {
      var _this2 = this;

      fetch('http://127.0.0.1:8000/api/get/all_joined_jobs/', {
        headers: {
          'content-type': 'application/json' }
      }).then(function (response) {
        return response.json();
      }).then(function (responseData) {
        _this2.setState({
          values: responseData
        });
      }).catch(function (error) {
        console.log('Fetching and parsing data error', error);
      });
    }
  }, {
    key: 'render',
    value: function render() {
      console.log(this.state.values);
      return React.createElement(
        'div',
        { 'class': 'row' },
        this.state.values.slice(0, 4).map(function (list_value) {
          return React.createElement(Job, { value_props: list_value,
            key: list_value.job_id });
        })
      );
    }
  }]);

  return JobList;
}(React.Component);

var Job = function (_React$Component2) {
  _inherits(Job, _React$Component2);

  function Job(props) {
    _classCallCheck(this, Job);

    var _this3 = _possibleConstructorReturn(this, (Job.__proto__ || Object.getPrototypeOf(Job)).call(this, props));

    _this3.count = 0;
    if (_this3.props.value_props.display_job_title) {
      var display_title = _this3.props.value_props.display_job_title;
    } else {
      var display_title = _this3.props.value_props.job_title;
    }
    display_title = _this3.state = {
      job_id: _this3.props.value_props.job_id,
      company_name: _this3.props.value_props.company_name,
      job_title: _this3.props.value_props.job_title,
      url: _this3.props.value_props.url,
      external_url: _this3.props.value_props.external_url,
      location_name: _this3.props.value_props.location_name,
      display_company_name: _this3.props.value_props.display_company_name,
      display_job_title: display_title + "////",
      date_published: _this3.props.value_props.date_published,
      date_scraped: _this3.props.value_props.date_scraped
    };
    return _this3;
  }

  _createClass(Job, [{
    key: 'render',
    value: function render() {

      return React.createElement(
        'div',
        { className: 'col-lg-2-auto card text-dark bg-light mb-3 container rounded-bottom border-0' },
        React.createElement(
          'div',
          { className: 'card-body' },
          React.createElement(
            'div',
            { className: 'row' },
            React.createElement(
              'p',
              null,
              this.state.company_name
            )
          ),
          React.createElement(
            'div',
            { className: 'row' },
            React.createElement(
              'p',
              null,
              this.state.display_company_name
            )
          ),
          React.createElement(
            'div',
            { className: 'row' },
            React.createElement(
              'p',
              null,
              this.state.job_title
            )
          ),
          React.createElement(
            'div',
            { className: 'row' },
            React.createElement(
              'p',
              null,
              this.state.display_job_title
            )
          )
        )
      );
    }
  }]);

  return Job;
}(React.Component);

var destination_list = document.getElementById("app");
ReactDOM.render(React.createElement(JobList, null), destination_list);
