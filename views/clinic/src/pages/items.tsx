import RegisterItem from "../components/ItemForm";
import Menu from "../components/menu";
import ItemsList from "../components/ItemsList";
import PurchaseItem from "../components/PurchaseItem";
import "./styles/items.css";

const Items = () => {
  return (
    <div>
      <div className="container">
        <ItemsList />
        <RegisterItem />
        <PurchaseItem />
      </div>
    </div>
  );
};

export default Items;
