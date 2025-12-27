from operator import itemgetter
def get_num_words(text):
    xd = text.split()
    word_count = 0
    for words in xd:
        word_count += 1
    return word_count

def get_num_char(text):
    my_dict ={}
    cuck = text.lower()
    for char in cuck:
        if char not in my_dict:
            my_dict[char] = 1
        elif char in my_dict:
            my_dict[char] += 1
    return my_dict
def get_num_key(item):
    return item["num"]
def sorted_list(num_char):
    dict_list = []
    for letter in num_char:
        if letter.isalpha():
            new_dict= {}
            new_dict['char'] = letter
            new_dict['num'] = num_char[letter]
            dict_list.append(new_dict)
    dict_list.sort(reverse=True, key= get_num_key)
    return dict_list
            
