class Inventory:
    def _init_(self,prodId,prodName,prodCount):
        self.prodId=prodId
        self.prodName=prodName
        self.prodCount=prodCount

    def show(self):
        print("ID:",self.prodId)
        print("Name:",self.prodName)
        print("Count:",self.prodCount)
display=Inventory(101,"Mobile",10)
display.show()
