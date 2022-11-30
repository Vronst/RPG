import sqlite3


def sql_save(x):

    connection = sqlite3.connect('list_npc.db')
    cursor = connection.cursor()

    cursor.execute("""
    SELECT COUNT * FROM npcs
    WHERE fr = '{}'
    """.format(x))
    connection.commit()
    connection.close()
#blad
