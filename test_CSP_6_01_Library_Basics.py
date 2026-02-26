import CSP_6_01_Library_Basics as HW
from CSP_6_01_Library_Basics import analyze_scores
from CSP_6_01_Library_Basics import sanitize_usernames
from CSP_6_01_Library_Basics import search_and_report

def test_process_expenses():
    assert HW.process_expenses([12,50,412,68]) == [13.8,57.5,473.8,78.2]
    assert HW.process_expenses([912,112,32,82]) == [1048.8,128.8,36.8,94.3]
    assert HW.process_expenses([52,344,142,100]) == [59.8,395.6,163.3,115]

def test_analyze_scores(monkeypatch):
    inputs = iter([
        "70",
        "85",
        "90"
    ])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    highest, average = analyze_scores(3)

    assert highest == 90.0
    assert average == 81.66666666666667

def test_sanitize_usernames():
    strings = ["Hello World", "PyTest IS FuN", "DATA"]
    result = sanitize_usernames(strings)

    assert result == ["helloworld", "pytestisfun", "data"]

def test_identify_outliers():
    assert HW.identify_outliers([100,23,5,410,123]) == [410,123]
    assert HW.identify_outliers([912,321,23,49,111]) == [912,321,111]
    assert HW.identify_outliers([101,61,77,12,99]) == [101]

def test_identify_outliers(monkeypatch):
    items = ["  apple ", " banana", "cherry ", " date"]

    monkeypatch.setattr("builtins.input", lambda _: "cherry")

    result = search_and_report(items)

    assert result == 2