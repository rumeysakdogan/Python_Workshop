if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    # s = raw_input().split()
    # s = [int(i) for i in s]
    # map(function, sequence) --> [fun(seq[0]),fun(seq[1]), ...]


    list_num = list(arr)
    list2 = []
    max = list_num[0]
    for i in list_num:
        if i >= max:
            max = i

    for i in list_num:
        if i == max:
            list2.append(i)

    for i in list2:
        list_num.remove(i)

    max = list_num[0]
    for i in list_num:
        if i >= max:
            max = i

    print(max)