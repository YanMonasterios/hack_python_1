"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = [5,4,3,2,1,0]
    i = 0
    while i < len(result):
        i += 1
    return result

print(fn_hack_7())