```mermaid
erDiagram
    %% 1. 사용자 및 주소
    USERS {
        int user_id PK
        string email
        string name
        string phone
        datetime created_at
    }
    USER_ADDRESSES {
        int address_id PK
        int user_id FK
        string address_line
        string city
        string postal_code
        boolean is_default
    }

    %% 2. 판매자 (오픈마켓)
    SELLERS {
        int seller_id PK
        string name
        string contact_email
        decimal rating
    }

    %% 3. 상품 및 카테고리
    CATEGORIES {
        int category_id PK
        string name
        int parent_id FK
    }
    PRODUCTS {
        int product_id PK
        int seller_id FK
        int category_id FK
        string name
        decimal price
        int stock_quantity
    }

    %% 4. 쇼핑 편의 기능 (장바구니, 위시리스트)
    CART {
        int cart_id PK
        int user_id FK
        datetime updated_at
    }
    CART_ITEMS {
        int item_id PK
        int cart_id FK
        int product_id FK
        int quantity
    }
    WISHLISTS {
        int wishlist_id PK
        int user_id FK
        int product_id FK
        datetime added_at
    }

    %% 5. 주문 및 결제
    ORDERS {
        int order_id PK
        int user_id FK
        int address_id FK
        string status
        decimal total_amount
        datetime created_at
    }
    ORDER_ITEMS {
        int item_id PK
        int order_id FK
        int product_id FK
        int quantity
        decimal unit_price
    }
    PAYMENTS {
        int payment_id PK
        int order_id FK
        string method
        string status
    }
    REVIEWS {
        int review_id PK
        int user_id FK
        int product_id FK
        int rating
        text comment
    }

    %% 관계 정의
    USERS ||--o{ USER_ADDRESSES : has
    USERS ||--o{ ORDERS : places
    USERS ||--o{ REVIEWS : writes
    USERS ||--|| CART : owns
    USERS ||--o{ WISHLISTS : keeps

    SELLERS ||--o{ PRODUCTS : sells

    CATEGORIES ||--o{ PRODUCTS : contains

    CART ||--o{ CART_ITEMS : contains
    PRODUCTS ||--o{ CART_ITEMS : added_to
    PRODUCTS ||--o{ WISHLISTS : saved_in

    PRODUCTS ||--o{ ORDER_ITEMS : included_in
    PRODUCTS ||--o{ REVIEWS : has
    
    ORDERS ||--o{ ORDER_ITEMS : contains
    ORDERS ||--|| PAYMENTS : generates
    
    %% 주문 시 저장된 주소 사용
    USER_ADDRESSES ||--o{ ORDERS : used_for