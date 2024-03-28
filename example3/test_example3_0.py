from example3 import add
import pytest

def test_add_catch_error():
    with pytest.raises(ValueError):
        add('two', '3')
