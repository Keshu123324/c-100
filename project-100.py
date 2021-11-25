class ATM(object):
    def __init__(self,Card,Pin):
        self.Card=Card
        self.Pin=Pin

    def cashWithdraw(self):
        print("Cash withdraw in progress.......completed")

    def balanceEnquiry(self):
        print("Balance enquiry")

mybank=ATM("1234","1234")
print(mybank.cashWithdraw())
print(mybank.balanceEnquiry())
