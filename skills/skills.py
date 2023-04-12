from app import Blueprint, jsonify, request
from app.use_db import skills_db


skills = Blueprint('skills', __name__)


@skills.route('/skills', methods=["GET", "POST"])
def all_skills():
    if request.method == "POST":
        name_s = request.json["name_s"]
        id_gp = request.json["id_gp"]
        description_gp = request.json["description_gp"]
        min_damage = request.json["min_damage"]
        max_damage = request.json["max_damage"]
        chance_crit_interest = request.json["chance_crit_interest"]
        max_crit_damage = request.json["max_crit_damage"]
        min_crit_damage = request.json["min_crit_damage"]
        miss_chance = request.json["miss_chance"]

        skills_db.create([name_s, id_gp, description_gp, min_damage,
                          max_damage, chance_crit_interest, max_crit_damage,
                          min_crit_damage, miss_chance])

        return jsonify(f"skills {name_s} for game_person {id_gp} is add")
