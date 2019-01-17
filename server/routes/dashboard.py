from flask_cors import cross_origin
from flask import jsonify, request
from server import app
from server.models.information import Information
from server.services.dashboard import Dashboard


@app.route('/dashboard', methods=['GET'])
@cross_origin(origin='')
def get_dashboard():
    dashboard = Dashboard()
    return jsonify(dashboard.getDashboard())