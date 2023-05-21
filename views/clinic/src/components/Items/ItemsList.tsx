import ItemCard from "./ItemCard";
import RegisterItem from "./ItemForm";
import PurchaseItem from "./PurchaseItem";
import { useState, useEffect } from "react";
import "./styles/Itemlist.css";

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
      .then((response) => {
        console.log(response);
        return response.json();
      })

      .then((data) => {
        console.log(data.data);

        setItems(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
  }, []);

  return (
    <div>
      <div className="itemheader">
        <h1>Items List</h1>
        <RegisterItem />
        <PurchaseItem />
      </div>
      <div className="Item-list">
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
