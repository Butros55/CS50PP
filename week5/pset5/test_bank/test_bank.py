from bank import value

def test_value():
    assert value("hello") == 0
    assert value("hey") == 20
    assert value("whats up") == 100
    assert value("HELLO") == 0
    assert value("HEY") == 20
    assert value("WHATS UP") == 100