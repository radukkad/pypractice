import pytest

from calculator import square
def main():
    test_positive()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9
def test_nagative():
    assert square(-3) == 9
    assert square(-1) == 1

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")

if __name__ == "__main__":
    main()