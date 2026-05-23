import pytest
from rich.traceback import Traceback

def test_traceback_van_except_bloka():
    with pytest.raises(ValueError):
        Traceback()