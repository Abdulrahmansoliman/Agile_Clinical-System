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
      <h2>Personal Information</h2>
      <p>
        Name: {patientInfo.first_name} {patientInfo.last_name}
      </p>
      <p>Birth Date: {patientInfo.birth_date}</p>
      <p>Email: {patientInfo.email}</p>
      <p>Phone Number: {patientInfo.phone_number}</p>
    </div>
  );
};

export default InfoCard;
