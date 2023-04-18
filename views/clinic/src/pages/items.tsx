import RegisterItem from "../components/Items/ItemForm";
import Menu from "../components/menu";
import ItemsList from "../components/Items/ItemsList";
import PurchaseItem from "../components/Items/PurchaseItem";
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
