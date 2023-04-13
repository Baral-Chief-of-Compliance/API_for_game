from app.use_db.tools import quarry


def create(*args):
    quarry.call("insert into skills(name_s, id_gp, description_gp, min_damage, "
                "max_damage, chance_crit_interest, max_crit_damage, min_crit_damage, miss_chance) values "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)", *args, commit=True, fetchall=False)


def skills_for_game_person(id_gp):
    inf = quarry.call("select * from skills where id_gp = %s", id_gp,
                      commit=False, fetchall=True)

    return inf


def skills_for_game_person_with_name(name_gp):
    inf = quarry.call("select * from skills where name_gp = %s", name_gp,
                      commit=False, fetchall=True)

    return inf

