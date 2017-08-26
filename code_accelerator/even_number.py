def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

is_even(14)

def test_is_even():
    assert is_even(2) == True
    assert is_even(3) == False
    assert is_even(8) == True
    assert is_even(100) == True
    assert is_even(101) == False
    print("YOUR CODE IS CORRECT")

test_is_even()




def bonus_challenge(number):
    return number % 2 == 0
    
