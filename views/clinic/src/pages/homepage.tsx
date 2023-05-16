import AppointmentList from "../components/Appointments/AppointmentList";
import AddAppointment from "../components/Appointments/AddAppointment";
import "./styles/homepage.css";

function Homepage() {
  const handleMenuClick = (menu: string) => {
    console.log(`Clicked ${menu}`);
  };

  return (
    <div className="container">
      <div className="component-container">
        <AddAppointment />
        <AppointmentList />
      </div>
    </div>
  );
}

export default Homepage;
