from io import StringIO
from rich.console import Console
from rich.traceback import Traceback

def test_zero_division():
    try:
        1 / 0
    except ZeroDivisionError:
        tb = Traceback()  

    console = Console(file=StringIO(), color_system=None)
    console.print(tb)
    output = console.file.getvalue()

    assert "ZeroDivisionError" in output
