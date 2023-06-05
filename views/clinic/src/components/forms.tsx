import React, { useState } from "react";
import "./styles/forms.css";

interface LoginFormProps {
  onusernameClick: () => void;
}

export const LoginemailForm = ({ onusernameClick }: LoginFormProps) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [emailError, setEmailError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  let usertype = "email";

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Form validation
    if (!email) {
      setEmailError("Email is required");
    } else {
      setEmailError("");
    }

    if (!password) {
      setPasswordError("Password is required");
    } else {
      setPasswordError("");
    }

    // Check if there are no errors before submitting the form
    if (email && password) {
      sendFormRequest({ usertype, email, password });
    }
  };

  const sendFormRequest = (formData: {
    usertype: string;
    email: string;
    password: string;
  }) => {
    console.log(formData);
    fetch(`http://127.0.0.1:5000/auth/login`, {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response data
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error(error);
      });
  };

  const handleusernameClick = () => {
    onusernameClick();
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        {emailError && <p className="error">{emailError}</p>}
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {passwordError && <p className="error">{passwordError}</p>}
        <button type="submit">Login</button>
      </form>
      <p>
        login with username?{" "}
        <button onClick={handleusernameClick}>username</button>
      </p>
    </div>
  );
};

interface RegisterFormProps {
  onBackToemailClick: () => void;
}

export const LoginusernameForm = ({
  onBackToemailClick,
}: RegisterFormProps) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [usernameError, setUsernameError] = useState("");
  const [passwordError, setPasswordError] = useState("");
  let userType = "username"; // Change variable name to 'userType'

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    // Form validation
    if (!username) {
      // Change 'email' to 'username'
      setUsernameError("Username is required"); // Change error message
    } else {
      setUsernameError("");
    }

    if (!password) {
      setPasswordError("Password is required");
    } else {
      setPasswordError("");
    }

    // Check if there are no errors before submitting the form
    if (username && password) {
      // Change 'email' to 'username'
      sendFormRequest({ userType, username, password }); // Change 'usertype' to 'userType'
    }
  };

  const sendFormRequest = (formData: {
    userType: string; // Change field name to 'userType'
    username: string; // Change field name to 'username'
    password: string;
  }) => {
    console.log(formData);
    fetch(`http://127.0.0.1:5000/auth/login`, {
      method: "POST",
      mode: "no-cors",
      body: JSON.stringify(formData),
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response data
        console.log(data);
      })
      .catch((error) => {
        // Handle any errors
        console.error(error);
      });
  };

  const handleBackToemailClick = () => {
    // Change function name to 'handleUsernameClick'
    onBackToemailClick();
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="username">Username:</label>{" "}
        {/* Change 'email' to 'username' */}
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        {usernameError && <p className="error">{usernameError}</p>}{" "}
        {/* Change variable name */}
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {passwordError && <p className="error">{passwordError}</p>}
        <button type="submit">Login</button>
      </form>
      <p>
        Login with email?{" "}
        <button onClick={handleBackToemailClick}>Email</button>{" "}
      </p>
    </div>
  );
};

export default {
  LoginemailForm,
  LoginusernameForm,
};
