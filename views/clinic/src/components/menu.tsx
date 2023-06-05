import React from "react";
import { Link } from "react-router-dom";
import "./styles/Menu.css";

interface MenuProps {
  onMenuClick: (menu: string) => void;
}

const Menu: React.FC<MenuProps> = ({ onMenuClick }) => {
  const handleMenuClick = (menu: string) => {
    onMenuClick(menu);
  };

  return (
    <nav className="menu">
      <ul className="menu-list">
        <Link to="/" className="menu-item">
          Appointments
        </Link>
        <Link to="/items" className="menu-item">
          Items
        </Link>
        <Link to="/addpatient" className="menu-item">
          patient
        </Link>
      </ul>
    </nav>
  );
};

export default Menu;
