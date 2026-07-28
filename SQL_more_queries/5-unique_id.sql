-- creates table unique_id with a unique id defaulting to 1, without failing if it exists
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
