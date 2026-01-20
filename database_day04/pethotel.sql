/*
반려동물 호텔예약 시스템
요구사항
    1. 한 반력동물은 여러 번 예약 가능
    2. 예약은 객실정보와 연결 
        2.1 고객은 여러반력 정보를 가질 수 있다
    3. 예약 시 다양한 서비스도 함계 예약 할 수 있따
    
*/
-- 반려동물 호텔 예약 시스템 테이터 베이스 생성
CREATE database pethotel;
USE pethotel;

-- 고객 테이블 생성
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    phone VARCHAR(20) NOT NULL
);

-- 반려동물 테이블 생성
CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_type VARCHAR(30) NOT NULL,
    pet_info VARCHAR(255) NOT NULL,
    customer_id INT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id)
);

-- 객실 테이블 생성
CREATE TABLE rooms (
    room_id INT AUTO_INCREMENT PRIMARY KEY,
    room_num CHAR(3) NOT NULL,
    room_type VARCHAR(20) NOT NULL,
    room_price INT NOT NULL
);

-- 서비스 테이블 생성
CREATE TABLE services (
    serv_id INT AUTO_INCREMENT PRIMARY KEY,
    serv_name VARCHAR(20) NOT NULL,
    serv_type VARCHAR(20) NOT NULL,
    serv_price INT NOT NULL
);

-- 예약 테이블 생성
CREATE TABLE reservations (
    reserv_id INT AUTO_INCREMENT PRIMARY KEY,
    checkin DATE NOT NULL,
    checkout DATE NOT NULL, 
    customer_id INT NOT NULL,
    room_id INT NOT NULL,
    pet_id INT NOT NULL,
    FOREIGN KEY (customer_id)
        REFERENCES customers (customer_id),
    FOREIGN KEY (room_id)
        REFERENCES rooms (room_id),
    FOREIGN KEY (pet_id)
        REFERENCES pets (pet_id)
);

-- 예약 서비스 테이블 생성
CREATE TABLE reservation_services(
id INT AUTO_INCREMENT PRIMARY KEY,
reserv_id INT NOT NULL,
serv_id INT NOT NULL,
FOREIGN KEY(reserv_id) REFERENCES reservations(reserv_id),
FOREIGN KEY (serv_id) REFERENCES services(serv_id)
);