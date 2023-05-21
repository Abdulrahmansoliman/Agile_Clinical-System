import React from "react";
import "./styles/ItemCard.css";
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
  const handleDelete = () => {
    fetch(`http://127.0.0.1:5000/clinicitems/${id}`, {
      method: "DELETE",
    });
  };

  return (
    <div className="item-card">
      <h2>{name}</h2>
      <p>id : {id}</p>
      <p>qunatity : {quantity} </p>
      <button onClick={handleDelete}>delete</button>
    </div>
  );
};

export default ItemCard;
