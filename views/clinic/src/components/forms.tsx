import React, { useState } from "react";
import "./styles/forms.css";

interface LoginFormProps {
  onFormSubmit: (formData: { email: string; password: string }) => void;
  onForgotPasswordClick: () => void;
  onRegisterClick: () => void;
}

export const LoginForm: React.FC<LoginFormProps> = ({
  onFormSubmit,
  onForgotPasswordClick,
  onRegisterClick,
}) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Form validation and submission logic
    onFormSubmit({ email, password });
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
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button type="submit">Login</button>
      </form>
      <p>
        <button onClick={onForgotPasswordClick}>Forgot Password</button>
      </p>
      <p>
        Don't have an account?{" "}
        <button onClick={onRegisterClick}>Register</button>
      </p>
    </div>
  );
};

interface ForgotPasswordFormProps {
  onFormSubmit: (formData: { email: string }) => void;
  onBackToLoginClick: () => void;
}

export const ForgotPasswordForm: React.FC<ForgotPasswordFormProps> = ({
  onFormSubmit,
  onBackToLoginClick,
}) => {
  const [email, setEmail] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Form validation and submission logic
    onFormSubmit({ email });
  };

  return (
    <div>
      <h2>Forgot Password</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <button type="submit">Submit</button>
      </form>
      <p>
        <button onClick={onBackToLoginClick}>Back to Login</button>
      </p>
    </div>
  );
};

interface RegisterFormProps {
  onFormSubmit: (formData: { email: string; password: string }) => void;
  onBackToLoginClick: () => void;
}

export const RegisterForm: React.FC<RegisterFormProps> = ({
  onFormSubmit,
  onBackToLoginClick,
}) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    // Form validation and submission logic
    onFormSubmit({ email, password });
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <label htmlFor="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />
        <button type="submit">Register</button>
      </form>
      <p>
        <button onClick={onBackToLoginClick}>Back to Login</button>
      </p>
    </div>
  );
};

export default {
  LoginForm,
  ForgotPasswordForm,
  RegisterForm,
};
