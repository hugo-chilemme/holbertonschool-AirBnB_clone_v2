--set db and user

CREATE DATABASE IF NOT EXISTS hbnb_dev_db; 
CREATE USER IF NOT EXISTS 'hbnb_dev'@'%';
GRANT ALL PRIVILEGES ON *.* TO 'hbnb_dev'@'%';
ALTER USER 'hbnb_dev'@'%' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'%';
FLUSH PRIVILEGES;

