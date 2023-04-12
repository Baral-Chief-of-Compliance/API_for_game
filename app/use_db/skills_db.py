from app.use_db.tools import quarry


def create(*args):
    quarry.call("insert into skills(name_s, id_gp, description_gp, min_damage, "
                "max_damage, chance_crit_interest, max_crit_damage, min_crit_damage, miss_chance) values "
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s)", *args, commit=True, fetchall=False)
