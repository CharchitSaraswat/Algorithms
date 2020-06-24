# REFER CORMEN PAGE 394
lcs = ""
def fetch_lcs_length(x, y):
    c = list()
    b= list()
    for i in range(len(x)):
        ci = list()
        bi = list()
        for j in range(len(y)):
            ci.append(0)
            bi.append("")
        c.append(ci)
        b.append(bi)
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                if i == 0 or j == 0:
                    c[i][j] = 1
                else:
                    c[i][j] = c[i-1][j-1] + 1
                b[i][j] = "m"
            elif c[i-1][j] > c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = "s"
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = "d"
    return c, b

def generate_lcs(b,x,i,j):
    global lcs
    if  i < 0 or j < 0:
        return
    elif b[i][j] == "m":
        lcs += x[i]
        generate_lcs(b, x, i-1, j-1)
    elif b[i][j] == "s":
        generate_lcs(b, x, i-1, j)
    else:
        generate_lcs(b, x, i, j-1)

if __name__ == "__main__":
    # x = "daer"
    # x = "bnck"
    x = "bread"
    y = "read"
    c, b = fetch_lcs_length(x, y)
    generate_lcs(b, x, len(x)-1, len(y)-1)
    print(lcs[::-1])
