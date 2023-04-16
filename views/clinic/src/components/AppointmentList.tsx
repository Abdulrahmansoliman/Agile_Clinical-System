import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";
import { useState, useEffect } from "react";

type Appointment = {
  birth_date: string;
  email: string;
  first_name: string;
  id: string;
  last_name: string;
  phone_number: string;
  role: string;
  specialization: string;
  username: string;
};

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/", { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.data);

        setAppointments(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
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
