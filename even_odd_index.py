''' Given a string, S, of length N that is indexed from  0 to N-1, print its even-indexed and odd-indexed characters as  space-separated strings on a single line (see the Sample below for more detail).

Note: 0  is considered to be an even index.'''

t = int(input())
for _ in range(t):
    s = str(input())
    a = []
    b = []
    for i in range(len(s)):
        if i % 2 == 0:
            a.append(s[i])
        else:
            b.append(s[i])
    print(''.join(a) , ''.join(b))
