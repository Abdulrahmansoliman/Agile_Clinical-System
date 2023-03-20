import React from "react";
import ReactDOM from "react-dom/client";
import { Link } from "react-router-dom";
import "./index.css";

function App() {
  return (
    <div className="container">
      <header>
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/appointments">Appointments</Link>
            </li>
            <li>
              <Link to="/patients">Patients</Link>
            </li>
            <li>
              <Link to="/doctors">Doctors</Link>
            </li>
          </ul>
        </nav>
      </header>
      <main>
        <h1>Welcome to the Clinic Management System</h1>
        <p>Here you can manage your appointments, patients, and doctors.</p>
        <Link to="/appointments" className="button">
          Schedule an appointment
        </Link>
      </main>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
