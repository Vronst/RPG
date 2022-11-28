#from staty import NPC
import sqlite3
#import random
from add import add_npc
from load import load_npc


p1 = []  # postacie

polaczenie = sqlite3.connect('list_npc.db')

kursor = polaczenie.cursor()

kursor.execute("""
CREATE TABLE IF NOT EXISTS npcs (
        fr TEXT,
        name TEXT,
        hp INTEGER,
        ll INTEGER,
        rl INTEGER,
        ch INTEGER,
        la INTEGER,
        ra INTEGER,
        he INTEGER,
        WS INTEGER,
        race TEXT,
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
    choice = input("A: Add NPC\tB: Show NPC\nE: exit\n").upper()
    if choice == 'A':
        add_npc()
    elif choice == 'B':
        load_npc()
    elif choice == 'E':
        break
