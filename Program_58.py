# Recursion in Python

def my_function(k):
    if(k>0):
        result=k+my_function(k-1)
    else:
        result=0
    return result
print(my_function(6))
