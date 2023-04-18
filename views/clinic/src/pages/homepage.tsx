import AppointmentList from "../components/Appointments/AppointmentList";
import "./styles/homepage.css";

function Homepage() {
  const handleMenuClick = (menu: string) => {
    console.log(`Clicked ${menu}`);
  };

  return (
    <div>
      <AppointmentList />
    </div>
  );
}

export default Homepage;
