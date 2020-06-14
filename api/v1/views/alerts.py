""" API Rest for alert - VIEW """
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.alert import Alert
from models import storage
from models.category_sub import CategorySub

attr = ['mileage_limit', 'mileage_act', 'high', 'middle']

def set_obj(obj, **data):
    for key, value in data.items():
        if key in attr:
            setattr(obj, key, value)

@app_views.route('/categories_sub/<cats_id>/alerts', methods=['POST'])
def create_alert(cats_id):
    """ Create an alert """
    try:
        if len(storage.getobject(CategorySub, "id", cats_id)) == 0:
            return jsonify({"Error": "CategorySub id not found"})
        data = request.get_json(force=True)
        for at in attr:
            if at not in data.keys():
                return jsonify({"Error": "Missing " + at})
        new_obj = Alert()
        set_obj(new_obj, **data)
        new_obj.low = (new_obj.middle - 1)
        new_obj.CategorySub_id = cats_id
        storage.insert(new_obj)
        return jsonify(new_obj.to_dict())
    except Exception:
        abort(404)
    
@app_views.route('/alerts/<alert_id>/', methods=['PUT'])
def update_alert(alert_id):
    try:
        my_alert = storage.getobject(Alert, "id", alert_id, "Dict")["Alert."+ str(alert_id)]
        data = request.get_json(force=True)
        set_obj(my_alert, **data)
        if 'high' or 'middle' in data:
            my_alert.low = (my_alert.middle - 1)
        storage.commit()
        return jsonify(my_alert.to_dict())
    except Exception:
        abort(404)

@app_views.route('/alerts/<alert_id>/', methods=['DELETE'])
def delete_alert(alert_id):
    try:
        my_alert = storage.getobject(Alert, "id", alert_id, "Dict")["Alert." + str(alert_id)]
        storage.delete(my_alert)
        return jsonify({})
    except Exception:
        abort(404)




