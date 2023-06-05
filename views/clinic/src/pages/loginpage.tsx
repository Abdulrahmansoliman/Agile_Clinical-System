import React, { useState } from "react";
import { LoginemailForm, LoginusernameForm } from "../components/forms";
import "./styles/loginpage.css";

enum LoginState {
  email,
  username,
}

const LoginPage = () => {
  const [loginState, setLoginState] = useState(LoginState.email);

  const handleusernameClick = () => {
    setLoginState(LoginState.username);
  };

  const handleBackToemailClick = () => {
    setLoginState(LoginState.email);
  };

  return (
    <div className="login-page">
      <div className="login-form">
        {loginState === LoginState.email && (
          <LoginemailForm onusernameClick={handleusernameClick} />
        )}
        {loginState === LoginState.username && (
          <LoginusernameForm onBackToemailClick={handleBackToemailClick} />
        )}
      </div>
    </div>
  );
};

export default LoginPage;
