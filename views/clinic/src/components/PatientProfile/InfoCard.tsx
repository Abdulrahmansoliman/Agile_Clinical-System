import { Link, useParams } from "react-router-dom";
import React, { useState, useEffect } from "react";
import "./styles/InfoCard.css";

type Profile = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  email: string;
  phone_number: string;
};

interface InfoCardProps {
  patientInfo: Profile;
}

const InfoCard: React.FC<InfoCardProps> = ({ patientInfo }) => {
  return (
    <div className="personal-info">
      <h1>
        {patientInfo.first_name} {patientInfo.last_name}
      </h1>
      <h2>Birth Date:</h2>
      <p>{patientInfo.birth_date.slice(0, 17)}</p>
      <h2>Email:</h2>
      <p>{patientInfo.email}</p>
      <h2>Phone Number:</h2>
      <p>{patientInfo.phone_number}</p>
    </div>
  );
};

export default InfoCard;
