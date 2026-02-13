CREATE DATABASE GearWiki;
USE GearWiki;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    base_atk INT DEFAULT 0,
    base_def INT DEFAULT 0
);

CREATE TABLE sets (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    set_name VARCHAR(255) NOT NULL,
    effect VARCHAR(255)
);

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    item_atk INT DEFAULT 0,
    item_def INT DEFAULT 0,
    set_id INT,
    FOREIGN KEY (set_id) REFERENCES sets(set_id) ON DELETE SET NULL,
    UNIQUE (item_id, parts)
);

CREATE TABLE equip (
    equip_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_id INT,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id, parts) REFERENCES items(item_id, parts) ON DELETE CASCADE,
    UNIQUE (user_id, parts)
);

CREATE TABLE wishlists (
    wishlist_id INT AUTO_INCREMENT PRIMARY KEY,
    wishlist_name VARCHAR(255) NOT NULL,
    user_id INT,
    item_id INT,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id, parts) REFERENCES items(item_id, parts) ON DELETE CASCADE,
    UNIQUE (user_id, wishlist_name, parts)
);


CREATE DATABASE GearWiki;
USE GearWiki;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    base_atk INT DEFAULT 0,
    base_def INT DEFAULT 0
);

CREATE TABLE sets (
    set_id INT AUTO_INCREMENT PRIMARY KEY,
    set_name VARCHAR(255) NOT NULL,
    effect VARCHAR(255)
);

CREATE TABLE items (
    item_id INT AUTO_INCREMENT PRIMARY KEY,
    item_name VARCHAR(255) NOT NULL,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    item_atk INT DEFAULT 0,
    item_def INT DEFAULT 0,
    set_id INT,
    FOREIGN KEY (set_id) REFERENCES sets(set_id) ON DELETE SET NULL,
    UNIQUE (item_id, parts)
);

CREATE TABLE equip (
    equip_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    item_id INT,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id, parts) REFERENCES items(item_id, parts) ON DELETE CASCADE,
    UNIQUE (user_id, parts)
);

CREATE TABLE wishlists (
    wishlist_id INT AUTO_INCREMENT PRIMARY KEY,
    wishlist_name VARCHAR(255) NOT NULL,
    user_id INT,
    item_id INT,
    parts ENUM('HELMET', 'CHESTPLATE', 'GAUNTLETS', 'LEGGINGS', 'BOOTS') NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id, parts) REFERENCES items(item_id, parts) ON DELETE CASCADE,
    UNIQUE (user_id, wishlist_name, parts)
);


-- 유저 생성
INSERT INTO users (user_name, password) VALUES ('전설의용사', '1234');

-- 세트 생성
INSERT INTO sets (set_name, effect) VALUES ('드래곤 세트', '공격력 +50%');

-- 아이템 생성 (드래곤 세트 ID: 1 가정)
INSERT INTO items (item_name, parts, set_id) VALUES 
('드래곤 투구', 'HELMET', 1),
('드래곤 갑옷', 'CHESTPLATE', 1);

-- 정상 장착 (성공)
INSERT INTO equip (user_id, item_id, parts) VALUES (1, 1, 'HELMET');

-- ★오류 테스트★: 투구 아이템(1번)을 다리(LEGGINGS)에 껴보기
-- 결과: Error Code: 1452 (Foreign key constraint fails) -> 성공적으로 방어됨!
INSERT INTO equip (user_id, item_id, parts) VALUES (1, 1, 'LEGGINGS');

-- '최강세팅'이라는 이름으로 2개 아이템 한번에 저장
INSERT INTO wishlists (user_id, wishlist_name, item_id, parts) VALUES 
(1, '최강세팅', 1, 'HELMET'),
(1, '최강세팅', 2, 'CHESTPLATE');