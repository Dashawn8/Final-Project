USE NCAT;

CREATE TABLE roster(
ID INT auto_increment,
class varchar(20),
code varchar(20),
primary key (ID)
);


insert INTO roster (class,code) values ('COMP267','401'),('COMP167','402');
SELECT * from roster;
