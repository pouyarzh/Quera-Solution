def fruits(fruit_list):
    accept_dic_list = []
    accept_dic = {}
    for item in fruit_list:
        if item['shape'] == 'sphere' and 300 <= int(item['mass']) <=600 and 100 <= int(item['volume']) <= 500:
            accept_dic_list.append(item['name'])
    for item in accept_dic_list:
        accept_dic.update({str(item): accept_dic_list.count(str(item))})
    print(accept_dic)
    return accept_dic



if __name__ == '__main__':
    fruits((
        {'name': 'apple', 'shape': 'sphere', 'mass': 350, 'volume': 120},
        {'name': 'mango', 'shape': 'square', 'mass': 150, 'volume': 120},
        {'name': 'lemon', 'shape': 'sphere', 'mass': 300, 'volume': 100},
        {'name': 'apple', 'shape': 'sphere', 'mass': 500, 'volume': 250}))