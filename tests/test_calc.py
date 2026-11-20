from calc import vat

def test_vat():
    assert vat(100) == 120.0

def test_zero_rate():
    assert vat(50, rate=0) == 50
