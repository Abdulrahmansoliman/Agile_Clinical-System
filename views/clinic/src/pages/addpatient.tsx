import React, { useState } from "react";

const Addpatient = () => {
  const [name, setName] = useState("");
  const [age, setAge] = useState("");

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new patient object with the input values
    const newPatient = {
      name: name,
      age: age,
    };

    // Make a POST request to the API endpoint with the new patient data
    fetch("/patients", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newPatient),
    })
      .then((response) => {
        if (response.ok) {
          console.log("Patient added successfully!");
          // Reset the form input values
          setName("");
          setAge("");
        } else {
          console.error("Failed to add patient.");
        }
      })
      .catch((error) => {
        console.error("Failed to add patient.", error);
      });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Name:
        <input
          name="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
      </label>
      <br />
      <label>
        Age:
        <input
          name="age"
          type="number"
          value={age}
          onChange={(e) => setAge(e.target.value)}
        />
      </label>
      <br />
      <button type="submit">Add Patient</button>
    </form>
  );
};

export default Addpatient;
