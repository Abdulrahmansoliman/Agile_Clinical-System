import React from "react";
import "../styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  patientId: number;
  doctorId: number;
  start_date: string; // may be edited to date type
  notes: string;
}

const AppointmentCard: React.FC<AppointmentCardProps> = ({
  patientId,
  doctorId,
  start_date,
  notes,
}) => {
  const formattedDate = new Date(start_date).toLocaleString();
  console.log(start_date);
  console.log(formattedDate);
  console.log("peter");
  return (
    <div className="appointment-card">
      <h2>Patient ID: {patientId}</h2>
      <p>Doctor ID: {doctorId}</p>
      <p>Date: {formattedDate}</p>
      <p>Notes: {notes} </p>
    </div>
  );
};

export default AppointmentCard;
