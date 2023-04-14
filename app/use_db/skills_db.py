from app.use_db.tools import quarry


def create(*args):
    quarry.call("insert into skills(name_s, id_gp, description_gp, min_damage, "
                "max_damage, chance_crit_interest, max_crit_damage, min_crit_damage, miss_chance) values "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)", *args, commit=True, fetchall=False)


def skills_for_game_person(id_gp):
    inf = quarry.call("select * from skills where id_gp = %s", [id_gp],
                      commit=False, fetchall=True)

    return inf


def skills_for_game_person_with_name(name_gp):
    inf = quarry.call("select * from skills where name_gp = %s", [name_gp],
                      commit=False, fetchall=True)

    return inf


def inf_about_skill(id_s):
    inf = quarry.call("select * from skills where id_s = %s", [id_s],
                      commit=False, fetchall=False)

    return inf


def delete_skill(id_s):
    quarry.call("delete from skills where id_s = %s", [id_s],
                commit=True, fetchall=False)


def update_skill(*args):
    quarry.call("update skills set name_s = %s, description_s = %s, "
                "min_damage_s = %s, max_damage_s = %s, miss_chance_s = %s, "
                "min_crit_damage_s = %s, max_crit_damage_s = %s, "
                "crit_chance_s = %s where id_s = %s", *args,
                commit=True, fetchall=False)

def inf_about_skills():
    inf = quarry.call("select * from skills", commit=False, fetchall=True)

    return inf

