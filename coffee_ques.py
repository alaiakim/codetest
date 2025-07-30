'''
### 문제: `ComposeCoffee` 클래스를 완성하라

1. **Delivery (배달)**: 최소 주문 금액 미만이면 배달료 3000원이 추가된다.
2. **ForHere (매장)**: 매장에서 주문하는 서비스로, 배달료는 없다.

1. **Delivery 클래스**
    - 메뉴는 `menu_items` 딕셔너리에 저장되어 있으며, `menu()` 메서드로 출력할 수 있어야 한다.
    - 주문 시 `order(coffee_type, quantity)`를 호출하면 해당 커피 가격 * 수량에 대해 계산하며, **10000원 미만이면 3000원의 배달료가 추가**된다.
    - 주문 정보(종류, 총 금액)는 클래스 내 변수에 저장된다.
    - 결제 시 `charge(payment)`를 호출하면 거스름돈을 계산해 출력한다.
2. **ForHere 클래스**
    - 매장 주문 전용이며, 배달료가 붙지 않는다.
    - 나머지는 Delivery와 동일한 방식으로 작동한다.
    
3. **ComposeCoffee 클래스**
    - `Delivery`와 `ForHere`를 상속하며, 생성자에서 `service_type`을 `"Delivery"` 또는 `"ForHere"`로 받아 어떤 서비스를 사용할지 결정한다.
    - `menu()`, `order()`, `charge()`는 현재 선택된 서비스에 따라 적절한 클래스를 호출한다.
    - `switch_service("Delivery" 또는 "forhere")` 메서드를 이용해 서비스 타입을 전환할 수 있어야 하며, 주문 상태도 초기화해야 한다.
    - `position` 인자는 매장 위치를 나타낸다.

- `ComposeCoffee` 클래스는 **반드시 다중 상속을 활용**해야 한다.
- (Optional) `Super()` 는 부모의 메서드를 갖고 올 때 사용가능
'''