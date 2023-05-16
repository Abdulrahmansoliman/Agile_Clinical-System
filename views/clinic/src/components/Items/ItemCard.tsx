import React from "react";
//import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface ItemCardProps {
  id: number;
  name: string;
  quantity: number;
  secretary_id: number;
}

const ItemCard: React.FC<ItemCardProps> = ({
  id,
  name,
  quantity,
  secretary_id,
}) => {
  return (
    <div className="appointment-card">
      <h2>{name}</h2>
      <p>id : {id}</p>
      <p>qunatity : {quantity} </p>
    </div>
  );
};

export default ItemCard;
