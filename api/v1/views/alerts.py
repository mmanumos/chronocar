""" API Rest for alert - VIEW """
from api.v1.views import app_views
from flask import request, jsonify, abort
from models.alert import Alert
from models import storage
from models.category_sub import CategorySub
from models.user import User

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

@app_views.route('/users/<user_id>/alerts/settings', methods=['GET'])
def alerts_settings(user_id):
    """ Alerts with settings for Ajustes - module """
    try:
        my_user = storage.getobject(User, "id", user_id, "Dict")["User." + str(user_id)]
    except Exception:
        return jsonify({"Error": "User id not found"})
    try:
        list_catsu = my_user.categories_sub
        list_alert = []
        for catsu in list_catsu:
            if catsu['CategoryMain_id'] == 2:
                list_tempa = storage.getobject(CategorySub, "id", catsu['id'], "Dict")["CategorySub." + str(catsu['id'])].alerts
                for tempa in list_tempa:
                    list_alert.append(tempa)
        return jsonify(list_alert)
    except Exception:
        abort(404)

@app_views.route('/users/<user_id>/alerts/panel/', methods=['GET'])
def alerts_panel(user_id):
    """ alerts with colors for main Pannel - Module """
    try:
        my_user = storage.getobject(User, "id", user_id, "Dict")["User." + str(user_id)]
    except Exception:
        return jsonify({"Error": "User id not found"})

    list_catsu = my_user.categories_sub
    list_alert = []
    #Alerts list from Cat Main type 2
    for catsu in list_catsu:
        if catsu['CategoryMain_id'] == 2:
            list_tempa = storage.getobject(CategorySub, "id", catsu['id'], "Dict")["CategorySub." + str(catsu['id'])].alerts
            for tempa in list_tempa:
                list_alert.append(tempa)
    #Identify the color, missing mileage, catsub_name for every alert in main panel
    list_alertpannel = []
    for al in list_alert:
        alert_dict = {}
        alert_dict['missing'] = al['mileage_limit'] - al['mileage_act']
        alert_dict['color'] = return_color(al['mileage_act'], al['high'], al['middle'])
        alert_dict['catsub_name'] = storage.getobject(CategorySub, "id", al['CategorySub_id'], "Dict")["CategorySub." + str(al['CategorySub_id'])].name
        list_alertpannel.append(alert_dict)
    return jsonify(list_alertpannel)


def return_color(mileage_act, high, middle):
    """ Identify the priority color for every alert """
    if mileage_act < middle:
        return str('green')
    elif mileage_act >= middle and mileage_act < high:
        return str('orange')
    else: 
        return str('red')

