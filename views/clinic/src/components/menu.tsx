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
          Add patient
        </Link>

        <Link to="/archive" className="menu-item">
          Archive
        </Link>
        <li className="menu-item">
          <input className="search-input" type="text" placeholder="Search" />
        </li>
      </ul>
    </nav>
  );
};

export default Menu;
