import React, { useState, useEffect } from "react";
import RecordCard from "./RecordCard";
import RecordForm from "./RecordfForm";
import "./styles/RecordList.css";

export type Record = {
  id: number;
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;

  allergies: {
    allergen: string;
    description: string;
    id: number;
    name: string;
    record_id: number;
  }[];

  lab_tests: {
    date: string;
    id: number;
    name: string;
    result: string;
  }[];

  medical_histories: {
    date: string;
    id: number;
    notes: string;
  }[];

  medications: {
    date: string;
    id: number;
    notes: string;
  }[];
};

type RecordListProps = {
  id: number;
};

const RecordList: React.FC<RecordListProps> = ({ id }) => {
  const [records, setRecords] = useState<Record[]>([]);
  const [showRecordForm, setShowRecordForm] = useState(false);

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/records/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setRecords([data.data]);
      })
      .catch((error) => console.error("Error fetching records:", error));
  }, [id]);

  const handleAddRecord = () => {
    setShowRecordForm(!showRecordForm);
  };

  return (
    <div className="record-list">
      <div className="header">
        <h2>Records</h2>
        <button className="add-record" onClick={handleAddRecord}>
          Add Record
        </button>
      </div>
      {showRecordForm && <RecordForm />}
      {records.length === 0 ? (
        <div className="no-records">No records found</div>
      ) : (
        <div>
          {records.map((record) => (
            <RecordCard key={record.id} record={record} />
          ))}
        </div>
      )}
    </div>
  );
};

export default RecordList;
