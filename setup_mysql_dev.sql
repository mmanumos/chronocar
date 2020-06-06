-- Script that prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS chrono_dev_db;
CREATE USER IF NOT EXISTS 'chrono_dev_user'@'localhost' IDENTIFIED BY 'chrono_dev_pwd';
GRANT ALL PRIVILEGES ON `chrono_dev_db`.* TO 'chrono_dev_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'chrono_dev_user'@'localhost';
FLUSH PRIVILEGES;
