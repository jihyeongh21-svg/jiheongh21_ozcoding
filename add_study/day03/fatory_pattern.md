# 팩토리 패턴 (Factory Pattern)

## 객체의 생성을 위한 인터페이스의 정의를 서브클래스에서 결정하게 하는 패턴

### 팩토리  패턴의 종류

#### A. 간단한 팩토리 (Simple Factory)
> *엄밀히 말하면 디자인 패턴이 아니라 프로그래밍 관용구(I에 가깝다.*

- **상황:** 피자 가게(`PizzaStore`)의 `orderPizza()` 메서드 안에 피자 종류를 고르는 `if-else` 구문이 너무 많아짐.
- **해결:** 객체 생성을 전담하는 `SimplePizzaFactory` 클래스를 따로 만듦.
- **구조:** `PizzaStore`가 `SimplePizzaFactory`를 **구성(Composition)**으로 가짐 (`has-a`).
- **한계:** 가게가 확장되어 지점(NY, Chicago)별로 다른 스타일을 만들어야 할 때, 하나의 공장 클래스로는 유연성이 부족함.

#### B. 팩토리 메서드 패턴 (Factory Method Pattern)
> **정의:** 객체를 생성하기 위한 인터페이스를 정의하는데, 어떤 클래스의 인스턴스를 만들지는 **서브클래스에서 결정**하게 만듭니다.

- **핵심:** 클래스의 인스턴스를 만드는 일을 **서브클래스에게 미루는(defer)** 것.
- **구조 (상속 - Inheritance 이용):**
    - **Creator (생산자):** `PizzaStore` (추상 클래스)
        - `createPizza()`: **추상 메서드 (팩토리 메서드)**
        - `orderPizza()`: `createPizza`를 사용하는 템플릿 메서드
    - **Concrete Creator (구체적 생산자):** `NYPizzaStore`, `ChicagoPizzaStore`
        - `createPizza()`를 실제로 구현하여 `NYStyleCheesePizza` 등을 반환함.
- **장점:** 클라이언트 코드(`orderPizza`)는 구체적인 피자 클래스(`NYStylePizza`)를 전혀 알 필요가 없음. (결합도 감소)

#### C. 추상 팩토리 패턴 (Abstract Factory Pattern)
> **정의:** 인터페이스를 이용하여 **서로 연관된, 또는 의존하는 객체들(제품군, Family)**을 구상 클래스를 지정하지 않고도 생성할 수 있게 해 줍니다.

- **상황:** 지점별로 사용하는 **원재료(Dough, Sauce, Cheese)**가 다름. 이를 세트로 묶어서 관리해야 함.
- **구조 (구성 - Composition 이용):**
    - **Abstract Factory:** `PizzaIngredientFactory` (인터페이스)
        - `createDough()`, `createSauce()`, `createCheese()`...
    - **Concrete Factory:** `NYPizzaIngredientFactory`, `ChicagoPizzaIngredientFactory`
    - **Client:** `Pizza` 클래스는 팩토리를 주입받아 재료를 생성함.
- **특징:** 팩토리 메서드 패턴이 '메서드'를 통해 객체를 만든다면, 추상 팩토리는 '객체(공장)'를 통해 제품군을 만듦.

---
### 핵심 : 의존성 역전 원칙 (DIP)
**"추상화된 것에 의존하도록 만들어라. 구상 클래스에 의존하지 않도록 만들어라."**