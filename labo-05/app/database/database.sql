-- TODO: Complete initial DB
CREATE TABLE books (
    id integer primary key,
    title varchar(500),
    sommaire text,
    FOREIGN KEY(author) REFERENCES author(id),
    created_at TEXT
);

CREATE TABLE author (
    id integer primary key,
    firstname varchar(500),
    lastname varchar(500),
)

INSERT INTO books(title, author, created_at) values ('My first super book', "This book talk about the first super book",1, "2020-01-01");
INSERT INTO books(title, author, created_at) values ('My second super book', "This book talk about the second super book" ,2, "2020-01-01");
INSERT INTO books(title, author, created_at) values ('My third super book', "This book talk about the third super book" ,3, "2020-01-01");
