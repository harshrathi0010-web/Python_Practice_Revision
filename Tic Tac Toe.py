"""
TIC TAC TOE


"""
# Decelarations
li=[1,2,3,4,5,6,7,8,9]
flag=0
player="X"
count=0
wins=[(0,1,2),(3,4,5),(6,7,8),(1,4,7),(0,4,8),(2,4,6)]

# Dashboard
while True:
    print("\n\t TIC-TAC-TOE")
    print(f"\n\t {li[0]} | {li[1]} | {li[2]}")
    print("\t-----------")
    print(f"\t {li[3]} | {li[4]} | {li[5]} ")
    print("\t-----------")
    print(f"\t {li[6]} | {li[7]} | {li[8]} ")
    if flag==1:
        break
    if count==9:
        print("\n\t Match Ties")
        break
    ch=int(input(f"\n\t Player {player}  turn's:"))

    if ch in li:
        
        # Reserve Positions
        li[ch-1]=player

        # Win check
        for a,b,c in wins:
            if li[a]==li[b]==li[c]:
                print(f"Player {player} win")
                flag=1
                
        
        

        # Player Change
        if player=="X":
            player='O'
        else:
            player="X"
    else:
        print("\n\t No Cheating")

    


