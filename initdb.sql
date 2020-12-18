use datarepresentation;

create table students(
    id int not null auto_increment,
    first_name varchar(250),
    surname varchar(250),
    grade int,
    absences int,
    primary key (id)
    );