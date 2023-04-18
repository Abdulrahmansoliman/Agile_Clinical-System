import ItemCard from "./ItemCard";
//import "./styles/AointmentList.css";
import { useState, useEffect } from "react";

type Items = {
  id: number;
  name: string;
  quantity: number;
  secretary_id: number;
};

function ItemsList() {
  const [items, setItems] = useState<Items[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/clinicitems", { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.data);

        setItems(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
  }, []);

  return (
    <div>
      <h1 className="appointment-list-h1">Items List</h1>
      <div className="appointment-list">
        {items.map((item, index) => (
          <ItemCard
            key={index}
            name={item.name}
            id={item.id}
            quantity={item.quantity}
            secretary_id={item.secretary_id}
          />
        ))}
      </div>
    </div>
  );
}
export default ItemsList;
