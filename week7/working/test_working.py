from working import convert
import pytest

def test_time():
    assert convert("9:00 AM to 10:00 PM") == "09:00 to 22:00"
    assert convert("9 AM to 10 PM") == "09:00 to 22:00"
    assert convert("9 PM to 10 AM") == "21:00 to 10:00"
    assert convert("9:00 AM to 10:00 PM") == "09:00 to 22:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_alpha():
    with pytest.raises(ValueError):
        assert convert("cat AM to dog PM")
    with pytest.raises(ValueError):
        assert convert("9:00 AM 10:00 PM")
    with pytest.raises(ValueError):
        assert convert("13:00 AM to 14:00 PM")
