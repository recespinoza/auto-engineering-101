from chapters.ch2.addNumbers import add

def test_addingEvenNumbersReturnsEvenNumber():
    number = add(2, 2)
    assert number == 4
