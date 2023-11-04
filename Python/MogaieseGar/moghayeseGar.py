def compare(string1, string2):
    string1 = stringTrim(string1)
    string2 = stringTrim(string2)
    while(len(str(string1)) != 0 and len(str(string2)) != 0):
        alphabet1 = string1[0]
        alphabet2 = string2[0]
        if(ord(alphabet1) < ord(alphabet2)):
            string1 = string1[1:]
        if(ord(alphabet2) < ord(alphabet1)):
            string2 = string2[1:]
        elif(ord(alphabet1) == ord(alphabet2)):
            string1 = string1[1:]
            string2 = string2[1:]
        if(len(str(string1)) != 0 and len(str(string2)) != 0):
            string1 = string1[::-1]
            string2 = string2[::-1]


    if(len(string1) == 0 and len(string2) == 0):
        print('Both strings are empty!')
        return 'Both strings are empty!'
    if(len(string1) == 0):
        print(string2)
        return string2
    if(len(string2) == 0):
        print(string1)
        return string1


def stringTrim(input):
    input = str(input).strip().lower()
    return input

if __name__ == '__main__':
    compare('  ali  ',' salib ')