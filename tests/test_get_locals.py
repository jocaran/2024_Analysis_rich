import sys
from rich.traceback import Traceback

def izvuci_kljuceve(trace):
    return [
        key
        for stack in trace.stacks
        for frame in stack.frames
        if frame.locals
        for key in frame.locals
    ]

def extract_sa_lokalnim(hide_dunder, hide_sunder):
    try:
        __dunder = "dunder"
        _sunder = "sunder"
        vidljiva = "vidljiva"
        raise ValueError("test")
    except ValueError:
        exc_type, exc_value, tb = sys.exc_info()
        return Traceback.extract(
            exc_type, exc_value, tb,
            show_locals=True,
            locals_hide_dunder=hide_dunder,
            locals_hide_sunder=hide_sunder,
        )

def test_get_locals_bez_filtriranja():
    trace = extract_sa_lokalnim(False, False)
    kljucevi = izvuci_kljuceve(trace)
    assert "__dunder" in kljucevi
    assert "_sunder" in kljucevi

def test_get_locals_hide_dunder():
    trace = extract_sa_lokalnim(True, False)
    kljucevi = izvuci_kljuceve(trace)
    assert "__dunder" not in kljucevi
    assert "vidljiva" in kljucevi

def test_get_locals_hide_sunder():
    trace = extract_sa_lokalnim(False, True)
    kljucevi = izvuci_kljuceve(trace)
    assert "_sunder" not in kljucevi
    assert "vidljiva" in kljucevi