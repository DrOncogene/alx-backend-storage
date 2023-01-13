-- trigger to reset valid_email column
DELIMITER $$

CREATE TRIGGER reset_valid_email
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
  IF OLD.email != NEW.email THEN
    SET NEW.valid_email = 0;
  END IF;
END$$

DELIMITER ;
