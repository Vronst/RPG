import sqlite3
import random
from countcheck import sql_save


def load_npc(checks):

    if checks == 'fr':
        fr = "fr"
        fr1 = "fraction"
    else:
        fr = "name"
       # fr1 = "race"

    sta = ["Fraction:", "Name:", "Race:", "HP:", "Left Leg:",
             "Right leg:","Left arm:", "Right arm:", "Chest:", "Head:", "WS:", "BS:",
             "S:", "T:", "I:", "AG:", "Dex:", "Int:", "WP:", "Fel:"]

    connection = sqlite3.connect('list_npc.db')
    cursor = connection.cursor()

    search = input("Type {}: \n".format(fr))
    if checks == 'fr':
        number_of = input("Random (R) or All (A) or Select (S)\n").upper()
    else:
        number_of = input("Random (R) or All (A)\n").upper()
    cursor.execute("""
    SELECT * FROM npcs
    WHERE {} = '{}'
    """.format(fr, search))
    if number_of == 'A':
        druk = cursor.fetchall()
        #w = 0
        # for petla in range(20):
        #     print(sta[w], end=" ")
        #     print(druk[petla - 1])
        #     w += 1
        print(druk)
    elif number_of == 'S':
        w = 0
        whcheck = True
        while whcheck:
            druk = cursor.fetchone()
            try:
                for petla in range(20):
                    print(sta[w], end=" ")
                    print(druk[petla - 1])
                    w += 1
                    if w > 19:
                        w = 0
            except:
                print("NO MORE NPC!")
                print(druk)
            wh1check = input("N: Next hero\tC: Cancel").upper()
            if wh1check == 'C':
                whcheck = False
            print("NEW HERO\n", )
            #ilosc -= 1
    elif number_of == 'R':
        x = int(input("Max number: \n"))
        ilosc = random.randint(1, x)
        druk = cursor.fetchmany(ilosc)
        print(druk)

    connection.commit()
    connection.close()