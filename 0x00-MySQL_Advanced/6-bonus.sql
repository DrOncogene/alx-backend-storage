-- stored procedure to add a new correction
DELIMITER $$
CREATE PROCEDURE AddBonus(
	IN user_id INT,
	IN proj_name VARCHAR(255),
	IN score FLOAT)
BEGIN
  DECLARE exist INT;
  DECLARE proj_id INT;
  SELECT COUNT(*) INTO exist
  FROM projects
  WHERE name = proj_name;

  IF exist = 0 THEN
    INSERT INTO projects (name)
    VALUES (proj_name);
  END IF;

  SELECT id INTO proj_id
  FROM projects
  WHERE name = proj_name;

  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, proj_id, score);
END$$

DELIMITER ;
