-- setting id to default and adding unique constraint
CREATE TABLE IF NOT EXISTS unique_id
(id INT UNIQUE DEFAULT 1, name VARCHAR(256));