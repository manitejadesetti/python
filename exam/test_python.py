from placeholders import *
from collections import OrderedDict


def square_of_each_item_in_list(input_list):
    return [val**2 for val in input_list]

def get_odds_list(count):
    """
     This method returns a list of the first 'count' odd numbers in descending
     order. e.g count = 3 should return [5,3,1]
    """
    a= [i for i in range(0, 2 + (count - 1) * 2) if (i % 2 != 0)]
    return a[::-1]


def get_odd_mountain(count):
    """
    odd mountain is a list of odd numbers going up from 1 and then back to 1.
     e.g. odd_mountain of size 5 is [1,3,5,3,1]
    odd_mountain of size 4 is [1,3,3,1]

    Hint: use the list functions and a builtin function we have already seen.
    """
    a=[i for i in range(0, count + 1) if (i % 2 != 0)]
    a=a+a[::-1] if(count==2) else a+a[-2::-1]
    return a

def get_multiples_desc(number, count):
    """
    return the first count multiples of number in desc order in a list.
    e.g call with input (3,2) returns [6,3]
    call with input(5,3) returns [15,10, 5]

    Hint: one line of code, use a builtin function we have already seen in the lists lesson.
    """
    a=[i*number for i in range(1,count+1)]
    return a[::-1]

def get_sorted_diff_string(first, second):
    """
    returns a string which contains letters in first but not in second.
    e.g.s apple and pig returns ael.
    """
    s=set([i for i in first if(i not in second)])

    return "".join(sorted(''.join(s)))

def get_sorted_without_duplicates(input):
    """
    returns a string in which characters are sorted and duplicates removed
    e.g apple returns aelp, engine returns egin
    """
    return "".join(sorted("".join(set(input))))

def create_palindrome(word):
    a=word+word[::-1] if(word!=None) else None
    return a

# Sort the words that are passed in by word length instead of word content.
# e.g ["apple", "dog", "elephant"] should result in ["elephant", "apple", "dog"]
# hint: use list.sort, don't write your own
def test_pow_of_each_item_in_list():
    assert [1,4,9] == square_of_each_item_in_list([1,2,3])

def sort_by_length(words):
    words.sort(key=len, reverse=True) if(words!= None) else None
    return words

def test_odds_list():
    assert [1] == get_odds_list(1)
    assert [] == get_odds_list(0)
    assert [5,3,1] == get_odds_list(3)
    assert [9,7,5,3,1] == get_odds_list(5)

def test_get_odd_mountain():
    assert [1,1] == get_odd_mountain(2)
    assert [1,3,1] == get_odd_mountain(3)
    assert [1,3,5,7,5,3,1] == get_odd_mountain(7)
    assert [] == get_odd_mountain(0)

def test_get_multiples_desc():
    assert [6,3] == get_multiples_desc(3,2)
    assert [15, 10, 5] == get_multiples_desc(5,3)
    assert [] == get_multiples_desc(6, 0)
    assert [3,2,1] == get_multiples_desc(1, 3)


def test_sorted_diff_string():
    assert "" == get_sorted_diff_string("apple", "apple")
    assert "aelp" == get_sorted_diff_string("apple", "")
    assert "do" == get_sorted_diff_string("dog", "pig")
    assert "in" == get_sorted_diff_string("pineapple", "apple")


def test_sorted_without_duplicates():
    assert "aelp" == get_sorted_without_duplicates("apple")
    assert "eorz" == get_sorted_without_duplicates("zeroo")
    assert "" == get_sorted_without_duplicates("")
    assert "abcd" == get_sorted_without_duplicates("abcdabcd")

def test_create_palindrome():
        assert "battab" == create_palindrome("bat")
        assert "abba" == create_palindrome("ab")
        assert "" == create_palindrome("")
        assert None == create_palindrome(None)

def test_sort_by_length():
    assert ["apple", "bear", "dog"] == sort_by_length(["dog", "apple", "bear"])
    assert ["apple", "bear", "dog"] == sort_by_length(["apple", "dog",  "bear"])
    assert ["apple", "dog", "cat"] == sort_by_length(["dog", "apple", "cat"])
    assert ["elephant", "apple"] == sort_by_length(["apple", "elephant"])
    assert ["three", "four", "one", "two"] == sort_by_length(["one", "two", "three", "four"])
    assert [] == sort_by_length([])
    assert None == sort_by_length(None)