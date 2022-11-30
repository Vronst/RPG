from staty import NPC
import sqlite3

p1 = []
def add_npc():

    try:
        polaczenie = sqlite3.connect('list_npc.db')
        kursor = polaczenie.cursor()

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
        b10= int(input("WS: "))
        b11 = int(input("BS: "))
        b12 = int(input("S: "))
        b13 = int(input("T: "))
        b14 = int(input("I: "))
        b15 = int(input("AG: "))
        b16 = int(input("Dex: "))
        b17 = int(input("Int: "))
        b18 = int(input("WP: "))
        b19 = int(input("Fel: "))
        p1.insert(NPC(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19))



        kursor.execute("""
        INSERT INTO npcs VALUES
        ('{}','{}',{},{},{},{},{},{},{},{},'{}',{},{},{},{},{},{},{},{},{})
        """.format(b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17, b18, b19))
        polaczenie.commit()
        polaczenie.close()  #dodaj kursory
    except ValueError:
        print("EMPTY OR WRONG VALUES\nReturning to main menu\n")



