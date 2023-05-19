import React, { useState } from "react";
import "./styles/AppointmentCard.css";
import { Link } from "react-router-dom";

interface AppointmentCardProps {
  id: number;
  patientId: number;
  patientName: string;
  doctorName: string;
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
  id,
  patientName,
  doctorName,
  patientId,
  doctorId,
  start_date,
  notes,
}) => {
  const handleDelete = () => {
    fetch(`http://127.0.0.1:5000/appointments/${id}`, {
      method: "DELETE",
    });
  };
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
      <div>
        <h2 className="identify">{patientName}</h2>
        <p>{doctorName}</p>
      </div>
      <p>Date: {formattedDate}</p>
      <div className="buttons">
        <div className="button-blue">
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
          <Link to={`/profile/${patientId}`}>
            <button>Profile</button>
          </Link>
        </div>
        <button onClick={handleDelete} className="button-red">
          Delete
        </button>
      </div>
    </div>
  );
};

export default AppointmentCard;
