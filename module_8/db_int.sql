/*
    Title: db_init.sql
    Author: Devin Latshaw
    Date: July 1st 2022
    Description: 
            1.  script used to initialize the pysports database
                will drop user pysports_user if exists and
                recreate user while granting privs.
            2.  Drops tabls player & team if exist and then 
                creates tables 
            3.  Fill sin the table with data
*/


-- drop test user if exists 
DROP USER IF EXISTS 'pysports_user'@'localhost';


-- create pysports_user and grant them all privileges to the pysports database 
CREATE USER 'pysports_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'pysp0rts';

-- grant all privileges to the pysports database to user pysports_user on localhost 
GRANT ALL PRIVILEGES ON pysports.* TO'pysports_user'@'localhost';


-- drop tables if they are present
DROP TABLE IF EXISTS player;
DROP TABLE IF EXISTS team;


-- create the team table 
CREATE TABLE team (
    team_id     INT             NOT NULL        AUTO_INCREMENT,
    team_name   VARCHAR(75)     NOT NULL,
    mascot      VARCHAR(75)     NOT NULL,
    PRIMARY KEY(team_id)
); 

-- create the player table and set the foreign key
CREATE TABLE player (
    player_id   INT             NOT NULL        AUTO_INCREMENT,
    first_name  VARCHAR(75)     NOT NULL,
    last_name   VARCHAR(75)     NOT NULL,
    team_id     INT             NOT NULL,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team 
    FOREIGN KEY(team_id)
        REFERENCES team(team_id)
);


-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Blue', 'Blue Jay');

INSERT INTO team(team_name, mascot)
    VALUES('Team Red', 'Fire');


-- insert player records 
INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Nathan', 'Wilcox', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Kory', 'Cubin', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jackie', 'Disco', (SELECT team_id FROM team WHERE team_name = 'Team Blue'));

INSERT INTO player(first_name, last_name, team_id) 
    VALUES('Jim', 'Black', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Jerry', 'Kerry', (SELECT team_id FROM team WHERE team_name = 'Team Red'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('Bill', 'Guy', (SELECT team_id FROM team WHERE team_name = 'Team Red'));
	