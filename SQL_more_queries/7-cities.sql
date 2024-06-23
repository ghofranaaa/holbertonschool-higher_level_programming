-- foreign key constraint
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0c_0;
CREATE TABLE IF NOT EXISTS cities
(id INT AUTO_INCREMENT PRIMARY KEY,
state_id NOT NULL,
name VARCHAR(256) NOT NULL,
FOREIGN KEY (state_id) REFERENCES states(id)
);