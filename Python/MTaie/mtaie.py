
def calculator(n, m, li):
    number_list = []
    start_index = 0
    end_index = m-1
    while(start_index < n):
        special_number = sum(li[start_index:end_index +1])
        print(special_number)
        number_list.append(special_number)
        start_index = start_index + m
        print(start_index)
        end_index = end_index + m
        print(end_index)

    print(number_list)
    return_value = 0
    plus = True
    for item in number_list:
        if(plus):
            return_value +=item
            plus = False
        else:
            return_value -= item
            plus = True

    return return_value

if __name__ == '__main__':
    print(calculator(11,5,[1, 2, 3, 4, 5, 6, 7, 8,9,10,11]))
    # print(test([1, 2, 3, 4, 5, 6, 7, 8]))