import AppointmentCard from "./AppointmentCard";
import "../styles/AppointmentList.css";
import { useState, useEffect } from "react";

type Appointment = {
  patient_id: number;
  doctor_id: number;
  secretary_id: number;
  date: Date; //may be edited to date type
  notes: string;
};

type Patient = {
  birth_date: Date;
  email: string;
  first_name: string;
  last_name: string;
  phone_number: string;
};

type Doctor = {
  birth_date: Date;
  email: string;
  first_name: string;
  id: number;
  last_name: string;
  phone_number: string;
  role: string;
  specialization: string;
  username: string;
};

//how to fetch data from patient route based on patient id
//how to fetch data from doctor route based on doctor id

function AppointmentList() {
  const [appointments, setAppointments] = useState<Appointment[]>([]);
  const [patients, setPatients] = useState<Record<number, Patient>>({});
  const [doctors, setDoctors] = useState<Record<number, Doctor>>({});

  useEffect(() => {
    fetch("http://localhost:5000/Appointments", { method: "GET" })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.data);

        setAppointments(data.data);
      })
      .catch((error) => console.error("alooooooooo", error.message));
  }, []);

  useEffect(() => {
    const patientIds = appointments.map(
      (appointment) => appointment.patient_id
    );
    const fetchPatients = async () => {
      const responses = await Promise.all(
        patientIds.map((patientId) =>
          fetch(`http://localhost:5000/patients/${patientId}`)
        )
      );
      const patientData = await Promise.all(
        responses.map((response) => response.json())
      );
      const patients = patientData.reduce((acc, patient) => {
        acc[patient.data.id] = patient.data;
        return acc;
      }, {} as Record<number, Patient>);
      setPatients((prevPatients) => ({ ...prevPatients, ...patients }));
    };
    fetchPatients();
  }, [appointments]);

  useEffect(() => {
    const doctorIds = appointments.map((appointment) => appointment.doctor_id);
    const fetchDoctors = async () => {
      const responses = await Promise.all(
        doctorIds.map((doctorId) =>
          fetch(`http://localhost:5000/doctors/${doctorId}`)
        )
      );
      const doctorData = await Promise.all(
        responses.map((response) => response.json())
      );
      const doctors = doctorData.reduce((acc, doctor) => {
        acc[doctor.data.id] = doctor.data;
        return acc;
      }, {} as Record<number, Doctor>);
      setDoctors((prevDoctors) => ({ ...prevDoctors, ...doctors }));
    };
    fetchDoctors();
  }, [appointments]);

  return (
    <div>
      <h1 className="appointment-list-h1">Appointment List</h1>
      <div className="appointment-list">
        {appointments.map((appointment, index) => (
          <AppointmentCard
            key={index}
            id={appointment.patient_id}
            name={
              patients[appointment.patient_id]?.first_name +
              " " +
              patients[appointment.patient_id]?.last_name
            }
            doctor={doctors[appointment.doctor_id]?.first_name}
            date={appointment.date}
            notes={appointment.notes}
          />
        ))}
      </div>
    </div>
  );
}
export default AppointmentList;
