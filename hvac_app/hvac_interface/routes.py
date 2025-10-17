from flask import Blueprint, request, jsonify
from data_model.model import Temprature
import yaml

HVAC_DIAG_LOC = r"data_model/hvac_model"

routes = Blueprint('routes', __name__)

# app/app-id/data
@routes.route('/hvac/temperature/<zone>', methods=['GET'])
def hvac_get_tempratures(zone):
    """Return all data of temperature but no values"""
    data = "0"

    return data