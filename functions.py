piece_values={"p":1,"l":3,"n":4,"s":5,"g":6,"b":8,"r":10,"k":0,
              "+p":7,"+l":6,"+n":6,"+s":6,"+b":10,"+r":12}   
pawnfilledcolumnsplayer1=[1,2,3,4,5,6,7,8,9]
pawnfilledcolumnsplayer2=[1,2,3,4,5,6,7,8,9]
promotable=["p","l","n","s","b","r"]
directions=["up","down","left","right","upleft","upright","downleft","downright"]



startmat=[["2la9","2ka8","2sa7","2ga6","2ka5","2ga4","2sa3","2ka2","2la1"],
          ["","2rb8","","","","","","2bb2",""],
          ["2pc9","2pc8","2pc7","2pc6","2pc5","2pc4","2pc3","2pc2","2pc1"],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["1pg9","1pg8","1pg7","1pg6","1pg5","1pg4","1pg3","1pg2","1pg1"],
          ["","1bh8","","","","","","1rh2",""],
          ["1li9","1ki8","1si7","1gi6","1ki5","1gi4","1si3","1ki2","1li1"]]
positionofpieces={"2la9":(0,8),"2ka8":(1,8),"2sa7":(2,8),"2ga6":(3,8),"2ka5":(4,8),"2ga4":(5,8),"2sa3":(6,8),"2ka2":(7,8),"2la1":(8,8),
                  "2rb8":(1,7),"2bb2":(7,7),
                  "2pc9":(0,6),"2pc8":(1,6),"2pc7":(2,6),"2pc6":(3,6),"2pc5":(4,6),"2pc4":(5,6),"2pc3":(6,6),"2pc2":(7,6),"2pc1":(8,6),
                  "1pg9":(0,2),"1pg8":(1,2),"1pg7":(2,2),"1pg6":(3,2),"1pg5":(4,2),"1pg4":(5,2),"1pg3":(6,2),"1pg2":(7,2),"1pg1":(8,2),
                  "1bh8":(1,1),"1rh2":(7,1),
                  "1li9":(0,0),"1ki8":(1,0),"1si7":(2,0),"1gi6":(3,0),"1ki5":(4,0),"1gi4":(5,0),"1si3":(6,0),"1ki2":(7,0),"1li1":(8,0)}
piecesofposition={ (0,8):"2la9", (1,8):"2ka8", (2,8):"2sa7", (3,8):"2ga6", (4,8):"2ka5", (5,8):"2ga4", (6,8):"2sa3", (7,8):"2ka2", (8,8):"2la1",
                            (1,7):"2rb8", (7,7):"2bb2",
                            (0,6):"2pc9", (1,6):"2pc8", (2,6):"2pc7", (3,6):"2pc6", (4,6):"2pc5", (5,6):"2pc4", (6,6):"2pc3", (7,6):"2pc2", (8,6):"2pc1",
                            (0,2):"1pg9", (1,2):"1pg8", (2,2):"1pg7", (3,2):"1pg6", (4,2):"1pg5", (5,2):"1pg4", (6,2):"1pg3", (7,2):"1pg2", (8,2):"1pg1",
                            (1,1):"1bh8", (7,1):"1rh2",
                            (0,0):"1li9", (1,0):"1ki8", (2,0):"1si7", (3,0):"1gi6", (4,0):"1ki5", (5,0):"1gi4", (6,0):"1si3", (7,0):"1ki2", (8,0):"1li1"}

piecefilledpositionsplayer1=[key for key in piecesofposition if piecesofposition[key][0]=="1"]
piecefilledpositionsplayer2=[key for key in piecesofposition if piecesofposition[key][0]=="2"]
player1pieces=[piecesofposition[key] for key in piecefilledpositionsplayer1]
player2pieces=[piecesofposition[key] for key in piecefilledpositionsplayer2]
pawnfilledcolumnsplayer1=[1,2,3,4,5,6,7,8,9]
pawnfilledcolumnsplayer2=[1,2,3,4,5,6,7,8,9]


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
            original=piecesofposition.pop((self.x,self.y))
            if self.player==2:
                self.y-=1
            elif self.player==1:
                self.y+=1
            piecesofposition[(self.x,self.y)]=original
    class Lance:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self):
            original=piecesofposition.pop((self.x,self.y))
            if self.player==2:
                self.y-=self.steps
            elif self.player==1:
                self.y+=self.steps
            piecesofposition[(self.x,self.y)]=original
    class Knight:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class Silver:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class Gold:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class Bishop:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class Rook:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class King:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class PromotedPawn:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class PromotedLance:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
    class PromotedKnight:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
 
    class PromotedSilver:
        def __init__(self, player, coordinates):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
  
    class PromotedBishop:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original

    class PromotedRook:
        def __init__(self, player, coordinates, steps):
            self.player = player
            self.x = coordinates[0]
            self.y = coordinates[1]
            self.steps = steps
        def move(self, direction):
            original=piecesofposition.pop((self.x,self.y))
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
            piecesofposition[(self.x,self.y)]=original
            
def droppiece(player):
    piece=str(input("Enter piece to drop: "))
    if player == 1:
        if piece=="pawn":
            x=int(input("Enter x coordinate to drop at (0-8): "))
            y=int(input("Enter y coordinate to drop at (0-7): "))
            while y<0 or y>7:
                y= int(input("Enter y coordinate to drop at (0-7): "))
            while x in pawnfilledcolumnsplayer1:
                print("You already have a pawn in this column. Choose another column.")
                x=int(input("Enter x coordinate to drop at (0-8): "))
            pawnfilledcolumnsplayer1.append(x+1)
        elif piece=="lance":
            x=int(input("Enter x coordinate to drop at (0-8): "))
            y=int(input("Enter y coordinate to drop at (0-7): "))
            while y<0 or y>7:
                 y= int(input("Enter y coordinate to drop at (0-7): "))
        elif piece=="knight":
            x=int(input("Enter x coordinate to drop at (0-8): "))
            y=int(input("Enter y coordinate to drop at (0-6): "))
            while y<0 or y>6:
                 y= int(input("Enter y coordinate to drop at (0-6): "))
        elif piece in ["silver", "gold", "bishop", "rook"]:
            x=int(input("Enter x coordinate to drop at (0-8): "))
            y=int(input("Enter y coordinate to drop at (0-8): "))
            while y<0 or y>8:
                 y= int(input("Enter y coordinate to drop at (0-8): "))
        else:
            print("Invalid piece")
            return droppiece(player)
        