from src.app.ext.utils.strings import get_random_string


def test_get_random_string():
    assert 'd' in get_random_string(24, 'dead')
