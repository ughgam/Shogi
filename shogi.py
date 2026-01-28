import functions

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
                  "1li9":(0,0),"1ki8":(0,1),"1si7":(0,2),"1gi6":(0,3),"1ki5":(0,4),"1gi4":(0,5),"1si3":(0,6),"1ki2":(0,7),"1li1":(0,8)}
player1pieces=["1pg9","1pg8","1pg7","1pg6","1pg5","1pg4","1pg3","1pg2","1pg1",
               "1bh8","1rh2",
               "1li9","1ki8","1si7","1gi6","1ki5","1gi4","1si3","1ki2","1li1"]
player2pieces=["2pc9","2pc8","2pc7","2pc6","2pc5","2pc4","2pc3","2pc2","2pc1",
               "2rb8","2bb2",
               "2la9","2ka8","2sa7","2ga6","2ka5","2ga4","2sa3","2ka2","2la1"]
print(startmat)
moves=0
player=1
while True:
    if moves%2==1:
        player=2
        print("Player 2's turn")
    else:
        player=1
        print("Player 1's turn")
    inp=input()
    if inp in player1pieces and player==1 or inp in player2pieces and player==2:
        moves+=1
        print("Valid input")
        if inp[1]=="p":
            functions.Piece.Pawn(player, positionofpieces[inp]).move()
            print("Pawn moved")
        elif inp[1]=="l":
            steps=int(input("Enter number of steps to move forward: "))
            functions.Piece.Lance(player, positionofpieces[inp], steps).move()
            print("Lance moved")
        elif inp[1]=="n":
            direction=str(input("Enter direction to move (upleft/upright): ")).lower()
            if player==2 and direction in ["upleft","upright"]:
                if direction=="upleft":
                    direction="downright"
                else:
                    direction="downleft"
            functions.Piece.Knight(player, positionofpieces[inp]).move(direction)
            print("Knight moved")
        elif inp[1]=="s":
            direction=str(input("Enter direction to move (up/upleft/upright/downleft/downright): ")).lower()
            if player==2 and direction in ["up","upleft","upright","downleft","downright"]:
                if direction=="up":
                    direction="down"
                elif direction=="upleft":
                    direction="downright"
                elif direction=="upright":
                    direction="downleft"
                elif direction=="downleft":
                    direction="upright"
                elif direction=="downright":
                    direction="upleft"
            functions.Piece.Silver(player, positionofpieces[inp]).move(direction)
            print("Silver moved")
        elif inp[1]=="g":
            direction=str(input("Enter direction to move (up/down/left/right/upleft/upright): ")).lower()
            if player==2 and direction in ["up","down","left","right","upleft","upright"]:
                if direction=="up":
                    direction="down"
                elif direction=="down":
                    direction="up"
                elif direction=="left":
                    direction="right"
                elif direction=="right":
                    direction="left"
                elif direction=="upleft":
                    direction="downright"
                elif direction=="upright":
                    direction="downleft"
            functions.Piece.Gold(player, positionofpieces[inp]).move(direction)
            print("Gold moved")
        elif inp[1]=="b":
            steps=int(input("Enter number of steps to move: "))
            direction=str(input("Enter direction to move (upleft/upright/downleft/downright): ")).lower()
            if player==2 and direction in ["upleft","upright","downleft","downright"]:
                if direction=="upleft":
                    direction="downright"
                elif direction=="upright":
                    direction="downleft"
                elif direction=="downleft":
                    direction="upright"
                elif direction=="downright":
                    direction="upleft"
            functions.Piece.Bishop(player, positionofpieces[inp],steps).move(direction)
            print("Bishop moved")
        elif inp[1]=="r":
            steps=int(input("Enter number of steps to move: "))
            direction=str(input("Enter direction to move (up/down/left/right): ")).lower()
            if player==2 and direction in ["up","down","left","right"]:
                if direction=="up":
                    direction="down"
                elif direction=="down":
                    direction="up"
                elif direction=="left":
                    direction="right"
                elif direction=="right":
                    direction="left"
            functions.Piece.Rook(player, positionofpieces[inp],steps).move(direction)
            print("Rook moved")
        elif inp[1]=="k":
            direction=str(input("Enter direction to move (up/down/left/right/upleft/upright/downleft/downright): ")).lower()
            if player==2 and direction in ["up","down","left","right","upleft","upright","downleft","downright"]:
                if direction=="up":
                    direction="down"
                elif direction=="down":
                    direction="up"
                elif direction=="left":
                    direction="right"
                elif direction=="right":
                    direction="left"
                elif direction=="upleft":
                    direction="downright"
                elif direction=="upright":
                    direction="downleft"
                elif direction=="downleft":
                    direction="upright"
                elif direction=="downright":
                    direction="upleft"
            print("King moved")
        else:
            moves-=1
            print("Invalid piece")
            continue
    elif inp=="exit":
        break
    else:
        print("Invalid input")
        continue