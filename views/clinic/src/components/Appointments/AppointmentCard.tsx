import React from "react";
import "../styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  id: number;
  name: string;
  doctor: string;
  date: Date; // may be edited to date type
  notes: string;
}

const AppointmentCard: React.FC<AppointmentCardProps> = ({
  id,
  name,
  doctor,
  date,
  notes,
}) => {
  return (
    <div className="appointment-card">
      <h2>
        {id}: {name}
      </h2>
      <p>{doctor}</p>
      <p>{date.toISOString()}</p>
      <p>{notes} </p>
      <Link to={`/patient/${id}`}>Profile</Link>
    </div>
  );
};

export default AppointmentCard;
