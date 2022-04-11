from flask import Blueprint
from flask import request, jsonify
import logging

jobs_bp = Blueprint("jobs", __name__)
logger = logging.getLogger(__name__)


@jobs_bp.route('/', methods=['GET', 'POST'])
def jobs():
    """ gets and creates jobs """
    try:
        if request.method == 'GET':
            return jsonify({"jobs":{"name":"cashier"}}),200
        else:
            return jsonify({"error":"request has no body."}),400
    except Exception as e:
        logger.exception(f"An error has occured: {str(e)}")
        return jsonify({"error":f"An error has occured: {str(e)}"}),400