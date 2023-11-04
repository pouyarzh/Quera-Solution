def words_check(text):
    words_list = separator(text)
    dict = {}
    accepted_words_list = []
    for item in words_list:
        print(item)
        result = checkGoodWord(item)
        if(result != 0):
            accepted_words_list.append(str(result))
    for item in accepted_words_list:
        dict.update({str(item): accepted_words_list.count(str(item))})

    return dict


def separator(text):
    return text.split()

def checkGoodWord(word):

    k = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

    getVals = list(filter(lambda x: x in k, word))
    result_word = "".join(getVals)
    result_word = result_word.lower().title()
    if ((len(word) /2) < len(result_word)):
        return result_word
    return 0



if __name__ == "__main__":
    print(words_check('"hEllO My FriEnDs!!! thIS i$s A tE%sT For your #p#r#o#b#l#e#m a'))
