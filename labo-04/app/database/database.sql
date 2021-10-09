-- TODO: Complete initial DB
CREATE TABLE individual (
    id integer primary key,
    firstname varchar(500),
    lastname varchar(500),
    age INTEGER
);

INSERT INTO individual(firstname, lastname, age) values ('Dominic', 'toto', 25);
INSERT INTO individual(firstname, lastname, age) values ('Alena', 'titi', 25);
INSERT INTO individual(firstname, lastname, age) values ('Tomtom', 'tata', 35);
INSERT INTO individual(firstname, lastname, age) values ('Michael', 'Jackson', 56);
