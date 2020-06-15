""" API Rest for expense - VIEW """
from api.v1.views import app_views
from flask import request, jsonify, abort
from models import storage
from models.expense import Expense
from models.category_sub import CategorySub

attr = ['amount', 'mileage']

def set_obj(obj, **data):
    """  set the attributes for an expense """
    not_key = ['id']
    for key, value in data.items():
        if key not in not_key:
            setattr(obj, key, value)

    
@app_views.route('/categories_sub/<cats_id>/expenses/', methods=['POST'])
def create_expense(cats_id):
    """ Create an expense """
    try:
        if len(storage.getobject(CategorySub, "id", cats_id)) == 0:
            return jsonify({"Error": "CategorySub id not found"}), 404
        data = request.get_json(force=True)
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": str("Missing " + at)})
        new_obj = Expense()
        set_obj(new_obj, **data)
        new_obj.CategorySub_id = cats_id
        storage.insert(new_obj)
        return jsonify(new_obj.to_dict())
    except Exception:
        abort(404)

@app_views.route('/expenses/<exp_id>/', methods=['PUT'])
def update_expense(exp_id):
    """ Update an expense """
    try:
        my_obj = storage.getobject(Expense, "id", exp_id, "Dict")["Expense."+ str(exp_id)]
        data = request.get_json(force=True)
        set_obj(my_obj, **data)
        storage.commit()
        return jsonify(my_obj.to_dict())
    except Exception:
        abort(404)

@app_views.route('/expenses/<exp_id>/', methods=['DELETE'])
def delete_expense(exp_id):
    """ Delete an object  """
    try:
        my_obj = storage.getobject(Expense, "id", exp_id, "Dict")["Expense."+ str(exp_id)]
        storage.delete(my_obj)
        return jsonify({})
    except Exception:
        abort(404)

