import pytest
def flatten(inputList):
    if inputList is None:
        raise TypeError
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in inputList), [])



def test_flatten():
    assert [1, 2, 3, 4, 5, 6, 7, 8] == flatten([[1], 2, [[3, 4], 5], [[]], [[[6]]], 7, 8, []])
    assert [] == flatten([])
    with pytest.raises(TypeError):
        flatten(None)