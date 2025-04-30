USE NCAT;

CREATE TABLE rosterclass(
rosterid INT,
userid INT,
Primary key (rosterid, userid),
foreign key (rosterid) references roster (ID),
foreign key (userid) references users (ID)
);

	insert into rosterclass (rosterid,userid) values (1,2);
    select * from rosterclass;