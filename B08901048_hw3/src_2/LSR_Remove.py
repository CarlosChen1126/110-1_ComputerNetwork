import sys


def min_s(check, D, num):
    minn = 100000000
    for i in range(1, num+1):
        if (D[i] < minn and check[i-1] == 0):
            minn = D[i]
            ans = i
    return ans


def LSR_R(s, table, num, remove_node):
    start = s
    P = []
    D = []
    check = []
    for i in range(0, num+1):
        P.append(-1)
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
    for i in range(1, num+1):
        if D[i] == 10000000:
            D[i] = -1
    return D, P


while True:
    c = input()
    if(c[0:2] == "lf"):
        inputname = c[3:]

        f = open(inputname, "r")
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
    elif (c[0:2] == "rm"):
        remove_node = c[4:]
        remove_node = int(remove_node)
        for i in range(0, num+1):
            table[remove_node][i] = -1
            table[i][remove_node] = -1
        for i in range(1, num+1):
            D, P = LSR_R(i, table, num, remove_node)
            DD.append(D)
            PP.append(P)

    elif(c[0:2] == "of"):
        outputname = inputname.replace(".txt", "_out2.txt")

        f = open(outputname, 'w')
        for i in range(0, num):
            if i+1 != remove_node:
                f.write("Routing table of router " + str(i+1)+"\n")
                for j in range(1, num+1):
                    f.write(str(DD[i][j])+" "+str(PP[i][j])+"\n")
        f.close()


# # remove router2
# remove_node = int(sys.argv[3])
# for i in range(0, num+1):
#     table[remove_node][i] = -1
#     table[i][remove_node] = -1

# DD = []
# PP = []
# for i in range(1, num+1):
#     D, P = LSR_R(i, table, num, remove_node)
#     DD.append(D)
#     PP.append(P)
# print(DD)
# print(PP)
# name = sys.argv[1]
# name = name.replace(".txt", "_out2.txt")
# f = open(name, 'w')
# for i in range(0, num):
#     if i+1 != remove_node:
#         f.write("Routing table of router " + str(i+1)+"\n")
#         for j in range(1, num+1):
#             f.write(str(DD[i][j])+" "+str(PP[i][j])+"\n")
# f.close()
