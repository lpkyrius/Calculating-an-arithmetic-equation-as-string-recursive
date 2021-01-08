
# ============================================
# Calculating a string expression
# --------------------------------------------
# given an arithmetic equation as a string. This equation will have single digits 0-9, 
# addition, subtraction, multiplication, and parentheses.
# Here's a function that takes this equation and calculates the correct answer.
# Example inputs include 1+1 and 2*(1+9)-((2+5)-9).
# --------------------------------------------
#  That's not the best solution, it still needs improvements. But offers you an idea to start
# ============================================

import re

def recursionX(the_expression):
    
    # let's start with parenthesis
    openning = the_expression.rfind('(') # last occurrence of '('
    if openning != -1: # doesn't find '('
    
        #second_openning = the_expression.find('(',openning+1)
        closing = the_expression.find(')',openning) 
        result = calculate(the_expression[openning+1:closing])
        result = recursionX(the_expression[:openning]+str(result)+the_expression[closing+1:])
    
    else:
    
        # now * (multiplication)
        multi = the_expression.find('*')

        if multi != -1:
            pos = len(re.findall(r'\d+',the_expression)[0])+1            
            final_pos = pos+len(re.findall(r'\d+',the_expression)[1])
            result = recursionX(str(calculate(the_expression[:final_pos]))+the_expression[final_pos:])
        else:
            # finally simple operations (+/-)
            result = calculate(the_expression)
    return result
    
    
def calculate(simple_expression):
    print(f'Calculating... {simple_expression}')
    
    char_to_check = ['+','-','*']
    for char in char_to_check:
        pos = simple_expression.find(char)
        if pos > -1:
            break 
    
    operator = simple_expression[pos:pos+1]
    first = simple_expression[:pos]
    second = simple_expression[pos+1:]

    if operator == '+':
        #return int(simple_expression[0:1])+int(simple_expression[2:3])
        return int(first)+int(second)
    elif operator == '-':
        return int(first)-int(second)
    else:
        return int(first)*int(second)


if __name__ == '__main__':

    the_expression = '1+1'

    print(f'Calculating... {the_expression}')

    result = recursionX(the_expression)

    print(f'The result of {the_expression} is {result}\n')

    the_expression = '2*(1+9)-((2+5)-9)'

    print(f'Calculating... {the_expression}')

    result = recursionX(the_expression)

    print(f'The result of {the_expression} is {result}\n')
