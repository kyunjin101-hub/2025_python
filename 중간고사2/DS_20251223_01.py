class Inventory:
    def __init__(self,stock=0):
        self.stock = stock
        print("새 상품이 등록되었습니다.")

    def get_stock(self):
        return self.stock
    
    def set_stock(self, amount, stock):
        if amount > 0:
            self.amount = amount
        else:
            self.stock = 0

    def add_stock(self, amount):
        if amount > 0:
            self.stock += amount
        return

    def remove_stock(self, amount):
        if amount < self.stock:
            self.stock -= amount
        

item1 = Inventory()
item1.add_stock(10)
item1.remove_stock(3)
print("현재 재고 수량:", item1.get_stock())

item1.set_stock(20)
print("수정된 재고 수량:". item1.get_stock())
        
            
