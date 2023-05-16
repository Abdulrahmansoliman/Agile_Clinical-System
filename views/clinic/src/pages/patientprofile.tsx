import { Link, useParams } from "react-router-dom";
import React, { useState, useEffect } from "react";
import "./styles/patientprofile.css";
import InfoCard from "../components/PatientProfile/InfoCard";
import RecordList from "../components/PatientProfile/RecordList";

type Profile = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  email: string;
  phone_number: string;
};

type Record = {
  record_date: string;
  notes: string;
};

//rewrite this part
async function fetchRecordsById(id: number): Promise<Record[]> {
  try {
    const response = await fetch(`http://127.0.0.1:5000/records/${id}`, {
      method: "GET",
    });
    const data = await response.json();
    return data.records;
  } catch (error) {
    console.error("Error fetching records:", error);
    return [];
  }
}

const PatientInfo: React.FC = () => {
  const { id } = useParams();
  const [patientInfo, setPatientInfo] = useState<Profile | null>(null);
  const [records, setRecords] = useState<Record[]>([]);

  useEffect(() => {
    // Fetch patient information
    fetch(`http://127.0.0.1:5000/patients/${id}`)
      .then((response) => response.json())
      .then((data) => setPatientInfo(data.data))
      .catch((error) =>
        console.error("Error fetching patient information:", error)
      );

    // Fetch patient records
    fetchRecordsById(Number(id))
      .then((data) => setRecords(data))
      .catch((error) => console.error("Error fetching records:", error));
  }, [id]);
  if (!patientInfo) {
    return <div>NO SUCH PROFILE</div>;
  }

  return (
    <div>
      <h1>Patient Information</h1>
      <InfoCard patientInfo={patientInfo} />
      <h2>Records</h2>
      {/*{records.length === 0 ? (
        <div>No records yet</div>
      ) : (
        <RecordList records={records} />
      )}*/}
    </div>
  );
};

export default PatientInfo;
