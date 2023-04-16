import Homepage from "./pages/homepage";
import Loginpage from "./pages/loginpage";
import Addpatient from "./pages/addpatient";
import Items from "./pages/items";
import "./App.css";
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/login" element={<Loginpage />} />
        <Route path="/addpatient" element={<Addpatient />} />
        <Route path="/items" element={<Items />} />
        <Route path="*" element={<h1>404: Not Found</h1>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
