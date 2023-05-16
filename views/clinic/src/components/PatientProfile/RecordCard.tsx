import React, { useState } from "react";
//import "./styles/RecordCard.css";

interface RecordCardProps {
  recordDate: string; // may be edited to date type
  notes: string;
}

const RecordCard: React.FC<RecordCardProps> = ({ recordDate, notes }) => {
  const [isExpanded, setIsExpanded] = useState(false);

  const handleToggle = () => {
    setIsExpanded(!isExpanded);
  };

  return (
    <div
      className={`record-card ${isExpanded ? "expanded" : ""}`}
      onClick={handleToggle}
    >
      <h2>Record Date: {recordDate}</h2>
      {isExpanded && <p>Notes: {notes}</p>}
    </div>
  );
};

export default RecordCard;
