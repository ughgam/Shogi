startmat=[["2la9","2ka8","2sa7","2ga6","2ka5","2ga4","2sa3","2ka2","2la1"],
          ["","2rb8","","","","","","2bb2",""],
          ["2pc9","2pc8","2pc7","2pc6","2pc5","2pc4","2pc3","2pc2","2pc1"],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["1pg9","1pg8","1pg7","1pg6","1pg5","1pg4","1pg3","1pg2","1pg1"],
          ["","1bh8","","","","","","1rh2",""],
          ["1li9","1ki8","1si7","1gi6","1ki5","1gi4","1si3","1ki2","1li1"]]
positionofpieces={"2la9":(-4,-4),"2ka8":(-3,-4),"2sa7":(-2,-4),"2ga6":(-1,-4),"2ka5":(0,-4),"2ga4":(1,-4),"2sa3":(2,-4),"2ka2":(3,-4),"2la1":(4,-4),
                  "2rb8":(-3,-3),"2bb2":(3,3),
                  "2pc9":(-4,-2),"2pc8":(-3,-2),"2pc7":(-2,-2),"2pc6":(-1,-2),"2pc5":(0,-2),"2pc4":(1,-2),"2pc3":(2,-2),"2pc2":(3,-2),"2pc1":(4,-2),
                  "1pg9":(-4,2),"1pg8":(-3,2),"1pg7":(-2,2),"1pg6":(-1,2),"1pg5":(0,2),"1pg4":(1,2),"1pg3":(2,2),"1pg2":(3,2),"1pg1":(4,2),
                  "1bh8":(-3,3),"1rh2":(3,-3),
                  "1li9":(-4,4),"1ki8":(-3,4),"1si7":(-2,4),"1gi6":(-1,4),"1ki5":(0,4),"1gi4":(1,4),"1si3":(2,4),"1ki2":(3,4),"1li1":(4,4)}
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
            print("Pawn moved")
            if inp[2]=="g":
                pass
            if inp[2]=="c":
                pass
        elif inp[1]=="l":
            print("Lance moved")
        elif inp[1]=="n":
            print("Knight moved")
        elif inp[1]=="s":
            print("Silver moved")
        elif inp[1]=="g":
            print("Gold moved")
        elif inp[1]=="b":
            print("Bishop moved")
        elif inp[1]=="r":
            print("Rook moved")
        elif inp[1]=="k":
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