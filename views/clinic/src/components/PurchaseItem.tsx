import React, { useState } from "react";
import "./styles/itemform.css";

const PurchaseItem = () => {
  const [itemName, setItemName] = useState("");
  const [itemId, setItemId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [isFirstForm, setIsFirstForm] = useState(true);

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new item object with the input values
    const newItem = isFirstForm
      ? {
          itemName: itemName,
          quantity: quantity,
        }
      : {
          itemId: itemId,
          quantity: quantity,
        };

    // Make a POST request to the API endpoint with the new item data
    fetch("http://127.0.0.1:5000/clinicitems/", {
      method: "POST",
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
          setItemId("");
          setQuantity("");
        } else {
          console.error("Failed to register item.");
        }
      })
      .catch((error) => {
        console.error("Failed to register item.", error);
      });
  };
  return (
    <div>
      <form onSubmit={handleSubmit}>
        <p>Add existing item</p>
        <label>
          Item ID:
          <input
            name="itemId"
            type="text"
            value={itemId}
            onChange={(e) => setItemId(e.target.value)}
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
          Add
        </button>
      </form>
    </div>
  );
};

export default PurchaseItem;
