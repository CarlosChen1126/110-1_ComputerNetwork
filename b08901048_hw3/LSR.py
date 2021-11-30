import sys


def min_s(check, D, num):
    minn = 100000000
    for i in range(1, num+1):
        if (D[i] < minn and check[i-1] == 0):
            minn = D[i]
            ans = i
    return ans


def LSR(s, table, num):
    start = s
    P = []
    D = []
    check = []
    for i in range(0, num+1):
        P.append(0)
        # for j in range(0, num+1):
        #     P[i].append(0)
        D.append(-1)
    for i in range(0, num):
        check.append(0)

    check[s-1] = 1
    D[s] = 0
    P[s] = s
    keep = True

    t = 0
    for i in range(1, num+1):
        if i != start:
            if table[start][i] > 0:
                D[i] = table[start][i]
                P[i] = i
            else:
                D[i] = 10000000
    while(keep == True):
        # w = min(i for i in D if i > 0)
        w = min_s(check, D, num)
        # w = D.index(w)
        check[w-1] = 1
        for i in range(1, num+1):
            if check[i-1] == 0 and table[w][i] > 0:
                if D[w]+table[w][i] <= D[i]:
                    D[i] = D[w]+table[w][i]
                    P[i] = w
                    if table[start][P[i]] < 0:
                        P[i] = P[P[i]]
                    if P[i] != P[P[i]]:
                        P[i] = P[P[i]]
        # print(D)
        if 0 in check:
            keep = True
            # print("T")
        else:
            keep = False
            # print("F")
    return D, P


f = open(sys.argv[1], "r")
input_data = []
for line in f.readlines():
    input_data.extend(line.split())
f.close()
num = input_data[0]
num = int(num)
table = []

for i in range(0, num+1):
    table.append([])
    for j in range(0, num+1):
        table[i].append(-1)
for i in range(1, num*num+1):
    input_data[i] = int(input_data[i])
    if i % num != 0:
        table[((i-1)//num) + 1][i % num] = input_data[i]
    else:
        table[((i-1)//num) + 1][num] = input_data[i]
DD = []
PP = []
for i in range(1, num+1):
    D, P = LSR(i, table, num)
    DD.append(D)
    PP.append(P)
print(DD)
print(PP)

f = open(sys.argv[2], 'w')
for i in range(0, num):
    f.write("Routing table of router " + str(i+1)+"\n")
    for j in range(1, num+1):
        f.write(str(DD[i][j])+" "+str(PP[i][j])+"\n")
f.close()

# l = []
# l.append(1)
# D = [1, 1, 3, -1, 0]
# w = min(i for i in D if i > 0)
# w = D.index(w)
# print(w)
# if(l[w] != 1):
#     print(w)
# print(table[1][2])
# for i in range(1, len(table)):
#     for j in range(1, len(table[0])):
#         print(table[i][j])

# column
# print(len(table))
# row
# print(len(table[0]))
