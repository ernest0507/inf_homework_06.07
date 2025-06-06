from re import findall

file = open('24_17685.txt')
a = file.readline()
file.close()

valid_exp = findall(r'(?:0|[1-9][0-9]*)(?:[+*](?:0|[1-9][0-9]*))*', a)
print(valid_exp[:50])
mlen = 0
for x in valid_exp:
    if eval(x) == 0:
        mlen = max(mlen, len(x))
print(mlen)

