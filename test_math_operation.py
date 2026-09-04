from math_operation import add,subtract,multiply,divide


def test_add():
    assert add(10,5)==15
    assert add(2, 3) == 5
    assert add(-5, 5) == 0

    
def test_subtract():
    assert subtract(10, 5) == 5
    
def test_multiply():
    assert multiply(10, 5) == 50
    
def test_divide():
    assert divide(10, 5) == 2
    assert divide(10, 0) == "second number can not be 0"
    
