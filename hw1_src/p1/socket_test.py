import socket

operator = {
    '+': "addition",
    '-': "subtraction",
    '*': "multiplication",
    '/': "division",
    '^': "power",

}

e = input("input: ")
for o in operator.keys():
    if o in e:
        l, c, r = e.partition(o)
        l = int(l)
        r = int(r)
        if(c == '+'):
            print(l+r)
        elif(c == '-'):
            print(l-r)
        elif(c == '*'):
            print(l*r)
        elif(c == '/'):
            print(l/r)
        elif(c == '^'):
