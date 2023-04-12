import Menu from "../components/menu";
import AppointmentList from "../components/AppointmentList";
import "./styles/homepage.css";

function Homepage() {
  const handleMenuClick = (menu: string) => {
    console.log(`Clicked ${menu}`);
  };

  return (
    <div>
      <Menu
        onMenuClick={function (menu: string): void {
          throw new Error("Function not implemented.");
        }}
      />
      <AppointmentList />
    </div>
  );
}

export default Homepage;
