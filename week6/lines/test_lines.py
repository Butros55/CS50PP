from lines import get_lines, open_file
import sys, pytest

def test_get_lines():
    assert get_lines(open("files/names7.py")) == 6





def test_errors():
    with pytest.raises(SystemExit):
        sys.argv[1] = "files/invalid_extension.txt"
        assert open_file() == "File does not exist"