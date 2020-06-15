""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.category_sub import CategorySub
from models.category_main import CategoryMain
from models.user import User
from models.alert import Alert
from models.expense import Expense
import models

def set_object(obj, **data):
    """ set the attributes of an object with given values """
    not_key = ['id', 'created_at', 'updated_at', 'User_id']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)

@app_views.route('/users/<user_id>/categories_sub/', methods=['GET'])
def list_categories_sub(user_id=None):
    """ Return all categories_sub for a user """
    try:
        myuser = storage.getobject(User, "id", user_id, "Dict")["User." + str(user_id)]
        return jsonify(myuser.categories_sub)
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>/categories_main/<catm_id>/categories_sub/', methods=['POST'])
def create_category_sub(user_id, catm_id):
    """ Create a CategorySub """
    try:
        data = request.get_json(force=True)
        #validations
        if 'name' not in data:
            return jsonify({"error": "missing name for CategorySub"}), 404
        if len(storage.getobject(CategoryMain, "id", catm_id)) == 0:
            return jsonify({"error": "CategoryMain id not found"}), 404
        if len(storage.getobject(User, "id", user_id)) == 0:
            return jsonify({"error": "User id not found"}), 404
        #new object
        new_obj = CategorySub()
        set_object(new_obj, **data)
        new_obj.CategoryMain_id = catm_id
        new_obj.User_id = user_id
        storage.insert(new_obj)
        return jsonify(new_obj.to_dict()), 201
    except Exception:
        abort(404)

@app_views.route('/categories_sub/<cats_id>/', methods=['PUT'])
def update_category_sub(cats_id):
    """ Update a CategorySub """
    """ The User_id it can't be modified """
    try:
        obj = storage.getobject(CategorySub, "id", cats_id, "Dict")["CategorySub." + str(cats_id)]
    except Exception:
        return jsonify({"error": "CategorySub id not found"})
    try:
        data = request.get_json(force=True)
        if 'CategoryMain_id' in data:
            if len(storage.getobject(CategoryMain, "id", data['CategoryMain_id'])) == 0:
                return jsonify({"error": "CategoryMain id not found"}), 404
        if 'User_id' in data:
            return jsonify({"error": "User id - invalid action"}), 404
        set_object(obj, **data)
        storage.commit()
        return jsonify(obj.to_dict()), 200
    except Exception:
        abort(404)

@app_views.route('/categories_sub/<cats_id>', methods=['DELETE'])
def delete_category_sub(cats_id):
    """  """
    try:
        obj = storage.getobject(CategorySub, "id", cats_id, "Dict")["CategorySub." + str(cats_id)]
        # Delete associated alerts
        if obj.CategoryMain_id == 2:
            alerts = obj.alerts
            for al in alerts:
                storage.delete(storage.getobject(Alert, "id", al['id'], "Dict")["Alert." + str(al['id'])])
        # Delete associated expenses
        expenses = obj.expenses
        for ex in expenses:
            storage.delete(storage.getobject(Expense, "id", ex['id'], "Dict")["Expense." + str(ex['id'])])
        # Delete CategorySub
        storage.delete(obj)
        return jsonify({})
    except Exception:
        abort(404)
        

