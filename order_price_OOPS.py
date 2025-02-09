class Order():
    def __init__(self,item,price):
        self.item = item
        self.price = price
    def __gt__(self,item2):
        return self.price > item2.price
item2 = Order('chips',40)
item3 = Order('biscuits',30)
print(item2>item3)