DROP USER IF EXISTS 'whatabook_user'@'localhost';

CREATE USER 'WHATABOOK_USER'@'LOCALHOST' IDENTIFIED WITH mysql_native_password by 'MySQL8IsGreat!';

GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

ALTER TABLE wishlist DROP FOREIGN KEY fk_book;
ALTER TABLE wishlist DROP FOREIGN KEY fk_user;

DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS book;
DROP TABLE IF EXISTS store;
DROP TABLE IF EXISTS wishlist;




CREATE TABLE user (
    user_id         INT             NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);


CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(200)    NOT NULL,
    PRIMARY KEY(book_id)
);

CREATE TABLE store (
    store_id    INT    NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE wishlist (
    wishlist_id     INT     NOT NULL    AUTO_INCREMENT,
    user_id         INT     NOT NULL,
    book_id         INT     NOT NULL,
    PRIMARY KEY(wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_id)
);

/*
    Inserting users
*/
INSERT INTO user(first_name, last_name)
    VALUES('Nathan', 'Wilcox');

INSERT INTO user(first_name, last_name)
    VALUES('Jim', 'Black');

INSERT INTO user(first_name, last_name)
    VALUES('Kory', 'Cubin');

/*
    Inserts books
*/
INSERT INTO book(book_name, author, details)
    VALUES('The Return of the King', 'J.R.Tolkien', 'The third part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Fellowship of the Ring', 'J.R.Tolkien', 'The first part of The Lord of the Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Two Towers', 'J.R.Tolkien', 'The second part of The Lord of The Rings');

INSERT INTO book(book_name, author, details)
    VALUES('The Hobbit or There and Back Again', 'J.R.Tolkien', 'Hobbit stuff');

INSERT INTO book(book_name, author, details)
    VALUES('Dune: Deluxe Edition', 'Frank Herbert', 'Delexue edition of Dune');

INSERT INTO book(book_name, author, details)
    VALUES("Charlotee's Web", 'E.B. White', 'Spider, pig, web what more you want?');

INSERT INTO book(book_name, author, details)
    VALUES('The Great Gatsby', 'F. Scott Fitzgerald', 'Some rich dude life');

INSERT INTO book(book_name, author, details)
    VALUES('The Lion, the Witch, and the Wardrobe', 'C.S. Lewis', 'Turkish delight is not that great!');

INSERT INTO book(book_name, author, details)
    VALUES('The Catcher and the Rye', 'J.D. Salinger', 'Fish and bread...joking');

/*
    inserts into store
*/
INSERT INTO store(locale)
    VALUES('4700 Baker Street Extension, Lakewood, NY, 14750');

/*
    inserts wishlist
*/

INSERT INTO wishlist(user_id, book_id) 
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Kory'), 
        (SELECT book_id FROM book WHERE book_name = 'The Lion, the Witch, and the Wardrobe')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Nathan'),
        (SELECT book_id FROM book WHERE book_name = 'The Catcher and the Rye')
    );

INSERT INTO wishlist(user_id, book_id)
    VALUES (
        (SELECT user_id FROM user WHERE first_name = 'Jim'),
        (SELECT book_id FROM book WHERE book_name = 'Dune: Deluxe Edition')
    );