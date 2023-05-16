import RegisterItem from "../components/Items/ItemForm";
import DeleteItem from "../components/Items/DeleteItem";
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
        <DeleteItem />
      </div>
    </div>
  );
};

export default Items;
