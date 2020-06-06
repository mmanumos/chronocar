# Chronocar
:open_file_folder: chronocar/

## Stack
* [x] HTML
* [x] CSS
* [x] JavaScript
* [x] Python
* [x] MySQL

## Install & Setup
* [x] pycodestyle
* [x] MySQL
* [x] Flask
* [x] SQLAlchemy

## Directory description
* ```api/``` 
* ```api/v1/``` 
* ```api/v1/views/``` 
* ```models/``` 
* ```models/engine/``` 
* ```static/``` Directory contains all content static this project.
* ```static/images/``` 
* ```static/scripts/``` 
* ```static/styles/``` 
* ```templates/``` Directory contains all html files for this project.
* ```tests/``` 

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
