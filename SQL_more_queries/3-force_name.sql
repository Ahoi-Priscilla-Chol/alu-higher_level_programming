-- creates table force_name with a NOT NULL name field, without failing if it exists
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
