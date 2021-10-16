-- TODO: Complete initial DB
CREATE TABLE books (
    id integer primary key,
    title varchar(500),
    sommaire text,
    created_at TEXT
);


INSERT INTO books(title, sommaire, created_at) values ('My first super book', "This book talk about the first super book", "2020-01-01");
INSERT INTO books(title, sommaire, created_at) values ('My second super book', "This book talk about the second super book", "2020-01-01");
INSERT INTO books(title, sommaire, created_at) values ('My third super book', "This book talk about the third super book", "2020-01-01");
