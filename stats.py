def word_counter(text):
    list_of_text = text.split()
    counter = 0
    for txt in list_of_text:
        counter += 1
    return counter

def char_count(text):
    texts = text.lower()
    char_list = []
    num_dic = {}
    for c in texts:
       check = c in char_list
       if check == False:
           char_list.append(c)
    for ch in char_list:
        counter = 0
        for c in texts:
            if c == ch:
                counter += 1
        num_dic[ch] = counter
    
    return num_dic

def sort_on(dict):
    return dict["num"]

def get_sorted(dect):
    new_list = []
    ch = "char"
    num = "num"
    for key, value in dect.items():
        new_dic = {}
        new_dic[ch]= key
        new_dic[num]= value
        new_list.append(new_dic)
    new_list.sort(reverse=True, key=sort_on)
    return new_list

