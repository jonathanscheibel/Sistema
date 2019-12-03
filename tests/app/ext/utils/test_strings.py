from src.app.ext.utils.strings import get_random_string


def test_get_random_string():
    assert 'a' in get_random_string(24, 'dead')
