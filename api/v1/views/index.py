#!/usr/bin/python3
'''
routes:
/status - returns status: Ok
/stats - returns the number of instance
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """Create status return"""
    return jsonify({'status': 'OK'})