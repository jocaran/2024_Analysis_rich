import sys
import pytest
from rich.traceback import Traceback
from rich.console import Console
from io import StringIO

@pytest.mark.skipif(sys.version_info < (3, 11), reason="ExceptionGroup dostupan od Python 3.11")
def test_exception_group():
    try:
        raise ExceptionGroup("vise gresaka", [
            ValueError("greska 1"),
            RuntimeError("greska 2"),
        ])
    except ExceptionGroup:
        tb = Traceback()

    console = Console(file=StringIO(), color_system=None)
    console.print(tb)
    output = console.file.getvalue()

    assert "ExceptionGroup" in output
    assert "ValueError" in output
    assert "RuntimeError" in output