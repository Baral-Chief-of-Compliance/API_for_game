from app import app, jsonify, request, Blueprint, send_from_directory, get_swaggerui_blueprint, redirect
from game_person.game_person import game_person
from skills.skills import skills


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


app.register_blueprint(game_person, url_prefix='/the_stone_sword/api/v1.0/')
app.register_blueprint(skills, url_prefix='/the_stone_sword/api/v1.0/')


@app.route('/')
def swagger():
    return redirect('/swagger')


@app.route('/the_stone_sword/api/v1.0/')
def index():
    return jsonify("пошел нахуй")


### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGER_UI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "The_Stone_Sword_API"
    }
)
app.register_blueprint(SWAGGER_UI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###



# https://editor.swagger.io/
# https://github.com/Sean-Bradley/Seans-Python3-Flask-Rest-Boilerplate/blob/master/static/swagger.json