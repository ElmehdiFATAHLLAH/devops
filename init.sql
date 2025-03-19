USE students_db;

CREATE TABLE IF NOT EXISTS students (
	id INT AUTO_INCREMENT PRIMARY KEY,
	first_name VARCHAR(255) NOT NULL,
	last_name VARCHAR(255) NOT NULL,
	age INT NOT NULL,
	email VARCHAR(255) NOT NULL
);

INSERT INTO students (first_name,last_name,age,email) VALUES
('Yassine', 'Rmidi',20,'yassine.rmidi@estc.ma');


