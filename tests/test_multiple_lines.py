from io import StringIO
from rich.console import Console
from rich.traceback import Traceback


def test_iter_syntax_lines_vise_linija():
    try:
        raise RuntimeError("test")
    except RuntimeError:
        tb = Traceback()

    
    frame = tb.trace.stacks[0].frames[0]
    frame.last_instruction = ((1, 0), (5, 10))  

    console = Console(file=StringIO(), color_system=None)
    console.print(tb)
    output = console.file.getvalue()
    assert "RuntimeError" in output