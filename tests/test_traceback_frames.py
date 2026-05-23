import sys
from rich.traceback import Traceback

def test_extract_ima_frejmove():
    def unutrasnja_funkcija():
        raise ValueError("greska")

    try:
        unutrasnja_funkcija()
    except ValueError:
        exc_type, exc_value, tb = sys.exc_info()
        trace = Traceback.extract(exc_type, exc_value, tb)

    frame_imena = [f.name for f in trace.stacks[0].frames]
    assert "unutrasnja_funkcija" in frame_imena