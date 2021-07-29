import mock

import catana.workers.celery as email_reminder


def test_book_reminder():
    result = email_reminder.refresh_borrow_list()
    assert result
