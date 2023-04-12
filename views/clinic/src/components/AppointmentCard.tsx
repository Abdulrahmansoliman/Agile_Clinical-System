import React from "react";
import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  name: string;
  time: string;
}

const AppointmentCard: React.FC<AppointmentCardProps> = ({ name, time }) => {
  return (
    <div className="appointment-card">
      <h2>{name}</h2>
      <p>{time}</p>
    </div>
  );
};

export default AppointmentCard;
