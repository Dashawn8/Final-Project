use NCAT;

CREATE TABLE Users(
ID int auto_increment,
username VARCHAR(20),
userpassword VARCHAR(20),
roleID VARCHAR(20),
fname VARCHAR(20),
lname VARCHAR(20),
majorID int,
foreign key (roleID) references roles (ID),
foreign key (majorID) references major (ID),
primary key (ID)
);

INSERT INTO Users(roleID, username, userpassword) VALUES ('mgr','Manager1','AggiePride1');
INSERT INTO Users (roleID,username,userpassword) VALUES ('stu','Student1','AggiePride2');

UPDATE Users
SET majorID = 1
WHERE ID = 2;


SELECT * FROM Users;
