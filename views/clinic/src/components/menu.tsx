import React from "react";
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
        <li
          className="menu-item"
          onClick={() => handleMenuClick("appointments")}
        >
          Appointments
        </li>
        <li className="menu-item" onClick={() => handleMenuClick("items")}>
          Items
        </li>
        <li
          className="menu-item"
          onClick={() => handleMenuClick("add-patients")}
        >
          Add Patients
        </li>
        <li className="menu-item" onClick={() => handleMenuClick("archive")}>
          Archive
        </li>
        <li className="menu-item">
          <input className="search-input" type="text" placeholder="Search" />
        </li>
      </ul>
    </nav>
  );
};

export default Menu;
