import React, { useState } from "react";
import "../styles/itemform.css";

const AddPatientForm = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [birthDate, setBirthDate] = useState("");
  const [phoneNumber, setPhoneNumber] = useState("");
  const [email, setEmail] = useState("");

  const handleSubmit = (event: any) => {
    event.preventDefault();

    // Create a new patient object with the input values
    const newPatient = {
      first_name: firstName,
      last_name: lastName,
      birth_date: birthDate,
      phone_number: phoneNumber,
      email: email,
    };
    console.log(newPatient);
    // Make a POST request to the API endpoint with the new patient data
    fetch("http://127.0.0.1:5000/patients", {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(newPatient),
    })
      .then((response) => {
        console.log(response);
        console.log("Patient added successfully!");
        // Reset the form input values
        setFirstName("");
        setLastName("");
        setBirthDate("");
        setPhoneNumber("");
        setEmail("");
      })

      .catch((error) => {
        console.error("Failed to add patient.", error);
      });
  };

  return (
    <div className="form">
      <form onSubmit={handleSubmit}>
        <label>
          First Name:
          <input
            name="firstName"
            type="text"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </label>
        <br />
        <label>
          Last Name:
          <input
            name="lastName"
            type="text"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
          />
        </label>
        <br />
        <label>
          Birth Date:
          <input
            name="birthDate"
            type="date"
            value={birthDate}
            onChange={(e) => setBirthDate(e.target.value)}
          />
        </label>
        <br />
        <label>
          Phone Number:
          <input
            name="phoneNumber"
            type="text"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
          />
        </label>
        <br />
        <label>
          Email:
          <input
            name="email"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </label>
        <br />
        <button type="submit">Add Patient</button>
      </form>
    </div>
  );
};

export default AddPatientForm;
