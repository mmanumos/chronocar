""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User 

# Allowed attributes to modify and create
attr = ['name', 'last_name', 'email', 'password', 'initial_mileage']

def set_obj(obj, **data):
    """ set the attributes of an object """
    not_key = ['id', 'created_at', 'updated_at']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)

@app_views.route('/users/', methods=['POST'])
def create_user():
    """ Creation of a user """
    try:
        data = request.get_json(force=True)
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": str("Missing " + at)})
        new_obj = User()
        set_obj(new_obj, **data)
        storage.insert(new_obj)
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



