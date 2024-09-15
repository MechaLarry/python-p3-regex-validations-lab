# tests/test_regex.py

from regex import name_regex, phone_regex, email_regex

def test_name_regex():
    assert name_regex.fullmatch("John Cena")
    assert not name_regex.fullmatch("john cena")

def test_phone_regex():
    assert phone_regex.fullmatch("555-555-5555")
    assert not phone_regex.fullmatch("555555555")

def test_email_regex():
    assert email_regex.fullmatch("john.cena@wwe.com")
    assert not email_regex.fullmatch("john$cena@wwe.com")
