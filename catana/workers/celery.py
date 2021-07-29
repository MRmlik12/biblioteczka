"""Celery app"""
from datetime import datetime

from celery import Celery
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Session

from catana.core.config import (
    EMAIL,
    POSTGRESQL_CONNECTION_STRING,
    REDIS_CONNECTION_STRING,
)
from catana.core.email_templates import (
    RETURN_BORROWED_BOOK,
    RETURN_BORROWED_BOOK_SUBJECT,
)
from catana.models.domain.books import BookInDb
from catana.models.domain.users import UserInDb
from catana.services import email

db = create_engine(POSTGRESQL_CONNECTION_STRING).connect()
celery = Celery(
    "tasks", backend=REDIS_CONNECTION_STRING, broker=REDIS_CONNECTION_STRING
)


@celery.on_after_configure.connect
def setup_periodic_tasks(sender):
    """Celery on connect event for celery beat"""
    sender.add_periodic_task(60.0, refresh_borrow_list)


@celery.task
def refresh_borrow_list() -> bool:
    """Refresh borrower list, if succesfull return true"""
    try:
        session = Session(db.engine)
        books = session.query(BookInDb).all()
        for book in books:
            if book.is_borrowed and book.updated_at.month - datetime.now().month == 0:
                user = session.query(UserInDb).filter_by(id=book.user_borrow_id).first()
                email.Email().send(
                    EMAIL,
                    user.email,
                    RETURN_BORROWED_BOOK_SUBJECT,
                    RETURN_BORROWED_BOOK,
                )
        return True
    except:
        return False
