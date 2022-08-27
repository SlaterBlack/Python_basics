class GoCard:
    _balance=0.0
    transactions=[["item","amount($)","Balance ($)"]]

    def __init__(self,Startbalance):
        self._balance = Startbalance
        self._transaction_history = [Startbalance]

    def getbal(self):
        return 

    def addtopup(self,topup):
        self._balance+=topup

    
    def rideCost(self,cost):
        self._balance-+cost

    def getStatement(self):...