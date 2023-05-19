import React, { useState } from "react";

interface RecordFormProps {}

interface Allergy {
  allergen: string;
  description: string;
  id: number;
  name: string;
  record_id: number;
}

interface LabTest {
  date: string;
  id: number;
  name: string;
  result: string;
}

interface MedicalHistory {
  date: string;
  id: number;
  notes: string;
}

interface Medication {
  date: string;
  id: number;
  notes: string;
}

interface RecordFormData {
  id: number;
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;
  allergies: Allergy[];
  lab_tests: LabTest[];
  medical_histories: MedicalHistory[];
  medications: Medication[];
}

const RecordForm: React.FC<RecordFormProps> = () => {
  const [openForm, setopenForm] = useState(false);

  const [formData, setFormData] = useState<RecordFormData>({
    id: 0,
    notes: "",
    patient_profile_id: 0,
    date: "",
    doctor_id: 0,
    marital_status: "",
    allergies: [],
    lab_tests: [],
    medical_histories: [],
    medications: [],
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    fetch(`http://127.0.0.1:5000/records`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Call the onSubmit callback with the form data
        // Reset the form after submission
        setFormData({
          id: 0,
          notes: "",
          patient_profile_id: 0,
          date: "",
          doctor_id: 0,
          marital_status: "",
          allergies: [],
          lab_tests: [],
          medical_histories: [],
          medications: [],
        });
      })
      .catch((error) => console.error("Error submitting record:", error));
  };

  return (
    <div className="record-form">
      <h2>Add Record</h2>
      <form onSubmit={handleSubmit}>
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default RecordForm;
