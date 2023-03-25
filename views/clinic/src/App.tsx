import Menu from "./components/menu";
import AppointmentList from "./components/AppointmentList";
import "./App.css";

function App() {
  const appointments = [
    { name: "John Doe", time: "9:00am" },
    { name: "Jane Smith", time: "10:30am" },
    { name: "Bob Johnson", time: "2:00pm" },
    { name: "peter", time: "9:00am" },
    { name: "khelo", time: "9:00am" },
    { name: "kamsor", time: "9:00am" },
    { name: "kamsor", time: "9:00am" },
    { name: "kamsor", time: "9:00am" },
    { name: "kamsor", time: "9:00am" },
  ];

  const handleMenuClick = (menu: string) => {
    console.log(`Clicked ${menu}`);
  };

  return (
    <div>
      <Menu onMenuClick={handleMenuClick} />
      <AppointmentList appointments={appointments} />
    </div>
  );
}

export default App;
