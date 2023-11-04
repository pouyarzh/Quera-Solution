def game(number):
    count = 0
    tepNumber = number
    while (tepNumber > 0):
        count = count + 1
        tepNumber = tepNumber // 10

    if count > 2 :
        raise Exception('number out of range')

    my_list = [int(x) for x in str(number)]
    max_digit = max(my_list)
    min_digit = min(my_list)
    return max_digit - min_digit



if __name__ == "__main__":
    game(15)