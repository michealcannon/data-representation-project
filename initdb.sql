use datarepresentation;

create table students(
    id int not null auto_increment,
    first_name varchar(250),
    surname varchar(250),
    grade int,
    absences int,
    primary key (id)
    );

create table registrations(
    id int not null auto_increment,
    email varchar(250),
    password varchar(250),
    primary key (id)
    );