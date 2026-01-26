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


