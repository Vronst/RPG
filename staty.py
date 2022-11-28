#import sqlite3

class NPC:

    def __init__(self, fr="", name="", race="", hp=1, ll=0, rl=0, ch=0, la=0, ra=0, he=0, WS=1, BS=1, S=1, T=1, I=1, Ag=1, Dex=1, Int=1, WP=1, Fel=1):
        self.fr = fr
        self.name = name
        self.hp = hp
        self.ll = ll
        self.rl = rl
        self.ch = ch
        self.la = la
        self.ra = ra
        self.he= he
        self.WS = WS
        self.race = race
        self.BS = BS
        self.S = S
        self.T = T
        self.i = I
        self.Ag = Ag
        self.Dex = Dex
        self.Int = Int
        self.WP = WP
        self.Fel = Fel
        #self.connection = sqlite3.connect('list_npc.db')
        #self.cursor = self.connection.cursor()