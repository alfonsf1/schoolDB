


CREATE TABLE professors ( id SERIAL PRIMARY KEY, professorName VARCHAR(100) NOT NULL );

CREATE TABLE classes ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, professorId INTEGER REFERENCES professors(id) );

CREATE TABLE students ( id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, graduationStatus BOOLEAN, birthday DATE, yearInCollege INTEGER, coursesTaking TEXT[] );

INSERT INTO classes (name, professorId) VALUES
('CPSC 120', 1),
('CPSC 121', 1),
('CPSC 131', 2),
('CPSC 440', 3),
('MATH 100', 2),
('MATH 140', 4),
('MATH 180', 4),
('MATH 220', 5),
('ENG 100', 5),
('ENG 140', 6),
('SCI 100', 6),
('SCI 200', 7),
('SCI 300', 7);

INSERT INTO professors (professorName) VALUES
('Dr. Leroy Jenkins'),
('Dr. Tracy McGrady'),
('Dr. Ray Lewis'),
('Dr. Gabriel Pec'),
('Dr. Kobe Bryant'),
('Dr. Derrick Henry'),
('Dr. Ed Reed');

INSERT INTO students (name, graduationStatus, birthday, yearInCollege, coursesTaking) VALUES
('Joanne Moore', FALSE, '01-01-2001', 3, ARRAY['CPSC 120', 'MATH 100', 'ENG 100, SCI 100']),
('Allyson Blackburn', TRUE, '02-02-2003', 4, ARRAY['CPSC 121', 'MATH 140', 'ENG 140, SCI 300']),
('Lavern Oliver', FALSE, '03-03-2004', 3, ARRAY['CPSC 131', 'MATH 100', 'ENG 100, SCI 100']),
('Wilmer Gates', TRUE, '04-04-2003', 4, ARRAY['CPSC 121', 'MATH 180', 'ENG 140, SCI 300']),
('Geraldine Castro', FALSE, '05-05-2002', 3, ARRAY['CPSC 131', 'MATH 140', 'ENG 100, SCI 100']),
('Norbert Tucker', TRUE, '06-06-2003', 4, ARRAY['CPSC 120', 'MATH 180', 'ENG 140, SCI 200']),
('Hollie Wiggins', FALSE, '07-07-2001', 1, ARRAY['CPSC 440', 'MATH 100', 'ENG 100, SCI 200']),
('Jackie Huff', TRUE, '08-08-2000', 4, ARRAY['CPSC 440', 'MATH 140', 'ENG 140, SCI 300']),
('Tia Macdonald', FALSE, '09-09-2000', 1, ARRAY['CPSC 120', 'MATH 100', 'ENG 140, SCI 200']),
('Melvin Conner', TRUE, '12-12-2000', 4, ARRAY['CPSC 121', 'MATH 220', 'ENG 100, SCI 100']),
('Shelton Fuller', FALSE, '10-02-2002', 3, ARRAY['CPSC 120', 'MATH 100', 'ENG 100, SCI 300']),
('Jordon Wells', TRUE, '01-16-2004', 4, ARRAY['CPSC 120', 'MATH 180', 'ENG 140, SCI 100']),
('Jolene Summers', FALSE, '09-02-1999', 3, ARRAY['CPSC 131', 'MATH 140', 'ENG 100, SCI 100']),
('Ericka Morrow', TRUE, '01-06-1997', 4, ARRAY['CPSC 121', 'MATH 100', 'ENG 140, SCI 200']),
('Art Rowland', FALSE, '06-02-2003', 1, ARRAY['CPSC 120', 'MATH 220', 'ENG 100, SCI 300']),
('Haywood Christensen', FALSE, '09-02-1999', 1, ARRAY['CPSC 440', 'MATH 220', 'ENG 140, SCI 100']),
('Rosetta Phillips', TRUE, '12-02-1994', 4, ARRAY['CPSC 121', 'MATH 100', 'ENG 100, SCI 200']),
('Geraldine Haynes', FALSE, '01-02-2000', 2, ARRAY['CPSC 131', 'MATH 180', 'ENG 140, SCI 100']),
('Sid Santos', FALSE, '01-02-2000', 1, ARRAY['CPSC 121', 'MATH 220', 'ENG 140, SCI 100']);

CPSC 120
CPSC 121
CPSC 131
CPSC 440

MATH 100
MATH 140
MATH 180
MATH 220

ENG 100
ENG 140

SCI 100
SCI 200
SCI 300
