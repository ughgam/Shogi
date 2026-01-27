piece_values={"p":1,"l":3,"n":4,"s":5,"g":6,"b":8,"r":10,"k":0,
              "+p":7,"+l":6,"+n":6,"+s":6,"+b":10,"+r":12}   
promotable=["p","l","n","s","b","r"]
class Pawn:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class Lance:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class Knight:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class Silver:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class Gold:
    def __init__(self, player, number):
        self.player = player
        self.number = number

class Bishop:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class Rook:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class King:
    def __init__(self, player):
        self.player = player
class PromotedPawn:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class PromotedLance:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class PromotedKnight:
    def __init__(self, player, number):
        self.player = player
        self.number = number    
class PromotedSilver:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class PromotedBishop:
    def __init__(self, player, number):
        self.player = player
        self.number = number
class PromotedRook:
    def __init__(self, player, number):
        self.player = player
        self.number = number       
