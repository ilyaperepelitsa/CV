import React from "react";

const SkillFields = (props) => (
        <div>
        <div className="col p-0 m-0 mb-2 text-center">
            First Skill
        </div>
        <div className="row">
          {(props.skillset
            &&
            (props.skillset.map(function(skill){
              if (skill.skill_id === props.skill_1) {
                return <button className="col btn btn-info mr-2 mt-2"
                          onClick={(event) => {
                                              props.handleSkillSelect({
                                                job_id : props.job_id,
                                                skill_1 : true,
                                                skill_id : skill.skill_id})
                                                }}
                            key ={skill.skill_id}>{skill.skill_label}</button>
              } else if (skill.skill_id === props.skill_2){
                return <button className="col btn btn-secondary mr-2 mt-2"
                            disabled
                            onClick={(event) => {
                                      props.handleSkillSelect({
                                        job_id : props.job_id,
                                        skill_1 : true,
                                        skill_id : skill.skill_id})
                                        }}
                              key ={skill.skill_id}>{skill.skill_label}</button>
              } else {
                return <button className="col btn btn-secondary mr-2 mt-2"
                            onClick={(event) => {
                                      props.handleSkillSelect({
                                        job_id : props.job_id,
                                        skill_1 : true,
                                        skill_id : skill.skill_id})
                                        }}
                              key ={skill.skill_id}>{skill.skill_label}</button>
              }

            })))}
          </div>

        <div className="col p-0 m-0 mb-2 mt-2 text-center">
          Second Skill
        </div>
        <div className="row">
          {(props.skillset
            &&
            (props.skillset.map(function(skill){
              if (skill.skill_id === props.skill_2) {
                return <button className="col btn btn-info mr-2 mt-2"
                              onClick={(event) => {
                                        props.handleSkillSelect({
                                          job_id : props.job_id,
                                          skill_2 : true,
                                          skill_id : skill.skill_id})
                                          }}
                              key ={skill.skill_id}>{skill.skill_label}</button>
              } else if (skill.skill_id === props.skill_1){
                return <button className="col btn btn-secondary mr-2 mt-2"
                            disabled
                            onClick={(event) => {
                                      props.handleSkillSelect({
                                        job_id : props.job_id,
                                        skill_2 : true,
                                        skill_id : skill.skill_id})
                                        }}
                            key ={skill.skill_id}>{skill.skill_label}</button>
              } else {
                return <button className="col btn btn-secondary mr-2 mt-2"
                            onClick={(event) => {
                                      props.handleSkillSelect({
                                        job_id : props.job_id,
                                        skill_2 : true,
                                        skill_id : skill.skill_id})
                                        }}
                            key ={skill.skill_id}>{skill.skill_label}</button>

              }

            })))}
          </div>
        </div>
      )


// <div className="row">
//       {props.skillset.map(skill =>
//         )}
//   </div>)


export default SkillFields;
