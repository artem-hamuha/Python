def max_num_in_list(listt):
    maxx = listt[ 0]
    for a in listt:
        if a > maxx:
            maxx = a
    return maxx


print(max_num_in_list([1, 2, 4, 0]))


def smallest_num_in_list(listt):
    minn = listt[0]
    for a in listt:
        if a < minn:
            minn = a
    return minn


print(smallest_num_in_list([1, 2, -8, 0]))
