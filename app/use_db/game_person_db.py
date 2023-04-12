from app.use_db.tools import quarry


def create_with_avatar(*args):
    quarry.call("insert into game_person(name_gp, story, avatar_png) "
                "(%s, %s, %s)", *args,
                commit=True, fetchall=False)


def create_without_avatar(*args):
    quarry.call("insert into game_person(name_gp, story) "
                "(%s, %s)", *args,
                commit=True, fetchall=False)


def inf_about_all():
    inf = quarry.call("select * from game_person",
                      commit=False, fetchall=True)
    return inf
