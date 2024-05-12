import time


def test_start(parser, browser_dynamic):
    assert browser_dynamic.title == "Your Store"
