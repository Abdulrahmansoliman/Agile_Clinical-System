import * as React from "react";
import { Link } from "react-router-dom";
import "./App.css";

function App() {
  return (
    <div className="container">
      <header>
        <nav>
          <ul></ul>
        </nav>
      </header>
      <main>
        <h1>Welcome to the Clinic Management System</h1>
        <p>Here you can manage your appointments, patients, and doctors.</p>
      </main>
    </div>
  );
}

export default App;
