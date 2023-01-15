-- creates an index for the name column
CREATE INDEX idx_name_first
ON names (name(1));
