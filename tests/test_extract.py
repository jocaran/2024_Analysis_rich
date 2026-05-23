import sys
from rich.traceback import Traceback

def test_extract_vraca_trace():
    try:
        raise RuntimeError("test greska")
    except RuntimeError:
        exc_type, exc_value, tb = sys.exc_info()
        trace = Traceback.extract(exc_type, exc_value, tb)

    assert len(trace.stacks) == 1
    assert trace.stacks[0].exc_type == "RuntimeError"
    assert trace.stacks[0].exc_value == "test greska"