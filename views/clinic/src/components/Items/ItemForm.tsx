import React, { useState } from "react";
import "../styles/itemform.css";

const ItemForm = () => {
  const [itemName, setItemName] = useState("");
  const [quantity, setQuantity] = useState("");
  const [isNewItem, setIsNewItem] = useState(false);
  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new item object with the input values
    const newItem = {
      name: itemName,
      quantity: quantity,
      secretary_id: 5,
    };
    console.log(newItem);
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
        console.log(response);
        console.log("Item registered successfully!");
        // Reset the form input values
        setItemName("");
        setQuantity("");
      })
      .catch((error) => {
        console.error("Failed to register item.", error);
      });
  };

  return (
    <div>
      <button onClick={() => setIsNewItem(!isNewItem)}>Add New Item</button>
      {isNewItem && (
        <div className="containerForm">
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
            <button className="button" onClick={() => setIsNewItem(false)}>
              Cancel
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default ItemForm;
