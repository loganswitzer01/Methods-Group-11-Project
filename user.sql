BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "user" (
	"userID" INTEGER NOT NULL UNIQUE,
	"Email"	TEXT NOT NULL,
	"Password" TEXT NOT NULL,
	"First Name"	TEXT NOT NULL,
	"Last Name"	TEXT NOT NULL,
	"Address"	TEXT NOT NULL,
	"City"	TEXT NOT NULL,
	"State" TEXT NOT NULL,
	"Zip" INTEGER NOT NULL,
	"Payment" TEXT NOT NULL,
	PRIMARY KEY("userID")
);
INSERT INTO "user" VALUES (0001,'agb444@msstate.edu','','Aiden','Baham','','','','','');
INSERT INTO "user" VALUES (0002,'jls1867@msstate.edu','','Logan','Switzer','','','','','');
INSERT INTO "user" VALUES (0003,'mbr260@msstate.edu','','Matthew','Rushing','','','','','');
COMMIT;
