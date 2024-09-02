


#1
str = 'SANJU'
s = ''

for l in str:
    s = l + s
print(s)


#2
def Reverse(s):
    str=""
    for i in s:
        str = i + str
    return str

s = 'CRICKET'

print(Reverse(s))

#3

def reverse(r):
    if len(r) == 0:
        return r
    else:
        return reverse(r[1:]) + r[0]

r = 'PYTHON'

print(reverse(r))





# PRACTISE


x = "Tenet"
def reverse(x):
    str = ""
    for i in x:
        str = i + str
    return str


print(reverse(x))

