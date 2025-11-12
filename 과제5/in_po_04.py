class Computer:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

    def get_info(self):
        print(f"브랜드:{self.brand}, 가격:{self.price}만 원")
    
class Laptop(Computer):
    def __init__(self,brand,price,weight):
        super().__init__(brand,price)
        self.weight=weight

    def get_info(self):
        super().get_info()
        print("무게:", self.weight)