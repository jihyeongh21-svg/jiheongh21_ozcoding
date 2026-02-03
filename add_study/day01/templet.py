from abc import ABC, abstractmethod

class Serve(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def run(self, input_money):
        self.insert_coin(input_money)
        
        if input_money >= self.price:
            self.check_coin()
            self.make_product() 
            self.out_product()
            self.give_change(input_money)
        else:
            print(f"[{self.name}] 금액이 부족합니다. 전액 반환합니다.")

    def insert_coin(self, money):
        print(f"[{self.name}] 돈 투입: {money}원")

    def check_coin(self):
        print(f"[{self.name}] 금액 검증 완료 (필요: {self.price}원)")

    def out_product(self):
        print(f"[{self.name}] 제품 배출 완료")

    def give_change(self, money):
        change = money - self.price
        print(f"[{self.name}] 거스름돈 {change}원 반환")

    @abstractmethod
    def pre_product(self):
        pass


class CoffeeVendingMachine(Serve):
    def __init__(self):
        super().__init__("커피 자판기", 1200)


    def pre_product(self):
        print(f"[{self.name}] 원두 분쇄 중...")
        print(f"[{self.name}] 추출 중...")
        print(f"[{self.name}] 컵에 담는 중...")

