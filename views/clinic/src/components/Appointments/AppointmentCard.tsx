import React, { useState } from "react";
import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  patientId: number;
  doctorId: number;
  start_date: string; // may be edited to date type
  notes: string;
}

const NotesWindow: React.FC<{ notes: string }> = ({ notes }) => {
  const [isOpen, setIsOpen] = useState(false);

  const handleToggle = () => {
    setIsOpen(!isOpen);
  };

  return (
    <div>
      <button onClick={handleToggle}>View Notes</button>
      <div className="notes-window">
        {isOpen && (
          <div className="modal">
            <div className="modal-content">
              <h2>Notes</h2>
              <p>{notes}</p>
              <button onClick={handleToggle}>Close</button>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

const AppointmentCard: React.FC<AppointmentCardProps> = ({
  patientId,
  doctorId,
  start_date,
  notes,
}) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const handleModalOpen = () => {
    setIsModalOpen(true);
  };

  const handleModalClose = () => {
    setIsModalOpen(false);
  };

  const formattedDate = new Date(start_date).toLocaleString();
  console.log(start_date);
  console.log(formattedDate);
  console.log("peter");
  return (
    <div className="appointment-card">
      <h2>Patient ID: {patientId}</h2>
      <p>Doctor ID: {doctorId}</p>
      <p>Date: {formattedDate}</p>
      <NotesWindow notes={notes} />
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <h2>Notes</h2>
            <p>{notes}</p>
            <button onClick={handleModalClose}>Close</button>
          </div>
        </div>
      )}
      <Link to={`/addpatient`}>
        <button>Profile</button>
      </Link>
    </div>
  );
};

export default AppointmentCard;
