import React from "react";
//import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface PatientCardProps {
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
  id: number;
}

const ItemCard: React.FC<PatientCardProps> = ({
  id,
  first_name,
  last_name,
  birth_date,
  phone_number,
  email,
}) => {
  return (
    <div className="appointment-card">
      <h2>
        {first_name} {last_name}
      </h2>
      <p>id:{id}</p>
      <p>{birth_date}</p>
      <p>phone:{phone_number}</p>
      <p>email:{email}</p>
    </div>
  );
};

export default ItemCard;
