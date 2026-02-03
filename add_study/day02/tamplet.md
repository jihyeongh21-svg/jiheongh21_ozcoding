# 템플릿 메서드 패턴 (Template Method Pattern)

### 1. 패턴의 정의
> **알고리즘의 골격(Skeleton)**을 정의하고, 일부 단계는 서브클래스에서 구현하도록 미루는 패턴.
> 알고리즘의 구조는 그대로 유지하면서 특정 단계의 작업만 서브클래스에서 재정의할 수 있다.

---

### 2. 예제 시나리오: 카페인 음료 만들기 (Coffee vs Tea)

**공통점 (부모 클래스)**
1. 물을 끓인다 (`boil_water`)
2. 컵에 따른다 (`pour_in_cup`)

**차이점 (자식 클래스 - 추상 메서드)**
1. 재료를 우려낸다 (`brew`)
   - 커피: 필터로 우려냄
   - 차: 티백을 담금
2. 첨가물을 넣는다 (`add_condiments`)
   - 커피: 설탕/우유
   - 차: 레몬

---

### 3. 주요 구성 요소

#### 1. 템플릿 메서드 (`prepare_recipe`)
- 전체 알고리즘의 **순서(흐름)**를 제어함.
- 서브클래스가 흐름을 제멋대로 변경하지 못하도록 보통 `final`로 취급함.

#### 2. 추상 메서드 (`brew`, `add_condiments`)
- 서브클래스가 **반드시 구현해야 하는** 부분.

#### 3. 구체 메서드 (`boil_water`, `pour_in_cup`)
- 모든 서브클래스가 공통으로 사용하는 로직.

#### 4. 후크 (Hook) 메서드 (`customer_wants_condiments`)
- 부모 클래스에 기본 구현(빈 상태 또는 기본값 `True`)이 되어 있는 메서드.
- 서브클래스는 이를 **선택적으로 오버라이드**하여 알고리즘의 흐름에 개입하거나 확장할 수 있음.
- *예: "고객이 원할 때만 추가."*

---

### 4. 핵심 디자인 원칙: 할리우드 원칙 (The Hollywood Principle)

> **"먼저 연락하지 마세요. 저희가 연락드릴게요."**
> **(Don't call us, we'll call you.)**

- **의미**: 서브클래스가 추상클래스를 직접 호출하지 않게 함.
- **동작 방식**: 템플릿메서드가 필요할 때만 서브클래스의 메서드를 호출함.
- **장점**: 의존성 부패(Dependency Rot)를 방지하고, 시스템의 제어권을 한곳(부모 클래스)에서 관리하기 용이함.
- **단점**: 구조를 가짐으로서 생기는 유연성의 상실(불필요한 부분도 알고리즘 순서를 따랴야 함 ), 부모 자식간의 강한결합(부모에서 변경되는 부분에 대해서 강한 영향을 받음)

### 5. 예제 코드 (Python 구현)

```python
from abc import ABC, abstractmethod

# 1. 추상 클래스 (템플릿) 전체 알고리즘 구조를 정의

class CaffeineBeverage(ABC):
    
    # 템플릿 메서드
    # 음료를 만드는 전체 흐름을 정의
    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        
        # [후크(Hook) 활용]
        # 조건에 따라 첨가물 추가 여부를 결정
        if self.customer_wants_condiments():
            self.add_condiments()
    
    # 서브클래스에서 구체적인 우려내는 법을 구현
    @abstractmethod
    def brew(self):
        pass
    
    # 서브클래스에서 구체적인 추가동작을 구현
    @abstractmethod
    def add_condiments(self):
        pass
    
    #  공통 로직
    def boil_water(self):
        print("물 끓이는 중")
        
    def pour_in_cup(self):
        print("컵에 따르는 중")
        
    # 후크(Hook) 메서드
    # 기본적으로 True를 반환, 서브클래스에서 필요시에 오버라이드 가능
    
    # "할리우드 원칙"에 따라 부모 클래스가 이 메서드를 호출하여 판단
    def customer_wants_condiments(self):
        return True

# 2. 구체 클래스 (Coffee)

class Coffee(CaffeineBeverage):
    def brew(self):
        print("필터로 커피를 우려내는 중")
        
    def add_condiments(self):
        print("설탕과 우유를 추가하는 중")
        
    # 후크 오버라이딩
    # 커피는 고객에게 물어보고 넣을지 말지 결정합니다.
    def customer_wants_condiments(self):
        answer = input("커피에 우유와 설탕을 넣을까요? (y/n): ").lower()
        if answer == 'y':
            return True
        else:
            return False

# 3. 구체 클래스 (Tea)

class Tea(CaffeineBeverage):
    def brew(self):
        print("차를 우려내는 중")
        
    def add_condiments(self):
        print("레몬을 추가하는 중")
        
    # 후크를 오버라이드하지 않았으므로,
    # 부모 클래스의 기본값(True)에 따라 무조건 레몬을 넣습니다.

# 4. 실행 

if __name__ == "__main__":
    print("홍차 준비 (기본 Hook 사용)")
    tea = Tea()
    tea.prepare_recipe()
    
    print("커피 준비 (Hook 오버라이딩)")
    coffee = Coffee()
    coffee.prepare_recipe()
```

