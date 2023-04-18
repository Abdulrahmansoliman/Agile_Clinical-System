import Homepage from "./pages/homepage";
import Loginpage from "./pages/loginpage";
import Patient from "./pages/patient";
import Items from "./pages/items";
import Menu from "./components/menu";
import Footer from "./components/footer";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Menu
        onMenuClick={function (menu: string): void {
          throw new Error("Function not implemented.");
        }}
      />
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Loginpage />} />
        <Route path="/addpatient" element={<Patient />} />
        <Route path="/items" element={<Items />} />
        <Route path="*" element={<h1>404: Not Found</h1>} />
      </Routes>
      <Footer />
    </BrowserRouter>
  );
}

export default App;
