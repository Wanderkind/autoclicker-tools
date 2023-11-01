
import os

Dir = "C:/Users/User/Documents/카카오톡 받은 파일"
name = input().strip()
f = open(Dir + f"/{name}.txt", "r")
unparsed = f.read()

i = 90
while True:
    i += 1
    if unparsed[i:i+7] == '"items"':
        break

l = unparsed[1:i-1].split(',')

res = "{\n"
for item in l:
    res += '\t' + item.replace(':', " : ") + " ,\n"

res += '\t"items" : [\n'
i += 10

while True:
    res += "\t\t{\n"
    j = i
    while True:
        j += 1
        if unparsed[j] == '}':
            break
    l = unparsed[i:j].split(',')
    for item in l:
        res += "\t\t\t" + item.replace(':', " : ") + " ,\n"
    res = res[:-3] + "\n\t\t} ,\n"
    i = j + 1
    if unparsed[i] == ']':
        break
    i += 2

res = res[:-3] + '\n\t] ,\n\t"additional": {\n'

l = unparsed[i+16:].split(',')
for item in l:
    res += "\t\t" + item.replace(':',  " : ") + " ,\n"

res = res[:-5] + "\n\t}\n}"

f = open(Dir + f"/{name}.txt", 'w')
f.write(res)
f.close()