from re import M


def solve(X: int) -> [int, int]:
    lst = list()
    m = X
    for i in range(1,X):
        TotalArea = i*i*i
        if TotalArea < X:
            lst.append(i)
            cube += TotalArea
    max = sum(lst)
    print (max + cube)

solve()
