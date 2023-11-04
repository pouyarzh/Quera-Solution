def separator(ls):
    oddlist = []
    evenlist = []
    for item in ls:
        if item % 2 ==0:
            evenlist.append(item)
        else:
            oddlist.append(item)
    return (evenlist,oddlist)



if __name__ == '__main__':
    print(separator([1, 11, 5, 7, 3]))


