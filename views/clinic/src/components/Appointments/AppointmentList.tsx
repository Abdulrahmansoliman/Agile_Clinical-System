import AppointmentCard from "./AppointmentCard";
import "./styles/AppointmentList.css";
import { useState, useEffect } from "react";

type Appointment = {
  doctor_id: number;
  id: number;
  notes: string;
  patient_id: number;
  secretary_id: number;
  start_time: string; //may be edited to date type
};

//how to fetch data from patient route based on patient id
//how to fetch data from doctor route based on doctor id

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/appointments/", { method: "GET" })
      .then((response) => {
        console.log(response);
        return response.json();
      })

      .then((data) => {
        console.log(data.data);

        setAppointments(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
  }, []);
  return (
    <div>
      <h1 className="appointment-list-h1">Appointment List</h1>
      <div className="appointment-list">
        {appointments.map((appointments, index) => (
          <AppointmentCard
            key={index}
            patientId={appointments.patient_id}
            doctorId={appointments.doctor_id}
            start_date={appointments.start_time}
            notes={appointments.notes}
          />
        ))}
      </div>
    </div>
  );
}
export default AppointmentList;
