# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers, the largest possible value
and the length of L being input by the user, and generates:
- a list "fractions" of strings of the form 'a/b' such that:
    . a <= b;
    . a*n and b*n both occur in L for some n
    . a/b is in reduced form
  enumerated from smallest fraction to largest fraction
  (0 and 1 are exceptions, being represented as such rather than as 0/1 and 1/1);
- if "fractions" contains then 1/2, then the fact that 1/2 belongs to "fractions";
- otherwise, the member "closest_1" of "fractions" that is closest to 1/2,
  if that member is unique;
- otherwise, the two members "closest_1" and "closest_2" of "fractions" that are closest to 1/2,
  in their natural order.
'''


import sys
from random import seed, randint
from math import gcd


try:
    arg_for_seed, length, max_value = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, length, max_value = int(arg_for_seed), int(length), int(max_value)
    if arg_for_seed < 0 or length < 0 or max_value < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, max_value) for _ in range(length)]
if not any(e for e in L):
    print('\nI failed to generate one strictly positive number, giving up.')
    sys.exit()
print('\nThe generated list is:')
print('  ', L)

fractions = []
spot_on, closest_1, closest_2 = [None] * 3

# Replace this comment with your code

L2 = []
for i in L:
 if not i in L2:
        L2.append(i)
L2.sort()

F1 = []
L3 = []
for i in range(0, len(L2)):
    if L2[i] == 0:
        L3.append('0')
        F1.append('0')
        continue
    for j in range(i, len(L2)):
        m, n = int(L2[i]), int(L2[j])
        g = gcd(L2[i], L2[j])
        m /= g
        n /= g
        m, n = int(m), int(n)
        if f'{m}/{n}' in F1:
            continue
        L3.append(f'{m/n:0.5f}')
        F1.append(f'{m}/{n}')
L4 = []
for i in L3:
	L4.append(float(i))
a=5
b=0
while True:
    b+=1
    for i in range(0,len(L3)):
        if a > float(L3[i]):
            a = float(L3[i])
            f = i
        else:
            continue
    L3[f] = a =8
    if F1[f] == '1/1':
        fractions.append('1')
    else:
        fractions.append(F1[f])
    if b == len(L3):
        break


list.sort(L4)

if len(L4) == 0:
    pass
elif len(L4) == 1:
    closest_1 = fractions[0]
elif L4[0] > 0.5:
    closest_1 = fractions[0]
elif L4[len(L4) - 1] < 0.5:
    closest_1 = fractions[len(L4) - 1]
else:
    for i in range(0,len(L4)):
        if L4[i] == 0.5:
            spot_on = True
            break
        if L4[i] > 0.5:
            if (0.5 - L4[i - 1]) - (L4[i] - 0.5) < 0:
                closest_1 = fractions[i - 1]
                break
            elif (0.5 - L4[i - 1]) - (L4[i] - 0.5) > 0:
                closest_1 = fractions[i]
                break
            else:
                closest_1 = fractions[i - 1]
                closest_2 = fractions[i]
                break

print('\nThe fractions no greater than 1 that can be built from L, from smallest to largest, are:')
print('  ', '  '.join(e for e in fractions))
if spot_on:
    print('One of these fractions is 1/2')
elif closest_2 is None:
    print('The fraction closest to 1/2 is', closest_1)
else:
    print(closest_1, 'and', closest_2, 'are both closest to 1/2')

