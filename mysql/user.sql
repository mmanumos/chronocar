CREATE DATABASE IF NOT EXISTS chrono_dev_db;
CREATE USER IF NOT EXISTS 'chrono_dev_user'@'localhost';
SET PASSWORD FOR 'chrono_dev_user'@'localhost' = PASSWORD('chrono_dev_pwd');
-- Assign privileges to these users to connect and manage the respective assigned databases 
GRANT ALL PRIVILEGES ON chrono_dev_db.* TO 'chrono_dev_user'@'localhost';
GRANT SELECT ON performance_schema.* TO 'chrono_dev_user'@'localhost'; 
FLUSH PRIVILEGES;
