BEGIN TRANSACTION;

CREATE TABLE IF NOT EXISTS "Cart" (
       "cart_id" INTEGER NOT NULL UNIQUE,
       "user_id" INTEGER NOT NULL UNIQUE,
       "quanity" INTEGER NOT NULL,
       "book_id" INTEGER NOT NULL,
       PRIMARY KEY("cart_id")

);
INSERT INTO "Cart" VALUES (0001, 'agb44@msstate.edu','', Aiden', 
