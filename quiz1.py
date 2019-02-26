# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers smaller than the length of L,
whose value is input by the user, and outputs two lists:
- a list M consisting of L's middle element, followed by L's first element,
  followed by L's last element, followed by L's second element, followed by
  L's penultimate element...;
- a list N consisting of L[0], possibly followed by L[L[0]], possibly followed by
  L[L[L[0]]]..., for as long as L[L[0]], L[L[L[0]]]... are unused, and then,
  for the least i such that L[i] is unused, followed by L[i], possibly followed by
  L[L[i]], possibly followed by L[L[L[i]]]..., for as long as L[L[i]], L[L[L[i]]]...
  are unused, and then, for the least j such that L[j] is unused, followed by L[j],
  possibly followed by L[L[j]], possibly followed by L[L[L[j]]]..., for as long as
  L[L[j]], L[L[L[j]]]... are unused... until all members of L have been used up.
'''

import sys
from random import seed, randrange

try:
    arg_for_seed, length = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length = int(arg_for_seed), int(length)
    if arg_for_seed < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(length) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
M = []
N = []

# Replace this comment with your code
L1=[0]*length
for a in range(0,length):
    L1[a]=L[a]
M=[0]*length
if length % 2 ==0:
    M[0] = L1.pop(int(length/2))
else:
    M[0] = L1.pop(int((length - 1) / 2))
for a in range(1,length):
    if ( a % 2 == 0 ):
        M[a] = L1.pop()
    else:
        M[a]=L1.pop(0)

L2 = [0]*length
for a in range(0, length):
    L2[a] = L[a]
N = [0] * length
a = 0
N[0] = L2[0]
L2[0] = -1
while True:
    m = N[a]
    if m >= length or m < 0:
        a += 1
        for index, b in enumerate(L2):
            if b == -1:
                continue
            else:
                N[a] = b
                L2[index] = -1
                break
    else:
        a += 1
        if L2[m] == -1:
            for n, b in enumerate(L2):
                if b == -1:
                    continue
                else:
                    N[a] = b
                    L2[n] = -1
                    break
        else:
            N[a] = L[m]
            L2[m] = -1
    if a == (length - 1):
        break


print('\nHere is M:')
print('  ', M)
print('\nHere is N:')
print('  ', N)
print('\nHere is L again:')
print('  ', L)
