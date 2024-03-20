from twttr import shorten

def test_shorten():
    assert shorten("hello, world") == "hll, wrld"
    assert shorten("Hello, World") == "Hll, Wrld"
    assert shorten("H3llo, World") == "H3ll, Wrld"
    assert shorten("HEllo, WOrld") == "Hll, Wrld"
