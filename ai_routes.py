from flask import Blueprint, request, jsonify
from services.ai_service import call_ai_service

ai_bp = Blueprint("ai_bp", __name__)


@ai_bp.route("/process", methods=["POST"])
def process_request():

    data = request.get_json()

    result = call_ai_service(data)

    return jsonify(result)