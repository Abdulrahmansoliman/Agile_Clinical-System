import React, { useState, useEffect } from "react";
import "./styles/AddAppointment.css";
import moment from "moment";

type Patients = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
};

type Doctors = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
  role: string;
  specialization: string;
  username: string;
};

const AddAppointment = () => {
  const [patients, setPatients] = useState<Patients[]>([]);
  const [doctors, setDoctors] = useState<Doctors[]>([]);

  const [patientId, setPatientId] = useState("");
  const [doctorId, setDoctorId] = useState("");
  const [secretaryId, setSecretaryId] = useState("");
  const [notes, setNotes] = useState("");
  const [date, setDate] = useState(moment().format("YYYY-MM-DDTHH:mm"));

  useEffect(() => {
    // Fetch all patients from the API
    fetch("http://127.0.0.1:5000/patients")
      .then((response) => response.json())
      .then((data) => {
        setPatients(data.data);
      })
      .catch((error) => {
        console.error("Failed to fetch patients.", error);
      });

    // Fetch all doctors from the API
    fetch("http://127.0.0.1:5000/doctors")
      .then((response) => response.json())
      .then((data) => {
        setDoctors(data.data);
      })
      .catch((error) => {
        console.error("Failed to fetch doctors.", error);
      });
  }, []);

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new appointment object with the input values
    const newAppointment = {
      patient_id: patientId,
      doctor_id: doctorId,
      secretary_id: secretaryId,
      start_time: date,
      notes: notes,
    };
    console.log(newAppointment);
    // Make a POST request to the API endpoint with the new appointment data
    fetch("http://127.0.0.1:5000/appointments/", {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(newAppointment),
    })
      .then((response) => {
        console.log(response);
        console.log("Appointment added successfully!");
        setPatientId("");
        setDoctorId("");
        setSecretaryId("");
        //setStartTime("");
        setNotes("");
      })
      .catch((error) => {
        console.error("Failed to add Appointment.", error);
      });
  };

  return (
    <div className="formAdd">
      <h2>Add Appointment</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Patient:
          <input
            type="text"
            list="patients"
            value={patientId}
            onChange={(e) => setPatientId(e.target.value)}
          />
          <datalist id="patients">
            {patients.map((patient) => (
              <option value={patient.id}>
                {patient.first_name} {patient.last_name}
              </option>
            ))}
          </datalist>
        </label>
        <br />
        <label>
          Doctor:
          <input
            type="text"
            list="doctors"
            value={doctorId}
            onChange={(e) => setDoctorId(e.target.value)}
          />
          <datalist id="doctors">
            {doctors.map((doctors) => (
              <option value={doctors.id}>
                {doctors.first_name} {doctors.last_name}
              </option>
            ))}
          </datalist>
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
          Date:
          <input
            type="datetime-local"
            value={date}
            onChange={(e) => {
              setDate(e.target.value);
              console.log(new Date(e.target.value));
            }}
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
        <button type="submit">Add Appointment</button>
      </form>
    </div>
  );
};

export default AddAppointment;
