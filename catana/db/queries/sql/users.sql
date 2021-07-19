--name: create_user_account

INSERT INTO users(id, username, surname, email, salt, hashed_password, phone_number, created_at)
VALUES (:id,
        :username,
        :surname,
        :email,
        :salt,
        :hashed_password,
        :phone_number,
        :created_at);--name: get_user_account


SELECT *
FROM users
WHERE email==:email
        AND hashed_password==:hashed_password
LIMIT 1; --name: get_user_login_credentials


SELECT salt,
       hashed_password
FROM users
WHERE email=:email
LIMIT 1;

--name: get_user_id

SELECT id
FROM users
WHERE email=:email
LIMIT 1;