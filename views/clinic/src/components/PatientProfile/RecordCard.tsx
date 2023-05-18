import React, { useState } from "react";
import { Record } from "./RecordList";
import "./styles/RecordCard.css";

type RecordCardProps = {
  record: Record;
};
const RecordCard: React.FC<RecordCardProps> = ({ record }) => {
  const [showNotes, setShowNotes] = useState(false);
  const [showAllergies, setShowAllergies] = useState(false);
  const [showLabTests, setShowLabTests] = useState(false);
  const [showMedicalHistories, setShowMedicalHistories] = useState(false);
  const [showMedications, setShowMedications] = useState(false);
  // onDelete: () => void;

  const handleToggleNotes = () => {
    setShowNotes(!showNotes);
  };

  const handleToggleAllergies = () => {
    setShowAllergies(!showAllergies);
  };

  const handleToggleLabTests = () => {
    setShowLabTests(!showLabTests);
  };

  const handleToggleMedicalHistories = () => {
    setShowMedicalHistories(!showMedicalHistories);
  };

  const handleToggleMedications = () => {
    setShowMedications(!showMedications);
  };

  return (
    <div className="record-card">
      <div className="identify">
        <h3>Record ID: {record.id}</h3>
        <p>Date: {new Date(record.date).toLocaleDateString()}</p>
        <p>Doctor ID: {record.doctor_id}</p>
        {/* <p>Marital Status: {record.marital_status}</p> */}
      </div>

      <div className="buttons">
        <div className="buttons-blue">
          <button onClick={handleToggleNotes}>View Notes</button>
          <div className="notes-window">
            {showNotes && (
              <div className="modal">
                <div className="modal-content">
                  <h2>Notes</h2>
                  <p>{record.notes}</p>
                  <button onClick={handleToggleNotes}>Close</button>
                </div>
              </div>
            )}
          </div>

          <button onClick={handleToggleAllergies}>Allergies</button>
          <div className="notes-window">
            {showAllergies && (
              <div className="modal">
                <div className="modal-content">
                  <h2>Allergies</h2>
                  <div>
                    {record.allergies.map((allergy) => (
                      <div key={allergy.id}>
                        <p>Allergen: {allergy.allergen}</p>
                        <p>Description: {allergy.description}</p>
                        <p>Allergy ID: {allergy.id}</p>
                        <p>Name: {allergy.name}</p>
                        <p>Record ID: {allergy.record_id}</p>
                      </div>
                    ))}
                  </div>
                  <button onClick={handleToggleAllergies}>Close</button>
                </div>
              </div>
            )}
          </div>

          <button onClick={handleToggleLabTests}>Lab Test</button>
          <div className="notes-window">
            {showLabTests && (
              <div className="modal">
                <div className="modal-content">
                  <h2>Lab Test</h2>
                  <div>
                    {record.lab_tests.map((test) => (
                      <div key={test.id}>
                        <p>Date: {test.date}</p>
                        <p>Test ID: {test.id}</p>
                        <p>Name: {test.name}</p>
                        <p>Result: {test.result}</p>
                      </div>
                    ))}
                  </div>
                  <button onClick={handleToggleLabTests}>Close</button>
                </div>
              </div>
            )}
          </div>

          <button onClick={handleToggleMedicalHistories}>
            Medical Histories
          </button>
          <div className="notes-window">
            {showMedicalHistories && (
              <div className="modal">
                <div className="modal-content">
                  <h2>Medical Histories</h2>
                  <div>
                    {record.medical_histories.map((history) => (
                      <div key={history.id}>
                        <p>Date: {history.date}</p>
                        <p>History ID: {history.id}</p>
                        <p>Notes: {history.notes}</p>
                      </div>
                    ))}
                  </div>
                  <button onClick={handleToggleMedicalHistories}>Close</button>
                </div>
              </div>
            )}
          </div>

          <button onClick={handleToggleMedications}>Medications</button>
          <div className="notes-window">
            {showMedications && (
              <div className="modal">
                <div className="modal-content">
                  <h2>Medications</h2>
                  <div>
                    {record.medications.map((medication) => (
                      <div key={medication.id}>
                        <p>Date: {medication.date}</p>
                        <p>Medication ID: {medication.id}</p>
                        <p>Notes: {medication.notes}</p>
                      </div>
                    ))}
                  </div>
                  <button onClick={handleToggleMedications}>Close</button>
                </div>
              </div>
            )}
          </div>
        </div>
        <div className="buttons-red">
          {/* onClick={onDelete} */}
          <button className="delete">Delete</button>
        </div>
      </div>
    </div>
  );
};

export default RecordCard;
