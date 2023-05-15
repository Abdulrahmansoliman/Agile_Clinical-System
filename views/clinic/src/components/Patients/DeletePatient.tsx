import React, { useState } from "react";
import "../styles/itemform.css";

const DeletePatient = () => {
  const [patient_id, setPatient_id] = useState("");

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Make a POST request to the API endpoint with the new item data
    fetch(`http://127.0.0.1:5000/patients/${patient_id}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (response.ok) {
          // Reset the form input values
          setPatient_id("");
        } else {
          console.error("Failed to purchase item.");
        }
      })
      .catch((error) => {
        console.error("Failed to purchase item.", error);
      });
  };
  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <p>Delete patient</p>
        <label>
          Item ID:
          <input
            name="ItemId"
            type="text"
            value={patient_id}
            onChange={(e) => setPatient_id(e.target.value)}
            className="input"
          />
        </label>
        <br />
        <button type="submit" className="button">
          Delete
        </button>
      </form>
    </div>
  );
};
export default DeletePatient;
