# 간단한 팩토리 메서드
from abc import ABC, abstractmethod

class PizzaStore:
    def order_pizza(self, type):
        pizza = self.create_pizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

    @abstractmethod
    def create_pizza(self, pizza_type):
        pass

class NYPizzaStore(PizzaStore):
    def create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return CheesePizza('NY Style Cheese Pizza')
        
        pass
class Pizza()