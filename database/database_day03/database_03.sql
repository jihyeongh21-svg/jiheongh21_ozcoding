CREATE DATABASE pratice;
USE pratice;

-- 1. employees 테이블을 생성
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10 , 2)
);

-- 2. 직원데이터를  테이블에 추가
INSERT INTO employees (name,position,salary) VALUES('혜린','PM',90000);
INSERT INTO employees (name,position,salary) VALUES('은우','Frontend',80000);
INSERT INTO employees (name,position,salary) VALUES('가을','Backend',92000);
INSERT INTO employees (name,position,salary) VALUES('지수','Frontend',78000);
INSERT INTO employees (name,position,salary) VALUES('민혁','Frontend',96000);
INSERT INTO employees (name,position,salary) VALUES('하온','Backend',130000);

-- 3. 모든직원의 이름과 연봉정보만 조회
SELECT 
    name, salary
FROM
    employees;
-- 3.1 Frontend 직책을 가진 직원중에서 연봉이 90000 이하인 직원의 이름과 연봉 조회
SELECT 
    name, salary
FROM
    employees
WHERE
    position = 'Frontend'
        AND salary <= 90000;
        
-- 3.2 PM 직책을 가진 모든 직원의 연보을 10% 이상한 후 그 결괴를 확인 하세요
SEt sql_safe_updates = 0; -- safe update 해제 일반 키를 사용해서 수정 허용
UPDATE employees 
SET 
    salary = salary * 1.1
WHERE
    position = 'PM';

SELECT 
    *
FROM
    employees
WHERE
    position = 'PM';

-- 3.3 모든 Backend 직책을 가진 직원의 연봉을 5% 인상
UPDATE employees 
SET 
    salary = salary * 1.05
WHERE
    position = 'Backend';
SELECT *
From employees
where position = 'Backend';

-- 3.4 민혁사원의 데이터를 삭제
DELETE FROM employees 
WHERE
    name = '민혁';
SET SQL_SAFE_UPDATES = 1; -- SAFE UPDATE 다시 활성화
-- 3.5 모든 직원의 postion별 평균연봉을 조회
SELECT 
    position, AVG(salary) AS avg_salary
FROM
    employees
GROUP BY position;
-- 3.6 employees 테이블을 삭제 
DROP TABLE employees;