#from staty import NPC
import sqlite3
#import random
from add import add_npc, p1
from load import load_npc


  # postacie

polaczenie = sqlite3.connect('list_npc.db')

kursor = polaczenie.cursor()

kursor.execute("""
CREATE TABLE IF NOT EXISTS npcs (
        fr TEXT,
        name TEXT,
        race TEXT,
        hp INTEGER,
        ll INTEGER,
        rl INTEGER,
        la INTEGER,
        ra INTEGER,
        ch INTEGER,
        he INTEGER,
        WS INTEGER,
        BS INTEGER,
        S INTEGER,
        T INTEGER,
        I INTEGER,
        Ag INTEGER,
        Dex INTEGER,
        Inter INTEGER,
        WP INTEGER,
        Fel INTEGER)
""")
polaczenie.commit()
polaczenie.close()

while True:
    choice = input("A: Add NPC\tB: Show NPC\tR: Recently added\nE: exit\n").upper()
    if choice == 'A':
        add_npc()
    elif choice == 'B':
        searchby = input("Search by: \nA: fraction\tB: name\n").upper()
        if searchby == 'A':
            load_npc("fr")
        elif searchby == 'B':
            load_npc("race")
    elif choice == 'E':
        break
    elif choice == 'R':
        print(p1)

# usprawnij wyswietlanie
