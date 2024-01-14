import pytest
from functions.similarity import minimal_edit_distance


@pytest.mark.parametrize(
    "string1,string2,answer", [
        (
            "intention",
            "execution",
            8
        )
    ]
)
def test_minimal_edit_distance(string1, string2, answer):
    result = minimal_edit_distance(string1, string2)

    assert result == answer