import copy

def recursive(array, n):
    if len(array) == n:
        operator_list.append(copy.deepcopy(array))
        return
    array.append(' ')
    recursive(array, n)
    array.pop()

    array.append('+')
    recursive(array, n)
    array.pop()

    array.append('-')
    recursive(array, n)
    array.pop()

test = int(input())
for _ in range(test):
    operator_list = []
    n = int(input())
    recursive([],n-1)

    num = [i+1 for i in range(n)]

    for operator in operator_list:
        string = ""
        for i in range(n-1):
            string += str(num[i]) + operator[i]
        string += str(num[-1])

        if eval(string.replace(" ", "")) == 0:
            print(string)
    print()


