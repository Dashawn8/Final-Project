USE NCAT;

CREATE TABLE roles(
ID varchar(20),
role varchar(20),
primary key (ID)
);

INSERT INTO roles(ID,role) VALUES ('mgr' , 'Manager');
 INSERT INTO roles(ID,role) VALUES ('stu' , 'Student');