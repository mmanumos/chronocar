#!/usr/bin/python3
'''
routes:
/status - returns status: Ok
'''
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status():
    """Route for status return"""
    return jsonify({'status': 'OK'})