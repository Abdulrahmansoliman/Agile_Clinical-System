import React, { useState } from "react";
import {
  LoginForm,
  ForgotPasswordForm,
  RegisterForm,
} from "../components/forms";
import "./styles/loginpage.css";

enum LoginState {
  LOGIN,
  FORGOT_PASSWORD,
  REGISTER,
}

const LoginPage = () => {
  const [loginState, setLoginState] = useState(LoginState.LOGIN);

  const handleForgotPasswordClick = () => {
    setLoginState(LoginState.FORGOT_PASSWORD);
  };

  const handleRegisterClick = () => {
    setLoginState(LoginState.REGISTER);
  };

  const handleBackToLoginClick = () => {
    setLoginState(LoginState.LOGIN);
  };

  return (
    <div className="login-page">
      <div className="login-form">
        {loginState === LoginState.LOGIN && (
          <LoginForm
            onForgotPasswordClick={handleForgotPasswordClick}
            onRegisterClick={handleRegisterClick}
            onFormSubmit={(formData: { email: string; password: string }) => {
              throw new Error("Function not implemented.");
            }}
          />
        )}
        {loginState === LoginState.FORGOT_PASSWORD && (
          <ForgotPasswordForm
            onBackToLoginClick={handleBackToLoginClick}
            onFormSubmit={(formData: { email: string }) => {
              throw new Error("Function not implemented.");
            }}
          />
        )}
        {loginState === LoginState.REGISTER && (
          <RegisterForm
            onBackToLoginClick={handleBackToLoginClick}
            onFormSubmit={(formData: { email: string; password: string }) => {
              throw new Error("Function not implemented.");
            }}
          />
        )}
      </div>
    </div>
  );
};
export default LoginPage;
