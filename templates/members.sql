DROP DATABASE IF EXISTS members;
CREATE DATABASE members;

CREATE TABLE regmembers(
	firstName VARCHAR(20),
	lastName VARCHAR(30),
	age INTEGER,
	email VARCHAR(50));

INSERT INTO regmembers VALUES('Diego','Bustamante','21','thisisfake@fake.com');
INSERT INTO regmembers VALUES('Laura','Wilford','23','laurafakeemail@fake.com');
INSERT INTO regmembers VALUES('Prisila','Bustamante','22','silafake@fake.com');
INSERT INTO regmembers VALUES('Hasan','Shami','20','isntthisfake@fake.com');
