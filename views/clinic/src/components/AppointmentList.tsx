import React from "react";
import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";
import { useState, useEffect } from "react";

type Appointment = {
  name: string;
  time: string;
};

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);

  useEffect(() => {
    fetch("../comunicate/appointments.json")
      .then((response) => response.json())
      .then((data) => setAppointments(data))
      .catch((error) => console.error(error));
  }, []);

  return (
    <div>
      <h1 className="appointment-list-h1">Appointment List</h1>
      <div className="appointment-list">
        {appointments.map((appointment, index) => (
          <AppointmentCard
            key={index}
            name={appointment.name}
            time={appointment.time}
          />
        ))}
      </div>
    </div>
  );
}
export default AppointmentList;
