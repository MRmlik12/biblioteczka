from catana.services.email import Email


def test_email_send_run_fake_server():
    email = Email()
    email.send("example@example.com", "example@localhost.com", "TEST", "TEST")
    email.close_connection()
