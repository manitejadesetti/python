from random import shuffle,choice
from itertools import permutations
#1
def sum_off_all_the_items_in_list(input_list):
    list_sum=sum(input_list)
    return list_sum
#2
def multiply_all_the_items_in_list(input_list):
    total=1
    for i in input_list:
        total*=i;
    return total
#3
def max_and_min_in_list(input_list):
    return max(input_list),min(input_list)
#4
def palindrome_or_not(word):
    check = True if word[::-1]==word else False
    return check
#5
def check_length_of_word_and_first_and_last_character(input_list):
    count=0
    for item in input_list:
        count+=1 if len(item)>2 and item[0]==item[len(item)-1] else 0
    return count
#6
def sort_in_incresing_order_by_last_element_in_tuple_from_a_list(input_list):
    def lastElem(item):
        return item[len(item)-1]
    input_list.sort(key=lastElem)
    return input_list
#7
def remove_duplicates_from_list(input_list):
    return list(set(input_list))
#8
def list_is_empty_or_not(input_list):
    check= True if(len(input_list)==0) else False
    return check
#9
def copy_of_list(input_list):
    new_list=list(input_list)
    return new_list
#10
def words_longer_than_n(str,n):
    li=str.split(" ")
    return [item for item in li if(len(item)>n)]
#11
def common_member(input_list1,input_list2):
    check=False
    for item1 in input_list1:
        for item2 in input_list2:
            check = True if(item2==item1) else False
            return check
#12
def specified_list(input_list):
    indices = 0, 2, 4, 5
    input_list = [i for j, i in enumerate(input_list) if j not in indices]
    return input_list
    return input_list
#13
def remove_non_alphabets(str):
    for i in str:
        if(not((ord(i)>=65 and ord(i)<=90) or (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57))):
            str=str.split(i)
            str="".join(str)
    return str
#14
def remove_even(input_list):
    return [item for item in input_list if(item%2!=0)]
#15
def shuffle():
    li=[1,2,3,4,5]
    li=shuffle(li)
#16
def first_and_last_five_elements():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l[:5]+l[-5:]
#17
def except_first_five_elements():
    l=[]
    for i in range(1,31):
        l.append(i**2)
    return l[5:]
#18
def permutations_of_list(input_list):
    return list(permutations(input_list))
#19
def difference_between_two_lists(input_list1,input_list2):
    return list(set(input_list1)-set(input_list2))
#20
def index_of_list(input_list):
    return [input_list.index(i) for i in input_list]
#21
def characters_into_string(input_list):
    return "".join(input_list)
#22
def append_list(input_list1,input_list2):
    return input_list2+input_list1
#23
def remove_adjacent_duplicates(input_list):
    index=1
    n=len(input_list[:])
    while(index<n):
        if input_list[index]== input_list[index-1]:
            del(input_list[index-1])
            n-=1
        else:
            index+=1
    return input_list
#24
def random_item_from_list(input_list):
    print choice(input_list)
#25
def circularly_identical(input_list1,input_list2):
    check = True if "".join(map(str,input_list1)) in "".join(map(str,input_list2*2)) else False
    return check

#testing
def test_sum_of_all_items_in_list():
    assert 20 ==sum_off_all_the_items_in_list([6,6,8 ])
    assert 28 == sum_off_all_the_items_in_list([6, 8, 7,7])
    assert 33 == sum_off_all_the_items_in_list([10, 11, 3,9])
    assert 64 == sum_off_all_the_items_in_list([21, 10, 5,26,2])

def test_multiply_all_items_in_list():
    assert 288 ==multiply_all_the_items_in_list([6,6,8 ])
    assert 2352 == multiply_all_the_items_in_list([6, 8, 7,7])
    assert 2970 == multiply_all_the_items_in_list([10, 11, 3,9])
    assert 54600 == multiply_all_the_items_in_list([21, 10, 5,26,2])

def test_max_and_min_in_list():
    assert (4,1)==max_and_min_in_list([1,2,3,4])
    assert (52,16) == max_and_min_in_list([18,16,22,33,52])

def test_palindrome_or_not():
    assert True == palindrome_or_not("madam")
    assert False == palindrome_or_not("Hello")

def test_check_length_of_word_and_first_and_last_character():
    assert 2== check_length_of_word_and_first_and_last_character(["abc","1221","aba","lion"])

def test_sort_in_incresing_order_by_last_element_in_tuple_from_a_list():
    assert [(4, 1), (2, 2), (1, 3), (3, 4)] == sort_in_incresing_order_by_last_element_in_tuple_from_a_list([(2, 2), (3, 4), (4, 1), (1, 3)])
    assert [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)] == sort_in_incresing_order_by_last_element_in_tuple_from_a_list([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])

def test_remove_duplicates_from_list():
    assert [1,2,3,4,5] == remove_duplicates_from_list([1,2,1,2,3,3,4,5])

def test_list_is_empty_or_not():
    assert True == list_is_empty_or_not([])
    assert False == list_is_empty_or_not([1,2])

def test_copy_of_list():
    assert [1,2,3,4,5] == copy_of_list([1,2,3,4,5])
    assert ["apple","mango","orange"] == copy_of_list(["apple","mango","orange"])

def test_words_longer_than_n():
    assert ['quick', 'brown', 'jumps', 'over', 'lazy'] ==words_longer_than_n("The quick brown fox jumps over the lazy dog",3)

def test_common_member():
    assert True == common_member([1,2,3,4,5],[1,2,3,4,5])
    assert False == common_member([1, 2, 3, 4, 5], [6,7,8,9,10])

def test_specified_list():
    assert [1,3] == specified_list([0,1,2,3,4,5])

def test_remove_non_alphabets():
    assert "ab2344" == remove_non_alphabets("ab$23#44")

def test_even_remove():
    assert [1,3,5] == remove_even([1,2,3,4,5])

def test_first_and_last_five_elements():
    assert [1, 4, 9, 16, 25, 676, 729, 784, 841, 900 ] == first_and_last_five_elements()

def test_except_first_five_elements():
    assert [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]== except_first_five_elements()

def test_permutations():
    assert [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)] == permutations_of_list([1,2,3])

def test_difference_between_two_lists():
    assert [3,4,5] == difference_between_two_lists([1,2,3,4,5], [1,2])

def test_index_of_list():
    assert [0,1,2,3,4] == index_of_list([12,3,4,5,6])
def test_remove_adjacent_duplicates():
    assert [1,2,3,2,4] == remove_adjacent_duplicates([1,1,2,2,3,2,4,4])

def test_characters_into_string():
    assert "apple" == characters_into_string(["a","p","p","l","e"])

def test_append_list():
    assert [1,2,3,4] == append_list([3,4],[1,2])