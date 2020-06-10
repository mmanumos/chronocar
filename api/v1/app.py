from flask import Flask   
from models import storage
from api.v1.views import app_views
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}}) 

@app.teardown_appcontext
def tear_down(exception):
    """ Calls close from dbstorage -> Session """
    storage.close()

@app.errorhandler(404)
def handler_404(error):
    """ 404 not found """
    return jsonify({'error': 'Not found'}), 404

if __name__ == "__main__":
    app.run("0.0.0.0", int(5000), threaded=True)