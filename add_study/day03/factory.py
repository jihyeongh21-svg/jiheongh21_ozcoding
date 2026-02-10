# 간단한 팩토리 메서드
from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass
    def bake(self):
        print("오븐에 굽기")
    def cut(self):
        print("피자를 사선으로 자르기")
    def box(self):
        print("상자에 피자 담기")

class NYStyleCheesePizza(Pizza):
    def prepare(self):
        print("도우에 토마토 소스 먼저 그리고 치즈를 올리기")

class ChicagoStyleCheesePizza(Pizza):
    def prepare(self):
        print("도우에 치즈를 먼저 그리고 토마토 소스를 올리기")

class PizzaStore(ABC):
    @abstractmethod
    def createPizza(self, item) -> Pizza:
        # Pizza라는 클래스를 반환 하는 생성자
        pass

    def orderPizza(self, type):
        pizza = self.createPizza(type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()
        return pizza

class NYPizzaStore(PizzaStore):
    def createPizza(self, item) -> Pizza:
        if item == "cheese":
            return NYStyleCheesePizza()
        else:
            return None
        

if __name__ == "__main__":
    # 1. 뉴욕 피자 가게 오픈
    ny_store = NYPizzaStore()

    # 2. 주문 (클라이언트는 구체적인 피자 클래스를 몰라도 됨)
    print(">>> 손님: 치즈 피자 주세요.")
    pizza = ny_store.order_pizza("cheese")
    
    if pizza:
        print(f"\n>>> 서빙 완료: {pizza.name} 맛있게 드세요!")
