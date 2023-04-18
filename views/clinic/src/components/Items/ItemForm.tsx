import React, { useState } from "react";
import "../styles/itemform.css";

const ItemForm = () => {
  const [itemName, setItemName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [price, setPrice] = useState("");

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new item object with the input values
    const newItem = {
      itemName: itemName,
      quantity: quantity,
      price: price,
    };

    // Make a POST request to the API endpoint with the new item data
    fetch("http://127.0.0.1:5000/clinicitems/", {
      method: "POST",
      mode: "no-cors",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newItem),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Item registered successfully!");
          // Reset the form input values
          setItemName("");
          setQuantity("");
          setPrice("");
        } else {
          console.error("Failed to register item.");
        }
      })
      .catch((error) => {
        console.error("Failed to register item.", error);
      });
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <p>Add New item</p>
        <label>
          Item name:
          <input
            name="itemName"
            type="text"
            value={itemName}
            onChange={(e) => setItemName(e.target.value)}
            className="input"
          />
        </label>
        <br />
        <label>
          Quantity:
          <input
            name="quantity"
            type="number"
            value={quantity}
            onChange={(e) => setQuantity(e.target.value)}
            className="input"
          />
        </label>
        <br />
        <button type="submit" className="button">
          Register Item
        </button>
      </form>
    </div>
  );
};

export default ItemForm;
