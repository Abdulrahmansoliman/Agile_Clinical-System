import React from "react";
import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";

interface Appointment {
  name: string;
  time: string;
}

interface AppointmentListProps {
  appointments: Appointment[];
}

const AppointmentList: React.FC<AppointmentListProps> = ({ appointments }) => {
  return (
    <div>
      <h1>Appointment List</h1>
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
};

export default AppointmentList;
