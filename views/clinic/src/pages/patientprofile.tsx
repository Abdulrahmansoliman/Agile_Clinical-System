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
  records: number[];
};

const PatientInfo: React.FC = () => {
  const { id } = useParams();
  const [patientInfo, setPatientInfo] = useState<Profile | null>(null);
  const [recordsList, setRecordList] = useState<number[]>([]);
  console.log("i am in patient info");

  useEffect(() => {
    // Fetch patient information
    fetch(`http://127.0.0.1:5000/patients/${id}`)
      .then((response) => response.json())
      .then((data) => {
        setPatientInfo(data.data);
      })
      .catch((error) =>
        console.error("Error fetching patient information:", error)
      );
  }, [id]);

  if (!patientInfo) {
    return <div>NO SUCH PROFILE</div>;
  }

  return (
    <div className="patient-profile">
      <h1>Patient Information</h1>
      <div className="container">
        <InfoCard patientInfo={patientInfo} />
        <RecordList
          patientID={patientInfo.id}
          recordsIDs={patientInfo.records}
        />
      </div>
    </div>
  );
};

export default PatientInfo;
