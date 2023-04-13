import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";
import { useState, useEffect } from "react";

type Appointment = {
  username: string;
  password: string;
  phone_number: string;
  specialization: string;
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
            name={appointment.username}
            phone={appointment.phone_number}
            specialization={appointment.specialization}
          />
        ))}
      </div>
    </div>
  );
}
export default AppointmentList;
