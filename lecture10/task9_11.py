#!usr/bin/python3
#Task 9-11

#import

def make_word_list_from_file(file_name):
    """
    Task9
    """
    f = open(file_name)
    word_list = []
    start = False
    start_index =  None
    text = f.read()
    for index in range(len(text)):
        if text[index].isalpha() and start == False:
            start = True
            start_index = index
        elif not text[index].isalpha() and start == True:
            start = False
            word_list.append(text[start_index:index])
    f.close()
    return word_list


def bisection_search(look_for, look_in):
    """
    Task10
    """
    if len(look_in) == 0:
        return False
    N = len(look_in)//2
    if look_for == look_in[N]:
        return True
    if N == 0:
        return False
    if look_for < look_in[N]:
        return bisection_search(look_for, look_in[:N])
    else:
        return bisection_search(look_for, look_in[N:])

def find_rev_pairs(sequence):
    """
    Task11
    """
    rev_pairs = []
    for elem in sequence:
        rev_elem = elem[-1::-1]
        if bisection_search(rev_elem, sequence):
            if not bisection_search((rev_elem, elem), rev_pairs):
                rev_pairs.append((elem, rev_elem))
    return rev_pairs


A = make_word_list_from_file("word.txt")
A = sorted(A)
print(find_rev_pairs(A))
