-- creates a view
CREATE OR REPLACE VIEW need_meeting
AS
SELECT name from students
WHERE score < 80 AND
  (ISNULL(last_meeting) OR
    TIMESTAMPDIFF(MONTH, last_meeting, NOW()) > 1);
