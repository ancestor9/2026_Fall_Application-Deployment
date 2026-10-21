#### 1. Pandas Merge 실습(Datascience Handbook)
- [Combining Datasets: Merge and Join](https://jakevdp.github.io/PythonDataScienceHandbook/03.07-merge-and-join.html)
- [Pivot Tables](https://jakevdp.github.io/PythonDataScienceHandbook/03.09-pivot-tables.html)

#### 2. Pandas with SQL 실습 과제: 테이블 조인 및 집계

##### 📝 과제 1. 가장 주문을 많이 한 상위 고객 Top 5 (2개 테이블)

- **사용 테이블:** `customers`, `orders`
- **문제:** 고객별 총 주문 횟수를 집계하여, 가장 주문을 많이 한 상위 5명의 고객 정보를 구하시오.

- **출력 컬럼:** `customer_id`, `first_name`, `last_name`, `order_count`
- **학습 목표:**
  - `customers.customer_id`와 `orders.customer_id`를 연결하는 1:N 조인 실습
  - `COUNT()`와 `GROUP BY`를 이용한 그룹별 집계
  - `ORDER BY`와 `LIMIT`을 이용한 상위 5명 조회

---

##### 📝 과제 2. 매장(Store)별 총 주문 건수 분석 (2개 테이블)

- **사용 테이블:** `stores`, `orders`
- **문제:** 각 매장(`stores`)에서 발생한 총 주문 건수를 집계하여, 주문 건수가 많은 순으로 정렬하시오.

- **출력 컬럼:** `store_id`, `store_name`, `city`, `total_orders`
- **학습 목표:**
  - 매장 테이블과 주문 테이블 간의 외래키(`store_id`) 조인
  - `COUNT()`와 `GROUP BY`를 이용한 매장별 주문 건수 집계
  - `ORDER BY`를 이용한 내림차순 정렬

---

##### 📝 과제 3. 가장 많이 판매된 상품 카테고리 Top 3 (2개 테이블)

- **사용 테이블:** `products`, `order_items`
- **문제:** 상품 카테고리(`category`)별 총 판매 수량(`quantity`의 합계)을 계산하여, 가장 많이 판매된 상위 3개 카테고리를 구하시오.

- **출력 컬럼:** `category`, `total_quantity_sold`
- **학습 목표:**
  - `product_id`를 기준으로 상품 정보와 주문 상세 수량을 결합하는 조인
  - `SUM()`을 이용한 카테고리별 판매 수량 집계
  - `ORDER BY`와 `LIMIT`을 이용한 상위 3개 카테고리 조회

---

##### 📝 과제 4. 주문별 총 결제 금액 계산 (3개 테이블)

- **사용 테이블:** `orders`, `order_items`, `products`
- **문제:** 각 주문(`orders`) 건별로 구매한 상품의 총 결제 금액을 계산하시오. 총 결제 금액은 상품 단가(`price`)에 구매 수량(`quantity`)을 곱한 값의 합계로 계산한다.

- **출력 컬럼:** `order_id`, `order_date`, `total_order_amount`
- **학습 목표:**
  - `orders` → `order_items` → `products`로 이어지는 3개 테이블 조인
  - `price * quantity`를 이용한 상품별 금액 계산
  - `SUM()`을 이용한 주문별 총 결제 금액 집계
  - `GROUP BY`를 이용한 주문 단위 그룹화

---

##### 📝 과제 5. 성별(Gender)에 따른 총 상품 구매 수량 (3개 테이블)

- **사용 테이블:** `customers`, `orders`, `order_items`
- **문제:** 고객의 성별(`gender`)에 따라 구매한 상품의 총수량(`quantity`의 합계)을 집계하시오.

- **출력 컬럼:** `gender`, `total_purchased_quantity`
- **학습 목표:**
  - `customers` → `orders` → `order_items`로 이어지는 3개 테이블 연속 조인
  - 외래키를 이용한 다중 테이블 조인
  - `SUM()`과 `GROUP BY`를 이용한 성별별 구매 수량 집계

---
