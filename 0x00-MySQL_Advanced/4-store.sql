-- creates a trigger to decrease items quantity
-- when an order is place
DELIMITER **
CREATE TRIGGER update_quatity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END**

DELIMITER ;
