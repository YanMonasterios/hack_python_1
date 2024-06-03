"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    result = [0,1,2,3,4,5]
    for i in result:
        print(i)
    return result


print(fn_hack_6())