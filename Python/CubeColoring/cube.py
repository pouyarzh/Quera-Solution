def coloring(ls):
    ls = list(ls)
    counter = 0

    for k in ls:
        counter2 = 0
        if counter == 0 or counter == (len(ls) - 1):
            for k2 in k:
                for k3 in range(len(k2)):
                    k2[k3] = 1

        else:
            for k2 in k:
                for k3 in range(len(k2)):
                    if counter2 == 0 or counter2 == (len(k) - 1):
                        k2[k3] = 1
                    else:
                        if k3 == 0 or k3 == (len(k2) - 1):
                            k2[k3] = 1
                        else:
                            k2[k3] = 0
                counter2 += 1

        counter += 1

    return (ls)


def generate_matrix(n, m, k):
    ls_user = [[[5 for i in range(k)] for j in range(m)] for it in range(n)]
    return ls_user

if __name__ == "__main__":
    ls = generate_matrix(3, 3, 3)
    coloring(ls)