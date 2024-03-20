from numb3rs import validate

def test_numbers():
    assert validate("192.168.0.1") == True
    assert validate("255.256.256.256") == False
    assert validate("25616801") == False
    assert validate("192.168.0.1.0") == False


def test_alphas():
    assert validate("cat") == False
    assert validate("DOG") == False