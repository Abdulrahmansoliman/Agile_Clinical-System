import Menu from "./components/menu";
import AppointmentList from "./components/AppointmentList";
import "./App.css";
//import { Switch, Route } from "react-router-dom";

function App() {
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

      {/* <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/appointments" component={Appointments} />
        <Route path="/items" component={Items} />
        <Route path="/patients/add" component={AddPatient} />
        <Route path="/patients/:id" component={PatientProfile} />
        <Route path="/archive" component={Archive} />
        <Route component={NotFound} />
      </Switch> */}
    </div>
  );
}

export default App;
