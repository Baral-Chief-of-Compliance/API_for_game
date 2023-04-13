from app.use_db.tools import quarry


def create_with_avatar(*args):
    quarry.call("insert into game_person(name_gp, story, avatar_png) "
                "(%s, %s, %s)", *args,
                commit=True, fetchall=False)


def create_without_avatar(*args):
    quarry.call("insert into game_person(name_gp, story) values "
                "(%s, %s)", *args,
                commit=True, fetchall=False)


def inf_about_all():
    inf = quarry.call("select * from game_person",
                      commit=False, fetchall=True)
    return inf


def inf_about_game_person(id_gp):
    inf = quarry.call("select * from game_person where id_gp = %s", id_gp,
                      commit=False, fetchall=False)

    return inf


def inf_about_game_person_with_name(name_gp):
    inf = quarry.call("select * from game_person where name_gp = %s", name_gp,
                      commit=False, fetchall=False)

    return inf


def delete_game_person(id_gp):
    quarry.call("delete from game_person where id_gp = %s", id_gp,
                commit=True, fetchall=False)


def delete_game_person_with_name(name_gp):
    quarry.call("delete from game_person where name_gp = %s", name_gp,
                commit=True, fetchall=False)
