import React, { useState, useEffect } from "react";
import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";

type Appointment = {
  doctor_id: number;
  id: number;
  notes: string;
  patient_id: number;
  secretary_id: number;
  start_time: string; // may be edited to date type
};

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);

  const [selectedDate, setSelectedDate] = useState(
    new Date().toISOString().slice(0, 10) // Default value is today's date
  );

  useEffect(() => {
    fetch("http://127.0.0.1:5000/appointments/", { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        setAppointments(data.data);
        console.log("alppp");
        console.log(appointments);
      })
      .catch((error) => console.error("Error:", error.message));
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
    <div>
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
