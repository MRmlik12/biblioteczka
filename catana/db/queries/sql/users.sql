--name: create_user_account

INSERT INTO users(id, username, surname, email, salt, hashed_password, phone_number, created_at)
VALUES (:id,
        :username,
        :surname,
        :email,
        :salt,
        :hashed_password,
        :phone_number,
        :created_at)