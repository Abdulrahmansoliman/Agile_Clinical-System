import React from "react";
import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  name: string;
  phone: string;
  specialization: string;
}

const AppointmentCard: React.FC<AppointmentCardProps> = ({
  name,
  phone,
  specialization,
}) => {
  return (
    <div className="appointment-card">
      <h2>{name}</h2>
      <p>{phone}</p>
      <p>{specialization} </p>
    </div>
  );
};

export default AppointmentCard;
