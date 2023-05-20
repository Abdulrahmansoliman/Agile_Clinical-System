import React, { useState, useEffect } from "react";
import { DevTool } from "@hookform/devtools";
import { useForm } from "react-hook-form";
import "./styles/AddAppointment.css";
import moment from "moment";

type Patients = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
};

type Doctors = {
  id: number;
  first_name: string;
  last_name: string;
  birth_date: string;
  phone_number: string;
  email: string;
  role: string;
  specialization: string;
  username: string;
};

interface AppointmentFormData {
  patient_id: string;
  doctor_id: string;
  secretary_id: string;
  start_time: string;
  notes: string;
}

const AddAppointment: React.FC<AppointmentFormData> = () => {
  const [patients, setPatients] = useState<Patients[]>([]);
  const [Appointments, setAppointments] = useState<AppointmentFormData[]>([]); // [
  const [doctors, setDoctors] = useState<Doctors[]>([]);

  const { register, control, handleSubmit, formState, reset } =
    useForm<AppointmentFormData>();
  const { errors, isSubmitSuccessful, isSubmitting } = formState;
  useEffect(() => {
    // Fetch all patients from the API
    fetch("http://127.0.0.1:5000/patients")
      .then((response) => response.json())
      .then((data) => {
        setPatients(data.data);
      })
      .catch((error) => {
        console.error("Failed to fetch patients.", error);
      });

    // Fetch all doctors from the API
    fetch("http://127.0.0.1:5000/doctors")
      .then((response) => response.json())
      .then((data) => {
        setDoctors(data.data);
      })
      .catch((error) => {
        console.error("Failed to fetch doctors.", error);
      });

    // Fetch all appointments from the API
    fetch("http://127.0.0.1:5000/appointments")
      .then((response) => response.json())
      .then((data) => {
        setAppointments(data.data);
      });
  }, []);

  useEffect(() => {
    if (isSubmitSuccessful) {
      reset();
    }
  }, [isSubmitSuccessful, reset]);

  const onSubmit = (data: AppointmentFormData) => {
    console.log(data);
    fetch("http://127.0.0.1:5000/appointments/", {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(data),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("Success:", data);
      });
  };

  return (
    <div className="formAdd">
      <h2>Add Appointment</h2>
      <form onSubmit={handleSubmit(onSubmit)} noValidate>
        <label>
          Patient:
          <input
            id="patient_id"
            type="text"
            list="patients"
            {...register("patient_id", {
              required: { value: true, message: "Add Pateint id" },
            })}
          />
          <datalist id="patients">
            {patients.map((patient) => (
              <option value={patient.id}>
                {patient.first_name} {patient.last_name}
              </option>
            ))}
          </datalist>
          <p className="error">{errors.patient_id?.message}</p>
        </label>
        <br />
        <label>
          Doctor:
          <input
            id="doctor_id"
            type="text"
            list="doctors"
            {...register("doctor_id", {
              required: { value: true, message: "Add the doctor id" },
            })}
          />
          <datalist id="doctors">
            {doctors.map((doctors) => (
              <option value={doctors.id}>
                {doctors.first_name} {doctors.last_name}
              </option>
            ))}
          </datalist>
          <p className="error">{errors.doctor_id?.message}</p>
        </label>
        <br />
        <label>
          Secretary ID:
          <input
            id="secretary_id"
            type="text"
            {...register("secretary_id", {
              required: {
                value: true,
                message: "will be calculated by the the authentication",
              },
            })}
          />
          <p className="error">{errors.secretary_id?.message}</p>
        </label>
        <br />
        <label>
          Date:
          <input
            type="datetime-local"
            {...register("start_time", {
              required: {
                value: true,
                message: "please add the start time of the session",
              },
              validate: {
                starttimeExist: (value) => {
                  return Appointments.find(
                    (appointment) => appointment.start_time === value
                  )
                    ? "this time is already taken"
                    : true;
                },
              },
            })}
          />
          <p className="error">{errors.start_time?.message}</p>
        </label>
        <br />
        <label>
          Notes:
          <input
            id="notes"
            type="text"
            {...register("notes", {
              required: { value: true, message: "what does the patient wants" },
            })}
          />
          <p className="error">{errors.notes?.message}</p>
        </label>
        <br />
        <div className="buttonsForm">
          <button type="button" onClick={() => reset()}>
            reset
          </button>
          <button type="submit">Add Appointment</button>
        </div>
      </form>
      <DevTool control={control} />
    </div>
  );
};

export default AddAppointment;
