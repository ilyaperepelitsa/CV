import React from "react";
import Modal from "react-modal";


const JobModal = (props) => {
  <Modal
    isOpen={!!props.selectedJob}
    contentLabel="Selected Job">
    onRequestClose={}

    <h3>{props.selectedJob.company_name}</h3>

  </Modal>
}

export default JobModal;
