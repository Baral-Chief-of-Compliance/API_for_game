from app import Blueprint, jsonify, request
from app.use_db import game_person_db
from app.use_db import skills_db


game_person = Blueprint('game_person', __name__)


@game_person.route('/game_persons', methods=['GET', 'POST'])
def all_game_persons():
    if request.method == 'POST':
        name_gp = request.json['name_gp']
        story = request.json['story']

        game_person_db.create_without_avatar([name_gp, story])

        return jsonify(f"{name_gp} is add")

    elif request.method == 'GET':
        json_persons = []
        persons = game_person_db.inf_about_all()

        for p in persons:
            json_persons.append({
                "id_gp": p[0],
                "name_gp": p[1]
            })

        return jsonify(json_persons)


@game_person.route('/game_persons/<int:id_gp>', methods=['GET', 'DELETE', 'PUT'])
def inf_about_game_person(id_gp):
    if request.method == "GET":
        json_skills = []
        inf = game_person_db.inf_about_game_person(id_gp)
        skills = skills_db.skills_for_game_person(id_gp)

        for s in skills:
            json_skills.append({
                "id_s": s[0],
                "name_s": s[1],
                "description_s": s[2],
                "min_damage_s": s[3],
                "max_damage_s": s[4],
                "miss_chance_s": s[5],
                "min_crit_damage_s": s[6],
                "max_crit_damage_s": s[7],
                "crit_chance_s": s[8]
            })
        return jsonify({
            "id_gp": inf[0],
            "name_gp": inf[1],
            "story": inf[2],
            "skills": json_skills
        })

    elif request.method == "DELETE":
        game_person_db.delete_game_person(id_gp)

        return jsonify(f"game person with {id_gp} is delete")

    elif request.method == "PUT":
        name_gp = request.json['name_gp']
        story = request.json['story']

        game_person_db.update_game_person([name_gp, story, id_gp])

        return jsonify(f"data about person with {id_gp} is update")

