from app import Blueprint, jsonify, request
from app.use_db import skills_db


skills = Blueprint('skills', __name__)


@skills.route('/skills', methods=["GET", "POST"])
def all_skills():
    if request.method == "POST":
        name_s = request.json["name_s"]
        id_gp = request.json["id_gp"]
        description_s = request.json["description_s"]
        min_damage_s = request.json["min_damage_s"]
        max_damage_s = request.json["max_damage_s"]
        crit_chance_s = request.json["crit_chance_s"]
        max_crit_damage_s = request.json["max_crit_damage_s"]
        min_crit_damage_s = request.json["min_crit_damage_s"]
        miss_chance_s = request.json["miss_chance_s"]

        skills_db.create([name_s, id_gp, description_s, min_damage_s,
                          max_damage_s, crit_chance_s, max_crit_damage_s,
                          min_crit_damage_s, miss_chance_s])

        return jsonify(f"skills {name_s} for game_person {id_gp} is add")

    elif request.method == "GET":
        json_skills = []
        skills = skills_db.inf_about_skills()

        for s in skills:
            json_skills.append({
                "id_s": s[0],
                "name_s": s[1],
                "id_gp": s[2],
                "description_s": s[3],
                "min_damage_s": s[4],
                "max_damage_s": s[5],
                "miss_chance_s": s[6],
                "min_crit_damage_s": s[7],
                "max_crit_damage_s": s[8],
                "crit_chance_s": s[9]
            })

        return jsonify(json_skills)

@skills.route('/skills/<int:id_s>', methods=["GET", "DELETE", "PUT"])
def inf_about_skills(id_s):
    if request.method == "GET":
        inf = skills_db.inf_about_skill(id_s)

        return jsonify({
            "id_s": inf[0],
            "name_s": inf[1],
            "id_gp": inf[2],
            "description_s": inf[3],
            "min_damage_s": inf[4],
            "max_damage_s": inf[5],
            "miss_chance_s": inf[6],
            "min_crit_damage_s": inf[7],
            "max_crit_damage_s": inf[8],
            "crit_chance_s": inf[9]
        })

    elif request.method == "DELETE":
        skills_db.delete_skill(id_s)

        return jsonify(f"skill with id {id_s} is delete")

    elif request.method == "PUT":
        name_s = request.json["name_s"]
        description_s = request.json["description_s"]
        min_damage_s = request.json["min_damage_s"]
        max_damage_s = request.json["max_damage_s"]
        miss_chance_s = request.json["miss_chance_s"]
        min_crit_damage_s = request.json["min_crit_damage_s"]
        max_crit_damage_s = request.json["max_crit_damage_s"]
        crit_chance_s = request.json["crit_chance_s"]

        skills_db.update_skill([name_s, description_s, min_damage_s,
                                max_damage_s, miss_chance_s, min_crit_damage_s,
                                max_crit_damage_s, crit_chance_s, id_s])

        return jsonify(f"skill with id {id_s} is update")
