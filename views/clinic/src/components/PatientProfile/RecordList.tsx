import React, { useState, useEffect } from "react";
import RecordCard from "./RecordCard";
import RecordForm from "./RecordfForm";
import "./styles/RecordList.css";
import "./styles/RecordCard.css";

type ReportValues = {
  report_attribute_id: number;
  id: number;
  report_entity_id: number;
  report_id: number;
  value: string;
  value_name: string;
};

type Report = {
  entity_name: string;
  id: number;
  record_id: number;
  report_entity_id: number;
  values: ReportValues[];
};

export type Record = {
  id: number;
  notes: string;
  patient_profile_id: number;
  date: string;
  doctor_id: number;
  marital_status: string;
  reports: Report[];
};

export type entities = {
  id: number;
  name: string;
  attributes: {
    id: number;
    name: string;
    type: string;
  }[];
};

type RecordListProps = {
  patientID: number;
  recordsIDs: number[];
};

const RecordList: React.FC<RecordListProps> = ({ patientID, recordsIDs }) => {
  const [records, setRecords] = useState<Record[]>([]);
  const [entites, setEntities] = useState<entities[]>([]);
  const [fetchedRecordIDs, setFetchedRecordIDs] = useState(new Set());
  console.log("i am in record list");

  useEffect(() => {
    fetch(`http://127.0.0.1:5000/reports/entities`)
      .then((response) => response.json())
      .then((data) => {
        setEntities(data.data);
        //console.log(data.data);
      })
      .catch((error) => console.error("Error fetching entities:", error));
  }, []);

  useEffect(() => {
    const fetchRecords = async () => {
      const fetchedRecords: Record[] = [];
      console.log(recordsIDs.length);
      for (let i = 0; i < recordsIDs.length; i++) {
        const recordID = recordsIDs[i];
        if (fetchedRecordIDs.has(recordID)) {
          continue; // Skip fetch request if record already fetched
        }

        try {
          const response = await fetch(
            `http://127.0.0.1:5000/records/${recordID}`
          );
          const data = await response.json();
          fetchedRecords.push(data.data);
          setFetchedRecordIDs((prevIDs) => new Set(prevIDs).add(recordID)); // Add record ID to fetched set
        } catch (error) {
          console.error("Error fetching records:", error);
        }
      }

      setRecords((prevRecords) => [...prevRecords, ...fetchedRecords]);
    };

    fetchRecords();
  }, []);

  return (
    <div className="record-list">
      <div className="header">
        <h2>Records</h2>
        <RecordForm id={patientID} entities={entites} />
      </div>
      {records.length === 0 ? (
        <div className="no-records">No records found</div>
      ) : (
        <div>
          {records.map((record) => (
            <RecordCard key={record.id} record={record} entities={entites} />
          ))}
        </div>
      )}
    </div>
  );
};

export default RecordList;
