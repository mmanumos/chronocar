# Chronocar
:open_file_folder: chronocar/

ChronoCar is a PWA that helps mainly vehicle owners to keep track the expenses divided them in categories like Preventive maintenance, corrective maintenance, consumables and fuel. Every expense is recorded with the mileage, therefore allows the app to create alerts to preventive maintenance indicating missing mileage.

## Use the app in this link
http://www.chronocar.online

## Stack technology

### Frontend
* [x] HTML
* [x] CSS - Bootstrap
* [x] JavaScript

### Backend
* [x] Python - Flask
* [x] Python - SQLAlchemy

### Databases
* [x] MySQL 

## Install & Setup
* [x] MySQL 
* [x] Flask
* [x] SQLAlchemy
* [x] flask_cors

## Directory description
* ```api/``` Directory that contains independent API which is used  by the application.
* ```api/v1/``` Version 1 of API
* ```api/v1/views/```  Directory with all view files which contains the routes for API
* ```models/```  Directory contains all logical models.
* ```models/engine/``` Directory contains all models for database connection and methods.
* ```static/``` Directory contains all content static.
* ```static/scripts/``` Directory contains all js files.
* ```static/styles/``` Directory contains all styles.
* ```templates/``` Directory contains all html files.

## File description
* ```AUTHORS``` Lists all individuals having contributed content to the repository.
* ```root/README.md``` Containing a description of the repository and describing what this project is about.
* ```root/directory/README.md``` Containing a specific description of the directory content.
* ```console.py``` Contains the entry point of the command interpreter.
* ```setup_mysql_dev.sq``` and ```setup_mysql_test.sql``` Scripts that prepare a MySQL server for the project.
* ```models/__init__.py``` Create a Python Package.
* ```models/base_model.py``` Contains class ```BaseModel``` that defines all common attributes/methods for other classes.
* ```models/engine/__init__.py``` Create a Python Package.
* ```models/engine/file_storage.py``` Contains class ```FileStorage``` that serializes instances to a JSON file and deserializes JSON file to instances.
* ```models/user.py``` Contains class ```User``` that inherits from ```BaseModel```.
* ```test1_base_model.py``` A test file.
* ```test2_base_model_dict.py``` A test file.
* ```test3_save_reload_base_model.py``` A test file.
* ```test4_save_reload_user.py``` A test file.

## Developers
Manuel Mosquera - [GitHub](https://github.com/mmanumos) / [Twitter](https://twitter.com/mmanumos)  
Javier Andrés Garzón Patarroyo - [GitHub](https://github.com/javierandresgp) / [Twitter](https://twitter.com/javierandresgp0)

## :copyright:
###### Our final project, stage "Foundations" at Holberton School.
