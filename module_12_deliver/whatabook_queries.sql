/*
    Title: whatabook_queries.sql
    Author: Devin Latshaw
    Date: 7/15/2022
    Description: Queries for the whatabook prgoram e.g. view a users wishlist items, store's location, etc
*/

/*
    Query to view a user's wishlist
*/
SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.autor FROM wishlist
    Inner Join user ON wishlist.user_id = user.user_id
    Inner Join book ON wishlist.book_id = book.book_id
WHERE user.user_id =1;

/*
   Query for store 
*/
SELECT store_id, locale from store;

/*
    Query for viewing Books & details
*/
SELECT book_id, book_name, author, details from book;

/*
    Query to view books that are NOT in a wishlist of a user
    user_id value will need to be replcae with input from user 
    from the program
*/
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 1);

/*
    Insert statement to add a new book to a users wishlist. 
    user_id & book_id value will need to be replcae with input from user 
    from the program
*/
INSERT INTO wishlist(user_id, book_id)
    VALUES(1, 9)

/*
    Remove a book from the user's wishlist.
    user_id & book_id value will need to be replcae with input from user 
    from the program
*/
DELETE FROM wishlist WHERE user_id = 1 AND book_id = 9;