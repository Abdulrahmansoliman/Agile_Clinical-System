import React, { useState, useEffect } from "react";
import ItemCard from "./ItemCard";
import RegisterItem from "./ItemForm";
import PurchaseItem from "./PurchaseItem";
import "./styles/Itemlist.css";

type Items = {
  id: number;
  name: string;
  quantity: number;
  secretary_id: number;
};

function ItemsList() {
  const [items, setItems] = useState<Items[]>([]);
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    fetch("http://localhost:5000/clinicitems", { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        setItems(data.data);
      })
      .catch((error) => console.error("Error fetching items:", error));
  }, []);

  const handleSearch = (query: string) => {
    setSearchQuery(query);
  };

  const filteredItems = items.filter((item) =>
    item.name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <div className="itemheader">
        <h1>Items List</h1>
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => handleSearch(e.target.value)}
          placeholder="Search items..."
        />
        <div className="buttons">
          <RegisterItem />
          <PurchaseItem />
        </div>
      </div>
      <div className="Item-list">
        {filteredItems.map((item, index) => (
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
