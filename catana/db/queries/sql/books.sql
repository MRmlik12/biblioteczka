--name: get_books

SELECT *
FROM books --name: get_book

SELECT *
FROM books
WHERE id=:book_id
LIMIT 1; --name: assign_user


UPDATE books
SET is_borrowed=TRUE,
                user_borrow_id=:user_id
WHERE id=:book_id --name: return_book

    UPDATE books
    SET is_borrowed=FALSE,
                    user_borrow_id=NULL WHERE id=:book_id
    AND user_borrow_id=:user_id