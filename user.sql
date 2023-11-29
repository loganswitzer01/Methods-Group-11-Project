BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "inventory" (
	"ISBN"	INTEGER NOT NULL UNIQUE,
	"Title"	TEXT NOT NULL,
	"Author"	TEXT NOT NULL,
	"Genre"	TEXT NOT NULL,
	"Pages"	INTEGER NOT NULL,
	"ReleaseDate"	TEXT NOT NULL,
	"Stock"	INTEGER NOT NULL,
	PRIMARY KEY("ISBN")
);
INSERT INTO "inventory" VALUES (60765542,'The Lion the Witch and the Wardrobe','C. S. Lewis','',77,'',9);
INSERT INTO "inventory" VALUES (140268863,'The Oddessey','Homer','Epic Poetry',541,'1614',11);
INSERT INTO "inventory" VALUES (340068655,'Great Expectations','Charles Dickens','Novel',410,'1861',16);
INSERT INTO "inventory" VALUES (375756817,'Adventures of Tom Sawyer','Mark Twain','',270,'',1);
INSERT INTO "inventory" VALUES (399501487,'Lord of the Flies','William Golding','',336,'',4);
INSERT INTO "inventory" VALUES (439784549,'Harry Potter and the Half Blood Prince','J. K. Rowling','',672,'',3);
INSERT INTO "inventory" VALUES (446310786,'To Kill a Mockingbird','Harper Lee','Tragedy',336,'July 11, 1960',5);
INSERT INTO "inventory" VALUES (451524934,'1984','George Orwell','Dystopian',328,'June 8, 1949',14);
INSERT INTO "inventory" VALUES (582002648,'Adventures of Huckleberry Finn','Mark Twain','',224,'',7);
INSERT INTO "inventory" VALUES (671555855,'A Tale of Two Cities','Charles Dickens','',0,'',10);
INSERT INTO "inventory" VALUES (684164981,'The Great Gatsby','F. Scott Fitzgerald','Tragedy',114,'April 10, 1925',8);
INSERT INTO "inventory" VALUES (1451673310,'Fahrenheit 451','Ray Bradbury','Dystopian',249,'October 19, 1953',7);
INSERT INTO "inventory" VALUES (1453065989,'Oliver Twist','Charles Dickens','',608,'',7);
INSERT INTO "inventory" VALUES (1566192633,'Moby Dick','Herman Melville','Adventure Fiction',652,'October 18, 1851',5);
INSERT INTO "inventory" VALUES (8175993162,'Frankenstein','Mary Shelley','',118,'',21);
COMMIT;
