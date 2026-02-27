import CSP_6_02_reading_files as HW


def test_toString():
    assert HW.toString("test1") == "Hello\nlol"
    assert HW.toString("test2") == "Hai\nHewo\nHow you doin"

def test_longestLine():
    assert HW.longestLine("test1") == "Hello\n"
    assert HW.longestLine("test2") == "How you doin"

def test_toBinary():
    assert HW.toBinary("01010101010100") == ['01010101', '010100']
    assert HW.toBinary("1010110111111010") == ['10101101', '11111010']