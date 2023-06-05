import React, { useState } from "react";
import { Record, entities } from "./RecordList";
import "./styles/RecordCard.css";

type Entity = {
  id: number;
  name: string;
  attributes: {
    id: number;
    name: string;
    type: string;
  }[];
};

type RecordCardProps = {
  record: Record;
  entities: Entity[];
};

const RecordCard: React.FC<RecordCardProps> = ({ record, entities }) => {
  const [showNotes, setShowNotes] = useState(false);

  const reports = record.reports;

  const entitiesMap = new Map<string, Entity>();

  for (const entity of entities) {
    entitiesMap.set(entity.name, entity);
  }

  const onDelete = () => {
    fetch(`http://127.0.0.1:5000/records/${record.id}`, {
      method: "DELETE",
    });
  };

  const handleToggleNotes = () => {
    setShowNotes(!showNotes);
  };

  return (
    <div className="record-card">
      <div className="identify">
        <h3>Record ID: {record.id}</h3>
        <p>Date: {new Date(record.date).toLocaleDateString()}</p>
        <p>Doctor ID: {record.doctor_id}</p>
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
                  <p>Marital Status: {record.marital_status}</p>

                  {reports.map((report) => {
                    const entity = entitiesMap.get(report.entity_name);
                    if (!entity) return null;
                    return (
                      <div key={entity.id}>
                        <h3>{entity.name}</h3>
                        {report.values.map((value) => (
                          <p key={value.id}>
                            {value.value_name}: {value.value}
                          </p>
                        ))}
                      </div>
                    );
                  })}

                  <button onClick={handleToggleNotes}>Close</button>
                </div>
              </div>
            )}
          </div>
        </div>
        <div className="buttons-red">
          <button onClick={onDelete} className="delete">
            Delete
          </button>
        </div>
      </div>
    </div>
  );
};

export default RecordCard;
