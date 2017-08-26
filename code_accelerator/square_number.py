# 1 input
# number based output: number ** 2

def square_number(number):
    return number ** 2

print(square_number(2))



# test code assertions

def test_square_number():
    assert square_number(2) == 4
    assert square_number(8) == 64
    assert square_number(10) == 100
    print("YOUR CODE IS CORRECT!")

test_square_number()



        
