import React from "react";
import "./styles/ProfileCard.css";
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
  const handleDelete = () => {
    fetch(`http://127.0.0.1:5000/patients/${id}`, {
      method: "DELETE",
    });
  };

  return (
    <div className="patient-card">
      <div className="patient-card-header">
        <h3>
          {first_name} {last_name}
        </h3>
        <p>id:{id}</p>
      </div>
      <p>{birth_date.slice(0, 16)}</p>
      <div className="patient-card-contacts">
        <p>phone:{phone_number}</p>
        <p>email:{email}</p>
      </div>
      <div className="patient-card-buttons">
        <Link to={`/profile/${id}`}>
          <button className="profile-button">profile</button>
        </Link>
        <button className="delete-button">delete</button>
      </div>
    </div>
  );
};

export default ItemCard;
