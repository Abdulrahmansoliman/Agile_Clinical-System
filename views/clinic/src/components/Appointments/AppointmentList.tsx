import React, { useState, useEffect } from "react";
import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";
import { set } from "react-hook-form";

type Appointment = {
  doctor_id: number;
  id: number;
  notes: string;
  patient_id: number;
  secretary_id: number;
  start_time: string; // may be edited to date type
};
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

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [patients, setPatients] = useState<Patients[]>([]);
  const [doctors, setDoctors] = useState<Doctors[]>([]);

  const [key, setKey] = useState(0);

  const childToParent = (childdata: number) => {
    setKey((prevKey) => prevKey + 1);
  };

  const [selectedDate, setSelectedDate] = useState(
    new Date().toISOString().slice(0, 10) // Default value is today's date
  );

  useEffect(() => {
    fetch("http://127.0.0.1:5000/appointments/", {
      method: "GET",
    })
      .then((response) => response.json())
      .then((data) => {
        setAppointments(data.data);
        console.log("alppp");
        console.log(appointments);
      })
      .catch((error) => console.error("Error:", error.message));
  }, []);

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

  const handleDateChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSelectedDate(event.target.value);
  };

  const filteredAppointments = appointments.filter((appointment) => {
    const startTime = new Date(appointment.start_time);
    const selectedDay = new Date(selectedDate);
    return (
      startTime.getDate() === selectedDay.getDate() &&
      startTime.getMonth() === selectedDay.getMonth() &&
      startTime.getFullYear() === selectedDay.getFullYear()
    );
  });

  return (
    <div key={key}>
      <div className="header">
        <h1 className="appointment-list-h1">Appointment List</h1>
        <div className="appointment-filter">
          <label htmlFor="date-input">Select Date:</label>
          <input
            type="date"
            id="date-input"
            value={selectedDate}
            onChange={handleDateChange}
          />
        </div>
      </div>
      <div className="appointment-list">
        {filteredAppointments.map((appointment, index) => (
          <AppointmentCard
            key={index}
            childToParent={key}
            id={appointment.id}
            patientName={
              patients.find((patient) => patient.id === appointment.patient_id)
                ?.first_name +
              " " +
              patients.find((patient) => patient.id === appointment.patient_id)
                ?.last_name
            }
            doctorName={
              doctors.find((doctor) => doctor.id === appointment.doctor_id)
                ?.first_name +
              " " +
              doctors.find((doctor) => doctor.id === appointment.doctor_id)
                ?.last_name
            }
            patientId={appointment.patient_id}
            doctorId={appointment.doctor_id}
            start_date={appointment.start_time}
            notes={appointment.notes}
          />
        ))}
      </div>
    </div>
  );
}

export default AppointmentList;
