from abc import ABC, abstractmethod

# 1. 추상 클래스 (템플릿)
class AbstractVendingMachine(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # 템플릿 메서드 전체 흐름 정의
    def serve(self, input_money):
        self.insert_coin(input_money)
        
        # 금액 검증
        if input_money >= self.price:
            self.check_coin()
            
            # 여기가 핵심! 서브클래스에 위임하는 단계
            self.prepare_product() 
            
            self.out_product()
            self.give_change(input_money)
        else:
            print(f"[{self.name}] 금액이 부족합니다. 전액 반환합니다: {input_money}원")

    # 공통 메서드들
    def insert_coin(self, money):
        print(f"[{self.name}] 돈 투입: {money}원")

    def check_coin(self):
        print(f"[{self.name}] 금액 검증 완료 (필요: {self.price}원)")

    def out_product(self):
        print(f"[{self.name}] 제품 배출 완료")

    def give_change(self, money):
        change = money - self.price
        if change > 0:
            print(f"[{self.name}] 거스름돈 {change}원 반환")
        else:
            print(f"[{self.name}] 거스름돈이 없습니다.")

    # [추상 메서드] 자식 클래스가 구현해야 할 부분
    @abstractmethod
    def prepare_product(self):
        pass


# 2. 구체 클래스 구현

class CoffeeVendingMachine(AbstractVendingMachine):
    def __init__(self):
        super().__init__("커피 자판기", 1200)

    def prepare_product(self):
        print(f"[{self.name}] 원두 분쇄 중...")
        print(f"[{self.name}] 추출 중...")
        print(f"[{self.name}] 컵에 담는 중...")


class ColaVendingMachine(AbstractVendingMachine):
    def __init__(self):
        super().__init__("콜라 자판기", 800)

    def prepare_product(self):
        print(f"[{self.name}] 냉장 상태 확인 중...")
        print(f"[{self.name}] 배출구로 이동 중...")


class RamenVendingMachine(AbstractVendingMachine):
    def __init__(self):
        super().__init__("라면 자판기", 1500)

    def prepare_product(self):
        print(f"[{self.name}] 컵면 배출")
        print(f"[{self.name}] 뜨거운 물 주입 중...")
        print(f"[{self.name}] (Tip) 뚜껑은 3분 뒤에 여세요!")


# 3. 실행 
if __name__ == "__main__":
    
    coins = 10000
    machines = [
        CoffeeVendingMachine(),
        ColaVendingMachine(),
        RamenVendingMachine()
    ]

    for machine in machines:
        print(machine.serve(coins))