from main import separate_the_chocolate


def test_one():
    chocolate = 'UUUU'
    result = separate_the_chocolate(2, 2, 4, chocolate)
    assert result == 12

