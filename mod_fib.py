cache = dict()
mod = dict()
# iterative
def fib_iterative(n):
    first, second = 0, 1
    for i in range(n):
        first, second = first + second, first
        cache[i] = first
def mod_fib(n, m):
    # Initialization
    mod[0]=0
    mod[1]=1
    flag = False
    for i in range(2,n+1):
        mod[i]=((mod[i-2]+mod[i-1])%m)
        # This if-statement checks if we are at the end of the period
        # in order to find the length of the period.
        if ((mod[i-1] == 0) and (mod[i] == 1)):
            flag = True
            length = i-1
            break
    if flag == False:
        return mod[n]
    else:
        temp = n % length
        return mod[temp]

def test_mod_fib():
    fib_iterative(20)
    assert cache[1]%7 == mod_fib(2,7) 
    assert cache[2]%7 == mod_fib(3,7) 
    assert cache[3]%7 == mod_fib(4,7) 
    assert cache[4]%7 == mod_fib(5,7) 
    assert cache[5]%7 == mod_fib(6,7) 
    assert cache[6]%7 == mod_fib(7,7) 
    assert cache[7]%7 == mod_fib(8,7) 
    assert cache[8]%7 == mod_fib(9,7) 
    assert cache[15]%7 == mod_fib(16,7) 
    assert cache[17]%7 == mod_fib(18,7) 
    fib_iterative(5000)
    assert cache[4999]%1357 == mod_fib(5000,1357)
    fib_iterative(135789)
    assert cache[124578]%999 == mod_fib(124579,999)

if __name__ == '__main__':
    n = 10**40  # nth fibonacci
    m = 10**6+7 # mod
    print(mod_fib(n,m))
    # test_mod_fib()
   
