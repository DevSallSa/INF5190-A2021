-- TODO: Complete initial DB
CREATE TABLE books (
    id integer primary key,
    title varchar(500),
    FOREIGN KEY(author) REFERENCES author(id),
    created_at TEXT
);

CREATE TABLE author (
    id integer primary key,
    firstname varchar(500),
    lastname varchar(500),

)

INSERT INTO books(title, author, created_at) values ('My first super book', 1, "2020-01-01");
INSERT INTO books(title, author, created_at) values ('My second super book', 2, "2020-01-01");
INSERT INTO books(title, author, created_at) values ('My third super book', 3, "2020-01-01");
