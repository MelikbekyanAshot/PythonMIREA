def f21(x):
    if x[3] == "cson":
        if x[2] == 1999:
            if x[1] == "gosu":
                return 0
            else:
                return 1
        elif x[2] == 2009:
            if x[1] == "gosu":
                return 2
            else:
                return 3
        elif x[2] == 1966:
            if x[0] == "hel":
                return 4
            elif x[0]:
                return 5
            else:
                return 6
    else:
        if x[1] == "gosu":
            return 7
        else:
            if x[0] == "hel":
                return 8
            elif x[0] == "sql":
                return 9
            else:
                return 10

print(f21(['xs', 'coq', 1999, 'cson']))
print(f21(['xs', 'gosu', 1999, 'meson']))