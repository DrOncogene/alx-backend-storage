-- computes as save average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN userId INT)
BEGIN
  DECLARE average FLOAT;

  SELECT AVG(score) INTO average
  FROM corrections
  WHERE user_id = userId;

  UPDATE users
  SET average_score = average
  WHERE id = userId;
END$$

DELIMITER ;
