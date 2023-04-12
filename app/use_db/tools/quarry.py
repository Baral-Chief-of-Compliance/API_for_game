from app import mysql


def call(quarry, *args, commit, fetchall):

    cur = mysql.connection.cursor()

    cur.execute(quarry, *args)

    if commit:
        cur.close()

        mysql.connection.commit()

        result_of_quarry = None

    else:

        if fetchall:
            result_of_quarry = cur.fetchall()
            cur.close()
        else:
            result_of_quarry = cur.fetchone()
            cur.close()

    return result_of_quarry