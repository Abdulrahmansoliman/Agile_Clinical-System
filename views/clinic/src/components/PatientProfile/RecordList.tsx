import React, { useState, useEffect } from "react";
import RecordCard from "./RecordCard";
import "./styles/RecordList.css";

const dummyData = [
  {
    recordDate: "2023-05-01",
    notes: "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  },
  {
    recordDate: "2023-05-02",
    notes: "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
  },
  {
    recordDate: "2023-05-03",
    notes:
      "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
  },
];

type Record = {
  record_date: string;
  notes: string;
};

interface RecordListProps {
  records: Record[];
}

const RecordList: React.FC<RecordListProps> = ({ records }) => {
  return (
    <div>
      <h2>Records</h2>
      {records.map((records, index) => (
        <RecordCard
          key={index}
          recordDate={records.record_date}
          notes={records.notes}
        />
      ))}
    </div>
  );
};

export default RecordList;
