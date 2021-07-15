--name: get_books

SELECT *
FROM books --name: assign_user

UPDATE books
SET is_borrowed=TRUE,
                user_borrow_id=:user_id
WHERE id=:book_id