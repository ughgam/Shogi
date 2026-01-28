piece_values={"p":1,"l":3,"n":4,"s":5,"g":6,"b":8,"r":10,"k":0,
              "+p":7,"+l":6,"+n":6,"+s":6,"+b":10,"+r":12}   
promotable=["p","l","n","s","b","r"]
directions=["up","down","left","right","upleft","upright","downleft","downright"]
class Piece:
    def __init__(self, player, piece, coordinates):
        self.player = player
        self.piece= piece
        self.coordinates = coordinates
    class Pawn:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self):
            if self.player==2:
                self.y-=1
            elif self.player==1:
                self.y+=1
    class Lance:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self):
            if self.player==2:
                self.y-=self.steps
            elif self.player==1:
                self.y+=self.steps
    class Knight:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="downright":
                    self.x+=1
                    self.y-=2
                elif direction=="downleft":
                    self.x-=1
                    self.y-=2
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="upleft":
                    self.x-=1
                    self.y+=2
                elif direction=="upright":
                    self.x+=1
                    self.y+=2
                else:
                    print("Invalid direction")
    class Silver:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
    class Gold:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="up":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="left":
                    self.x-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
    class Bishop:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            if self.player==2:
                if direction=="downleft":
                    self.x-=self.steps
                    self.y-=self.steps
                elif direction=="downright":
                    self.x+=self.steps
                    self.y-=self.steps
                elif direction=="upleft":
                    self.x-=self.steps
                    self.y+=self.steps
                elif direction=="upright":
                    self.x+=self.steps
                    self.y+=self.steps
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="downleft":
                    self.x-=self.steps
                    self.y-=self.steps
                elif direction=="downright":
                    self.x+=self.steps
                    self.y-=self.steps
                elif direction=="upleft":
                    self.x-=self.steps
                    self.y+=self.steps
                elif direction=="upright":
                    self.x+=self.steps
                    self.y+=self.steps
                else:
                    print("Invalid direction")
    class Rook:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")
            if self.player==1:
                if direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")
    class King:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y-=1
                elif direction=="down":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="upright":
                    self.x+=1
                    self.y-=1
                elif direction=="upleft":
                    self.x-=1
                    self.y-=1
                elif direction=="downright":
                    self.x+=1
                    self.y+=1
                elif direction=="downleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
    class PromotedPawn:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="up":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="left":
                    self.x-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
    class PromotedLance:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="up":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="left":
                    self.x-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
    class PromotedKnight:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="up":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="left":
                    self.x-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
 
    class PromotedSilver:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=1
                elif direction=="up":
                    self.y+=1
                elif direction=="right":
                    self.x+=1
                elif direction=="left":
                    self.x-=1
                elif direction=="downright":
                    self.x+=1
                    self.y-=1
                elif direction=="downleft":
                    self.x-=1
                    self.y-=1
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="up":
                    self.y+=1
                elif direction=="down":
                    self.y-=1
                elif direction=="left":
                    self.x-=1
                elif direction=="right":
                    self.x+=1
                elif direction=="upright":
                    self.x+=1
                    self.y+=1
                elif direction=="upleft":
                    self.x-=1
                    self.y+=1
                else:
                    print("Invalid direction")
  
    class PromotedBishop:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            if self.player==2:
                if direction=="downleft":
                    self.x-=self.steps
                    self.y-=self.steps
                elif direction=="downright":
                    self.x+=self.steps
                    self.y-=self.steps
                elif direction=="upleft":
                    self.x-=self.steps
                    self.y+=self.steps
                elif direction=="upright":
                    self.x+=self.steps
                    self.y+=self.steps
                elif direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")
            elif self.player==1:
                if direction=="downleft":
                    self.x-=self.steps
                    self.y-=self.steps
                elif direction=="downright":
                    self.x+=self.steps
                    self.y-=self.steps
                elif direction=="upleft":
                    self.x-=self.steps
                    self.y+=self.steps
                elif direction=="upright":
                    self.x+=self.steps
                    self.y+=self.steps
                elif direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")

    class PromotedRook:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            if self.player==2:
                if direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                elif direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")
            if self.player==1:
                if direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                elif direction=="down":
                    self.y-=self.steps
                elif direction=="up":
                    self.y+=self.steps
                elif direction=="right":
                    self.x+=self.steps
                elif direction=="left":
                    self.x-=self.steps
                else:
                    print("Invalid direction")
                    