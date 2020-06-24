""" API Rest for expense - VIEW """
from api.v1.views import app_views
from flask import request, jsonify, abort
from models import storage
from models.expense import Expense
from models.category_sub import CategorySub
from models.user import User
from models.alert import Alert

#Key mandatory attributes 
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
        #Actualización de kilometraje alertas
        second_last = storage.get_second_last(Expense)
        print("new_obj ", new_obj.mileage)
        act_alerts(new_obj.mileage, second_last.mileage)
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

@app_views.route('/users/<user_id>/expenses/', methods=['GET'])
def expenses_user(user_id):
    """ Expenses by user """
    try:
        my_user = storage.getobject(User, "id", user_id, "Dict")["User." + str(user_id)]
    except Exception:
        return jsonify({"Error": "User id not found"})
    try:
        list_catsu = my_user.categories_sub
        list_expen = []
        dict_name = {}
        for catsu in list_catsu:
            list_tempa = storage.getobject(CategorySub, "id", catsu['id'], "Dict")["CategorySub." + str(catsu['id'])].expenses
            dict_name[catsu['id']] = storage.getobject(CategorySub, "id", catsu['id'], "Dict")["CategorySub." + str(catsu['id'])].name
            for tempa in list_tempa:
                list_expen.append(tempa)
        for expe in list_expen:
            if expe['CategorySub_id'] in dict_name:
                expe['catsu_name'] = dict_name[expe['CategorySub_id']]
        return jsonify(list_expen)
    except Exception:
       abort(404)

def act_alerts(new, last):
    """ Set the alerts with last milleage  """
    val = new - last
    alerts = storage.getobject(Alert)
    for al in alerts:
        obj = storage.getobject(Alert, "id", al['id'], "Dict")["Alert." + str(al['id'])]
        setattr(obj,"mileage_act", obj.mileage_act + val)
        storage.commit()
