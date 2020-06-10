""" API Rest for categories_sub - VIEW """
from api.v1.views import app_views
from flask import jsonify, abort
from models import storage
from models.category_sub import CategorySub
import models

@app_views.route('/categories_sub/', methods=['GET'])
@app_views.route('/categories_sub/<keyname>/users/<keyvalue>', methods=['GET'])
def list_categories_sub(keyname=None, keyvalue=None):
    #try:
    
    if (keyname and keyvalue) is None:
        list_catsub = storage.getobject(CategorySub)
    else:
        list_catsub = storage.getobject(CategorySub, keyname, keyvalue)
    return jsonify(list_catsub)
    #except Exception:
     #   abort(404)
