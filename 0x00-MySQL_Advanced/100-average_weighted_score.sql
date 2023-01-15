-- computes as save average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN userId INT)
BEGIN
  DECLARE weighted_average FLOAT DEFAULT 0.0;
  DECLARE total_weight INT DEFAULT 0;
  DECLARE proj_weight INT;
  DECLARE curr_id INT;
  DECLARE curr_score INT DEFAULT 0;
  DECLARE done INT DEFAULT 0;

  DECLARE user_corrections CURSOR FOR
  SELECT project_id, score FROM corrections
  WHERE user_id = userId;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

  OPEN user_corrections;
  calc: LOOP
    FETCH user_corrections INTO curr_id, curr_score;
    IF done = 1 THEN
      LEAVE calc;
    END IF;
    SELECT weight INTO proj_weight
    FROM projects WHERE id = curr_id;

    SET total_weight = total_weight + proj_weight;
    SET weighted_average = weighted_average + (curr_score * proj_weight);
  END LOOP calc;
  CLOSE user_corrections;

  SET weighted_average = weighted_average / total_weight;

  UPDATE users
  SET average_score = weighted_average
  WHERE id = userId;
END$$

DELIMITER ;
