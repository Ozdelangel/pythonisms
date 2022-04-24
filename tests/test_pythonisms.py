from pythonisms import __version__
from pythonisms.python_iterators import Stack, Node

def test_version():
    assert __version__ == '0.1.0'
def test_for_in():
    fighters = Stack(('rampage','pantera','rumble'))
    fighters_list = []
    for fighter in fighters:
        fighters_list.append(fighter)
    assert fighters_list == ['rampage', 'pantera','rumble']
def test_list_comprehension():
    fighters = Stack(('rampage','pantera','rumble'))
    fighters_list = [fighter.upper() for fighter in fighters]
    assert fighters_list == ['RAMPAGE','PANTERA','RUMBLE']

def test_list_cast():
    fighters_list = ['rampage', 'pantera','rumble']
    fighters = Stack(fighters_list)
    assert list(fighters) == fighters_list

