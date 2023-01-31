def pascal_triangle(n):
    result = []
    for i in range(n):
        if i == 0:
            result.append([1])
        else:
            row = [1]
            for j in range(1, i):
                row.append(result[i-1][j-1] + result[i-1][j])
            row.append(1)
            result.append(row)
    return result

def exposant(n):
    U = [0x2070, 0x00B9, 0x00B2, 0x00B3, 0x2074, 0x2075, 0x2076, 0x2077, 0x2078, 0x2079]
    n = str(n)
    exp_n = ""
    for i in range(len(n)):
        exp_n += chr(U[int(n[i])])
    return exp_n

def identite_remarquable(a : str, b : str, ex : int) -> str: 
    pattern = pascal_triangle(ex+1)
    pattern = pattern[-1]
    resultat = []
    bex = [i for i in range(ex, -1, -1)]
    aex = [i for i in range(ex+1)]
    r = ''
    for op in range(len(pattern)-1, -1, -1):
        resultat.append(f"{pattern[op] if pattern[op] != 1 else ''}{a if aex[op] != 0 else ''}{r if (aex[op] == 1 or aex[op] == 0)  else exposant(aex[op])}{b if bex[op] != 0 else ''}{r if (bex[op] == 1 or bex[op] == 0)  else exposant(bex[op])}")
    resultat = ' + '.join(resultat)
    return f"({a} + {b}){exposant(ex)} = {resultat}"

print(identite_remarquable('a','b', 12))
