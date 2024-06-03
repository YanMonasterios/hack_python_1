"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1, 3, 5, 7, 9]
    result = result[1:4] # lista 0 1 3 5 7 9 , se indica que se tomara el valor despues de la posicion 1 hasta la posicion 4  
    return result

print(fn_hack_8())