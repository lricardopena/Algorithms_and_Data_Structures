import sys
import math


def binaryInsertion(A, L, R, k, previousm):
    if L >= R:
        A.insert(previousm, k)
        return A

    m = int(math.floor(L+R)/2)
    if A[m] > k:
        return binaryInsertion(A, L, m - 1 ,k, m)
    elif A[m] < k:
        return binaryInsertion(A, m + 1, R,k, m + 1)
    A.insert(m, k)
    return A

N, K = map(int,raw_input().strip().split(' '))
cookies = map(int,raw_input().strip().split(' '))
if cookies[0] >= K:
    print 0
elif len(cookies) < 2:
    print -1
else:
    d = 0
    while cookies[0] < K:
        if len(cookies) < 2:
            d = -1
            break
        A1, A2 = cookies[0:2]
        del cookies[0]
        del cookies [0]
        newcookie = A1 + 2 * A2
        cookies = binaryInsertion(cookies,0,len(cookies), newcookie,0)
        d += 1
    print d

sortedArray = []
for n in range(Q):
    inputs = map(str,raw_input().strip().split(' '))
    typeQuery = int(inputs[0])
    if len(inputs) > 1:
        k = int(inputs[1])
    if typeQuery == 1:
        sortedArray = binaryInsertion(sortedArray,0,len(sortedArray) - 1,k,0)
#n = int(raw_input().strip())
#arr = map(int,raw_input().strip().split(' '))