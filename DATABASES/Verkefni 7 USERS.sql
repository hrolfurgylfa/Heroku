DROP DATABASE IF EXISTS 2109013290_Verkefni_7_VEB;
CREATE DATABASE 2109013290_Verkefni_7_VEB;
USE 2109013290_Verkefni_7_VEB;

CREATE TABLE USERS (
	USER_USERNAME VARCHAR(99) PRIMARY KEY NOT NULL,
	USER_PASSWORD VARCHAR(99) NOT NULL,
    USER_NAME VARCHAR(99) NOT NULL
);
INSERT INTO
	USERS(USER_USERNAME, USER_PASSWORD, USER_NAME)
VALUES
	("admin","admin","admin"),
    ("hrolfur","H@ck$","Hrólfur");
    
# Fyrir Python
INSERT INTO USERS(USER_USERNAME, USER_PASSWORD, USER_NAME) VALUES ("admin","admin","admin")