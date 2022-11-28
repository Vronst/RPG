from staty import NPC
import sqlite3
import random


p1 = []  # postacie

polaczenie = sqlite3.connect('list_npc.db')

kursor = polaczenie.cursor()

kursor.execute("""
CREATE TABLE IF NOT EXISTS npcs (
        fr TEXT DEFAULT 'default',
        name TEXT DEFAULT 'Paolo',
        hp INTEGER DEFAULT 1,
        ll INTEGER DEFAULT 1,
        rl INTEGER DEFAULT 1,
        ch INTEGER DEFAULT 1,
        la INTEGER DEFAULT 1,
        ra INTEGER DEFAULT 1,
        he INTEGER DEFAULT 1,
        WS INTEGER DEFAULT 1,
        race TEXT DEFAULT 'Human',
        BS INTEGER DEFAULT 1,
        S INTEGER DEFAULT 1,
        T INTEGER DEFAULT 1,
        I INTEGER DEFAULT 1,
        Ag INTEGER DEFAULT 1,
        Dex INTEGER DEFAULT 1,
        Int INTEGER DEFAULT 1,
        WP INTEGER DEFAULT 1,
        Fel INTEGER DEFAULT 1
""")
polaczenie.commit()


def add_npc():

    b0 = str(input("Fratcion: "))
    b1 = str(input("Name: "))
    b2 = str(input("Race: "))
    b3 = int(input("HP: "))
    b4 = int(input("Left leg armor: "))
    b5 = int(input("Right leg armor: "))
    b6 = int(input("Left arm armor: "))
    b7 = int(input("Right arm armor: "))
    b8 = int(input("Chest armor: "))
    b9 = int(input("Head armor: "))
    b10 = int(input("WS: "))
    b11 = int(input("BS: "))
    b12 = int(input("S: "))
    b13 = int(input("T: "))
    b14 = int(input("I: "))
    b15 = int(input("AG: "))
    b16 = int(input("Dex: "))
    b17 = int(input("Int: "))
    b18 = int(input("WP: "))
    b19 = int(input("Fel: "))
    NPC({b0}, {b1}, {b2}, {b3}, {b4}, {b5}, {b6}, {b7}, {b8}, {b9}, {b10}, {b11}, {b12}, {b13}, {b14}, {b15}, {b16}, {b17}, {b18}, {b19})

    kursor.execute("""
    INSERT INTO npc VALUES
    ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})
    """.format(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19))
    polaczenie.commit()


def load_npc():

    search = input("Type name of fraction: \n")
    number_of = input("Random (R) or All (A)\n").upper()
    kursor.execute("""
    SELECT * FROM npcs
    WHERE fr = {}
    """.format(search))
    if number_of == 'A':
        druk = kursor.fetchall()
        print(druk)
    elif number_of == 'R':
        x = int(input("Max number: \n"))
        druk = kursor.fetchone()
        ilosc = random.randint(1, x)
        while ilosc > 0:
            print(druk)
            ilosc -= 1

while True:
    choice = input("A: Add NPC\tB: Show NPC\nE: exit").upper()
    if choice == 'A':
        add_npc()
    elif choice == 'B':
        load_npc()
    elif choice == 'E':
        break
