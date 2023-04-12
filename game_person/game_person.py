from app import Blueprint, jsonify, request
from app.use_db import game_person_db


game_person = Blueprint('game_person', __name__)


@game_person.route('/game_persons', methods=['GET', 'POST'])
def all_game_persons():
    if request.method == 'POST':
        name_gp = request.json['name_gp']
        story = request.json['story']
        avatar_png = request.json['avatar_png']

        if avatar_png == '':
            game_person_db.create_without_avatar([name_gp, story])
        else:
            pass

    elif request.method == 'GET':
        json_persons = []
        persons = game_person_db.inf_about_all()

        for p in persons:
            json_persons.append({
                "id_gp": p[0],
                "name_gp": p[1],
                "story": p[2],
                "avatar_png": p[3]
            })

        return jsonify(json_persons)
