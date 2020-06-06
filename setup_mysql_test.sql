-- Script that prepares a MySQL server for the project.
CREATE DATABASE IF NOT EXISTS chrono_test_db;
CREATE USER IF NOT EXISTS 'chrono_test_user'@'localhost' IDENTIFIED BY 'chrono_test_pwd';
GRANT ALL PRIVILEGES ON `chrono_test_db`.* TO 'chrono_test_user'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'chrono_test_user'@'localhost';
FLUSH PRIVILEGES;
