def add(first,second):
    return first+second

def subtract(first,second):
    return first-second

def multiply(first,second):
    return first*second

def divide(first,second):
    if second!=0:
        return first/second
    else:
        raise ValueError ("second number can not be 0")