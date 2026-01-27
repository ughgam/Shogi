startmat=[["la9","ka8","sa7","ga6","ka5","ga4","sa3","ka2","la1"],
          ["","rb8","","","","","","bb2",""],
          ["pc9","pc8","pc7","pc6","pc5","pc4","pc3","pc2","pc1"],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["","","","","","","","",""],
          ["pg9","pg8","pg7","pg6","pg5","pg4","pg3","pg2","pg1"],
          ["","bh8","","","","","","rh2",""],
          ["li9","ki8","si7","gi6","ki5","gi4","si3","ki2","li1"]]
positionofpieces={"la9":(-4,-4),"ka8":(-3,-4),"sa7":(-2,-4),"ga6":(-1,-4),"ka5":(0,-4),"ga4":(1,-4),"sa3":(2,-4),"ka2":(3,-4),"la1":(4,-4),
                  "rb8":(-3,-3),"bb2":(3,3),
                  "pc9":(-4,-2),"pc8":(-3,-2),"pc7":(-2,-2),"pc6":(-1,-2),"pc5":(0,-2),"pc4":(1,-2),"pc3":(2,-2),"pc2":(3,-2),"pc1":(4,-2),
                  "pg9":(-4,2),"pg8":(-3,2),"pg7":(-2,2),"pg6":(-1,2),"pg5":(0,2),"pg4":(1,2),"pg3":(2,2),"pg2":(3,2),"pg1":(4,2),
                  "bh8":(-3,3),"rh2":(3,-3),
                  "li9":(-4,4),"ki8":(-3,4),"si7":(-2,4),"gi6":(-1,4),"ki5":(0,4),"gi4":(1,4),"si3":(2,4),"ki2":(3,4),"li1":(4,4)}
print(startmat)
while True:
    inp=input()
    if inp=="exit":
        break
    elif len(inp)!=3 or inp[2] not in "123456789" or inp[1] not in "abcdefghi" or inp[0] not in "plnsgbrk":
        print("Invalid input")
        continue
    else:
        print("Valid input")
    if inp[0]=="p":
        print("Pawn moved")
        if inp[1]=="g":
            pass
        if inp[1]=="c":
            pass
    elif inp[0]=="l":
        print("Lance moved")
    elif inp[0]=="n":
        print("Knight moved")
    elif inp[0]=="s":
        print("Silver moved")
    elif inp[0]=="g":
        print("Gold moved")
    elif inp[0]=="b":
        print("Bishop moved")
    elif inp[0]=="r":
        print("Rook moved")
    elif inp[0]=="k":
        print("King moved")
    else:
        print("Invalid piece")
        