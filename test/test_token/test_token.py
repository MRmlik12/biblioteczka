import pytest

from catana.services.token import get_email_from_token


def test_email_from_token_raises_ValueError():
    with pytest.raises(ValueError) as e:
        get_email_from_token("xDKt7PNPP8NANdoraFTUKBBfhusCCvuCog==")
    assert "unable to decode JWT token" in str(e.value)
