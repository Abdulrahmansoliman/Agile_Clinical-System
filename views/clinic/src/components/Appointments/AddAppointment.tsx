import React, { useState } from "react";
import "../styles/itemform.css";

const AddAppointment = () => {
  const [patientId, setPatientId] = useState("");
  const [doctorId, setDoctorId] = useState("");
  const [secretaryId, setSecretaryId] = useState("");
  const [startTime, setStartTime] = useState("");
  const [notes, setNotes] = useState("");

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new patient object with the input values
    const newAppointment = {
      patient_id: patientId,
      doctor_id: doctorId,
      secretary_id: secretaryId,
      start_time: startTime,
      notes: notes,
    };
    console.log(newAppointment);
    // Make a POST request to the API endpoint with the new patient data
    fetch("http://127.0.0.1:5000/appointments/", {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(newAppointment),
    })
      .then((response) => {
        console.log(response);
        console.log("Appointment added successfully!");
        // Reset the form input values
        setPatientId("");
        setDoctorId("");
        setSecretaryId("");
        setStartTime("");
        setNotes("");
      })

      .catch((error) => {
        console.error("Failed to add Appointment.", error);
      });
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <label>
          Patient ID:
          <input
            name="patientId"
            type="text"
            value={patientId}
            onChange={(e) => setPatientId(e.target.value)}
          />
        </label>
        <br />
        <label>
          Doctor ID:
          <input
            name="doctorId"
            type="text"
            value={doctorId}
            onChange={(e) => setDoctorId(e.target.value)}
          />
        </label>
        <br />
        <label>
          Secretary ID:
          <input
            name="secretaryId"
            type="text"
            value={secretaryId}
            onChange={(e) => setSecretaryId(e.target.value)}
          />
        </label>
        <br />
        <label>
          Start Time:
          <input
            name="startTime"
            type="date"
            value={startTime}
            onChange={(e) => setStartTime(e.target.value)}
          />
        </label>
        <br />
        <label>
          Notes:
          <input
            name="notes"
            type="text"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Add Patient</button>
      </form>
    </div>
  );
};

export default AddAppointment;