### 6. 연습문제

#### 자판기 만들기

##### 문제 설명

**커피 자판기**, **콜라 자판기**, **라면 자판기**를 템플릿 메서드 패턴으로 설계해 보세요.

모든 자판기는 아래와 같은 **공통 흐름**으로 음료/식품을 제공합니다.

1. **돈 투입** - 고객이 금액을 넣는다.
2. **금액 검증** - 투입 금액이 제품 가격 이상인지 확인한다.
3. **제품 준비** - 자판기 종류에 따라 다른 방식으로 제품을 준비한다. *(구체 자판기마다 다름)*
4. **제품 배출** - 준비된 제품을 내보낸다.
5. **거스름돈 반환** - 잔액이 있으면 반환한다.

---

**제품별 준비 방식** 

-(추상 메서드로 구현할 부분)

| 자판기       | 제품 준비 과정 |
|-------------|----------------|
| **커피 자판기** | 원두 분쇄 → 추출 → 컵에 담기 |
| **콜라 자판기** | 캔/병 냉각 확인 → 해당 제품 배출구로 이동 |
| **라면 자판기** | 컵면 배출 → 뜨거운 물 주입 → 뚜껑 열기 힌트 출력 |

---

##### 요구사항

1. **추상 클래스**  
   위 1~5 단계를 담는 **템플릿 메서드**(예: `serve(amount: int)`)를 정의하고,  
   "제품 준비"만 **추상 메서드**로 두어 서브클래스가 구현하도록 하세요.

2. **구체 클래스**  
   - `CoffeeVendingMachine` : 커피 자판기  
   - `ColaVendingMachine`  : 콜라 자판기  
   - `RamenVendingMachine` : 라면 자판기  

   각 클래스에서 "제품 준비" 단계만 **자판기 종류에 맞게** 구현하세요.

3. **공통으로 처리할 수 있는 단계**  
   돈 투입, 금액 검증, 제품 배출, 거스름돈 반환은 **추상 클래스에만** 두고,  
   제품 준비 관련 로직만 서브클래스에 두면 됩니다.

---

##### 예상 출력 예시

```
[커피 자판기] 돈 투입: 1500원
[커피 자판기] 금액 검증 완료 (필요: 1200원)
[커피 자판기] 원두 분쇄 중...
[커피 자판기] 추출 중...
[커피 자판기] 컵에 담는 중...
[커피 자판기] 제품 배출 완료
[커피 자판기] 거스름돈 300원 반환
```

```
[콜라 자판기] 돈 투입: 1000원
[콜라 자판기] 금액 검증 완료 (필요: 800원)
[콜라 자판기] 냉장 상태 확인 중...
[콜라 자판기] 배출구로 이동 중...
[콜라 자판기] 제품 배출 완료
[콜라 자판기] 거스름돈 200원 반환
```

```
[라면 자판기] 돈 투입: 2000원
[라면 자판기] 금액 검증 완료 (필요: 1500원)
[라면 자판기] 컵면 배출
[라면 자판기] 뜨거운 물 주입 중...
[라면 자판기] 제품 배출 완료
[라면 자판기] 거스름돈 500원 반환
```

---

##### 정리

- **템플릿 메서드**: `serve(amount)` → 전체 흐름(1~5)을 한 번에 정의.
- **추상 메서드**: "제품 준비" 단계만 서브클래스에서 구현.

이 구조로 **커피 / 콜라 / 라면 자판기**를 구현해 보세요.

##### 구현 코드
```python
from abc import ABC, abstractmethod

# 1. 추상 클래스 (템플릿)
class AbstractVendingMachine(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    #   템플릿 메서드
    def serve(self, input_money):
        self.insert_coin(input_money)
        
        # 금액 검증
        if input_money >= self.price:
            self.check_coin()
            
            # 제품 준비 추상메서드
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

    # 추상 메서드 자식 클래스가 구현해야 할 부분
    @abstractmethod
    def prepare_product(self):
        raise NotImplementedError


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
        
```
### 