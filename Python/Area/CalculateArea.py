def get_func(ls):
    return_list = []

    for item in ls:
        if(item == 'square'):
            return_list.append(square_area)
        if(item == 'circle'):
            return_list.append(circle_area)
        if (item == 'rectangle'):
            return_list.append(rectangle_area)
        if (item == 'triangle'):
            return_list.append(triangle_area)
    return return_list


def square_area(edge):
    return edge * edge

def circle_area(redius):
    return float(redius * redius * 3.141592653589793)

def rectangle_area(lenght,width):
    return lenght * width

def triangle_area(height,frame):
    return (height * frame) / 2

def test():
    return square_area

if __name__ == "__main__":
    ls = get_func(['circle', 'circle', 'circle'])
    print(ls)
    print(ls[0](12,))  # 1
    print(ls[1](4,))  # 12.566370614359172
    print(ls[2](5.5,))  # 8
    # print(ls[3](4, 5))  # 10.0