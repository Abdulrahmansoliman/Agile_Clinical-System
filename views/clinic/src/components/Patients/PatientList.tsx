import PatientCard from "./PatientCard";
//import "./styles/AointmentList.css";
import { useState, useEffect } from "react";

type patients = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
};

function PatientList() {
  const [patients, setPatients] = useState<patients[]>([]);

  useEffect(() => {
    fetch("http://localhost:5000/patients", { method: "GET" })
      .then((response) => {
        console.log(response);
        return response.json();
      })

      .then((data) => {
        console.log(data.data);

        setPatients(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
  }, []);

  return (
    <div>
      <h1 className="appointment-list-h1">Patient List</h1>
      <div className="appointment-list">
        {patients.map((patients, index) => (
          <PatientCard
            key={index}
            id={patients.id}
            first_name={patients.first_name}
            last_name={patients.last_name}
            birth_date={patients.birth_date}
            phone_number={patients.phone_number}
            email={patients.email}
          />
        ))}
      </div>
    </div>
  );
}
export default PatientList;
