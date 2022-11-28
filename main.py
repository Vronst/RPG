from staty import NPC
import sqlite3


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
        Int INTEGER,
        WP INTEGER,
        Fel INTEGER
""")
polaczenie.commit()
