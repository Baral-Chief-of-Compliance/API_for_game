from app import Blueprint, jsonify, request
from app.use_db import skills_db


skills = Blueprint('skills', __name__)


@skills.route('/skills', methods=["GET", "POST"])
def all_skills():
    if request.method == "POST":
        name_s = request.json["name_s"]
        id_gp = request.json["id_gp"]