import sys; sys.path.append("..")
from pyDependabot.src.utils import get_if_possible
from pyDependabot.src.consts import NOT_POPULATED



def test_get_if_possible_returns_not_populated_when_element_not_found():
    mock = {}
    assert get_if_possible(mock, "s") == NOT_POPULATED

def test_get_if_possible_returns_not_populated_when_element_not_found_on_2nd_depth():
    mock = { "depth_1": {} }
    assert get_if_possible(mock, "depth_1.depth_2") == NOT_POPULATED

def test_get_if_possible_returns_not_populated_when_element_not_found_on_3nd_depth():
    mock = { "depth_1": { "depth_2":{} } }
    assert get_if_possible(mock, "depth_1.depth_2.depth_3") == NOT_POPULATED

def test_get_if_possible_returns_none_when_value_is_none():
    mock = {"x": None}
    assert get_if_possible(mock, "x") is None

def test_get_if_possible_returns_correct_value_when_value_exists():
    mock = {"x": "something"}
    assert get_if_possible(mock, "x") == "something"
