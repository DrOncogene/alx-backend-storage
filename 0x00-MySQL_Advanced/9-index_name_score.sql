-- creates an index for the name and score column
CREATE INDEX idx_name_first_score
ON names (name(1), score);
