import sqlite3
import random

def load_npc():

    connection = sqlite3.connect('list_npc.db')
    cursor = connection.cursor()

    search = input("Type name of fraction: \n")
    number_of = input("Random (R) or All (A)\n").upper()
    cursor.execute("""
    SELECT * FROM npcs
    WHERE fr = '{}'
    """.format(search))
    if number_of == 'A':
        druk = cursor.fetchall()
        print(druk)
    elif number_of == 'R':
        x = int(input("Max number: \n"))
        druk = cursor.fetchone()
        ilosc = random.randint(1, x)
        while ilosc > 0:
            print(druk)
            ilosc -= 1

    connection.commit()
    connection.close()