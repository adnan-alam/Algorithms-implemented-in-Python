
# algorithm to find if a number is Prime or not

from math import sqrt

for _ in range(int(input())):
    n = int(input())
    sq = sqrt(n)
    i = 2
    if n == 1:
        print("Not prime")
    else:
        while i <= sq:
            if n%i == 0:
                print("Not prime")
                break
            i += 1
        else:
            print("Prime")
