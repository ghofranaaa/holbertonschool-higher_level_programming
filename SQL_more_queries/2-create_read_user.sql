-- creating a data base and a user, and giving the user only select privileges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2 ;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT on *.* TO 'user_0d_2'@'localhost';