create table users (
  id integer primary key,
  username varchar(25),
  email varchar(100),
  salt varchar(32),
  hash varchar(128),
);

create table sessions (
  id integer primary key,
  id_session varchar(32),
  email varchar(100)
);

insert into users (username, email, salt, hash) values ('toto', 'toto@gmail.com', '6994a0ba08354a28937c46033232381b', 'd93a90ba5ecb43b5308450990911def502b68eaa588f4eab699b0fd5e0e35e11fa035b7ffb5c0df51db01b0edf2747d84d8e12c43dabdf6f1b119b795bb7b9cd');
