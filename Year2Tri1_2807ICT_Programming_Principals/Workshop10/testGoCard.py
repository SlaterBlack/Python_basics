from GoCard import GoCard

transactions=[["item","amount($)","Balance ($)"]]
def printStmt(st):
    for n in transactions:
        print(transactions)

startBal= float(input("creating account. Input initial balance: "))
card=GoCard(startBal)

cmd = ""
while cmd!="q":
    cmd=input("? ")
    if cmd == "q":
        printStmt(card.getStatement())
        quit(0)
    elif cmd == "b":
        bal = card.getBal()
        print("Balance = ${:.2f}".format(card.getBal()))
    else:
        cmd.split()
        if len(cmd) != 2:
            print("Bad command.")
        elif cmd[0]=="r":
            card.rideCost(float(cmd[1]))
            transactions.append(["Ride", cmd[1], card.getbal])
        elif cmd[0]=="t":
            card.addtopup(float(cmd[1]))
            transactions.append(["Top up", cmd[1], card.getbal])
        else:
            print("Bad command.")

