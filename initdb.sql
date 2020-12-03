use datarepresentation;

create table books(
    id int not null auto_increment,
    title varchar(250),
    author varchar(250),
    price int,
    primary key (id)
    );