import React, { useState } from "react";
import PatientList from "../components/Patients/PatientList";
import AddPatient from "../components/Patients/AddPatientForm";
import "./styles/patient.css";

const Patient = () => {
  return (
    <div className="patientcontainer">
      <PatientList />
    </div>
  );
};

export default Patient;
