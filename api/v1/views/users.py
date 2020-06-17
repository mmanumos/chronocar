""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User
from models.category_sub import CategorySub
import hashlib 

# Allowed attributes to modify and create
attr = ['name', 'last_name', 'email', 'password', 'initial_mileage']

def set_obj(obj, **data):
    """ set the attributes of an object """
    not_key = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in not_key:
            if key == 'password':
                password = value
                m = hashlib.md5()
                m.update(str.encode(password))
                value = m.hexdigest()
            setattr(obj, key, value)

@app_views.route('/users/', methods=['POST'])
def create_user():
    """ Creation of a user """
    try:
        data = request.get_json(force=True)
        if 'email' in data:
            exist = validateEmail(data['email'])
            if exist == 1:
                return jsonify({"Error": "User email already exists"})
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": str("Missing " + at)})
        new_obj = User()
        set_obj(new_obj, **data)
        storage.insert(new_obj)
        #Creation of subcategory Fuel for every new user
        mycs = CategorySub()
        mycs.CategoryMain_id = 1
        mycs.User_id = new_obj.id
        mycs.name = "Fuel"
        storage.insert(mycs)
        return jsonify(new_obj.to_dict())
    except Exception:
        abort(404)

@app_views.route('/users/<user_id>/', methods=['PUT'])
def update_user(user_id):
    """ Update an user  """
    try:
        data = request.get_json(force=True)
        for key in data.keys():
            if key not in attr:
                return jsonify({"error": "Invalid action"}), 404
        obj = storage.getobject(User, "id", user_id, "Dict")["User."+ str(user_id)]
        set_obj(obj, **data)
        storage.commit()
        return jsonify(obj.to_dict())
    except Exception:
        abort(404)

@app_views.route('/users/<user_id>', methods=['DELETE'])
def delete_object(user_id):
    """ Delete an user """
    try:
        obj = storage.getobject(User, "id", user_id, "Dict")["User." + str(user_id)]
        storage.delete(obj)
        return jsonify({})
    except Exception:
        abort(404)

@app_views.route('/users/<user_email>/login', methods=['POST'])
def login(user_email):
    """ Verify password and email  """
    try:
        users = storage.getuser(User, "email", user_email)
        if len(users) == 0:
            return jsonify({"Error": "User email not found"})
        data = request.get_json(force=True)
        if 'password' not in data:
            return jsonify({"Error": "Password is required"})
        #md5 for password
        password = data['password']
        m = hashlib.md5()
        m.update(str.encode(password))
        data['password'] = m.hexdigest()
        if users[0]['password'] == data['password']:
            if 'password' in users[0]:
                del users[0]['password']
            return jsonify(users[0])
    except Exception:
        abort(404)

def validateEmail(email):
    """ Verify if the email exists in database """
    users = storage.getuser(User, "email", email)
    if len(users) > 0:
        return 1
    else:
        return 0
       





