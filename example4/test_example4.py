import pytest
from example4 import add


@pytest.mark.parametrize("a, b, expected",
                         [(2, 3, 5),
                          ('2', '3', 5),
                          ('two', '3', ValueError),
                          ],
                          ids=["adding numbers",
                               "str to int cast",
                               "ValueError exception",
                               ])
def test_add(a, b, expected):
    if expected == ValueError:
        with pytest.raises(ValueError):
            add(a, b)
    else:
        assert add(a, b) == expected
