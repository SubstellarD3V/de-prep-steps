def sum_digits(input):

    total = 0
    if input is None:
        return None

    for digit in str(input):
        if digit == '-':
            continue
        elif digit.isdigit():
            total = total + int(digit)
            print(total)
    return total    
            

#print(sum_digits("")) # Expected = 0
#print(sum_digits(-99)) # Expected = 18
print(sum_digits(10.5)) # Expected = 6
print(sum_digits(20.0-5)) # Expected = 7
#print(sum_digits("123.a-4")) # Expected = 10