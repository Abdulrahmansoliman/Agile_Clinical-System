import PatientCard from "./PatientCard";
import AddPatientForm from "./AddPatientForm";
import "./styles/PatientList.css";
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
  const [searchQuery, setSearchQuery] = useState("");

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

  const handleSearch = (query: string) => {
    setSearchQuery(query);
  };

  const filteredpatient = patients.filter((patient) =>
    patient.first_name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div>
      <div className="patientheader">
        <h1 className="appointment-list-h1">Patient List</h1>
        <input
          type="text"
          value={searchQuery}
          onChange={(e) => handleSearch(e.target.value)}
          placeholder="Search items..."
        />
        <div className="buttons">
          <AddPatientForm />
        </div>
      </div>
      <div className="patient-list">
        {filteredpatient.map((patients, index) => (
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
