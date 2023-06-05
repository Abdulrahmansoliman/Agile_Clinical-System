import React, { useState } from "react";
import { useForm, useFieldArray } from "react-hook-form";
import "../styles/itemform.css";

const PurchaseItem = () => {
  const [itemId, setItemId] = useState("");
  const [quantity, setQuantity] = useState("");
  const [isPurshase, setIsPurchase] = useState(false);

  const handleSubmit = (event: any) => {
    event.preventDefault();

    fetch(`http://127.0.0.1:5000/clinicitems/${itemId}`, {
      method: "GET",
    }).then(async (data) => {
      console.log(data);
      let myitem = (await data.json()).clinicitem;
      myitem.quantity = myitem.quantity - parseInt(quantity);
      console.log(myitem);
      // Make a POST request to the API endpoint with the new item data
      fetch(`http://127.0.0.1:5000/clinicitems/${itemId}`, {
        method: "PATCH",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: myitem.name,
          quantity: myitem.quantity,
          secretary_id: myitem.secretary_id,
        }),
      })
        .then((response) => {
          if (response.ok) {
            // Reset the form input values
            setItemId("");
            setQuantity("");
          } else {
            console.error("Failed to purchase item.");
          }
        })
        .catch((error) => {
          console.error("Failed to purchase item.", error);
        });
    });

    // Create a new item object with the input values
  };
  return (
    <div className="itemform">
      <button className="button" onClick={() => setIsPurchase(!isPurshase)}>
        Purchase Item
      </button>
      {isPurshase && (
        <div className="containerForm">
          <form onSubmit={handleSubmit}>
            <p>Purchase Item</p>
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
              Purchase
            </button>
            <button className="button" onClick={() => setIsPurchase(false)}>
              cancel
            </button>
          </form>
        </div>
      )}
    </div>
  );
};

export default PurchaseItem;
