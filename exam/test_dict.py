#1
def sort_dictionary_by_values(input_dict):
    input_dict=input_dict.items()
    input_dict.sort(key=lambda x:x[1])
    return dict(input_dict)
#2
def add_key_to_dictionary(input_dict,key,value):
    input_dict[key] = value
    return input_dict
#3
def concatenate_dictionaries(dict1,dict2,dict3):
    return dict(dict1.items()+dict2.items()+dict3.items())
#4
def check_key_exists_or_not(input_dict,k):
    check=False
    for key in input_dict.keys():
        if(key==k):
            check=True
    return check
#5 #9
def iterate_dictionary():
    input_dict={1:"a",2:"b",3:"c"}
    for key, value in input_dict.iteritems():
        print key,value
#6
def generate_dictionary(n):
    dict={}
    for i in range(1,n+1):
        dict[i]=i*i
    return dict
#8
def merge_dictionary(dict1,dict2):
     dict2.update(dict1)
     return dict2
#10
def sum_all_items_in_dictionary(input_dict):
    return sum(input_dict.values())
#11
def multiply_all_the_items_in_dictionary(input_dict):
    total=1
    for key,value in input_dict.items():
        total*=value;
    return total
#12
def remove_key_from_dictionary(input_dict,key):
    try:
      del input_dict[key]
      return input_dict
    except KeyError:
        return "key not found"
#13
def map_two_lists_into_dictionary(list1,list2):
    return dict(zip(list1,list2))
#14
def sort_dictionary_by_key(input_dict):
    input_dict=input_dict.items()
    input_dict.sort(key=lambda x:x[0])
    return dict(input_dict)
#15
def max_and_min_in_dictionary(input_dict):
    return max(input_dict,key=lambda key:input_dict[key]), min(input_dict,key=lambda k:input_dict[k])
#16
def dictionary_from_object_fields():
    class Student(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
    s=Student("mani",21)
    return s.__dict__
#17
def remove_duplicates_from_dictionary(input_dict):
    return dict(set(input_dict.items()))
#18
def dictionary_is_empty_or_not(input_dict):
    check = True if (len(input_dict) == 0) else False
    return check
#testing
def test_sort_dictionary_by_values():
    assert {"varun":21, "ajay":22} == sort_dictionary_by_values({"ajay":22,"varun":21})

def test_add_key_to_dictionary():
    assert {1:"varun",2:"arun",3:"karun"} ==add_key_to_dictionary({1:"varun",2:"arun"},3,"karun")

def test_concatenate_dictionaries():
    assert {1:"varun",2:"arun",3:"karun"} == concatenate_dictionaries({1:"varun"},{2:"arun"},{3:"karun"})

def test_check_key_exist_or_not():
    assert True == check_key_exists_or_not({1:"varun",2:"arun",3:"karun"},2)

def test_generate_dictionary():
    assert {1:1,2:4,3:9} == generate_dictionary(3)
    #7
    assert {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225} == generate_dictionary(15)

def test_merge_dictionary():
    assert {1:"varun", 2:"arun",3:"karun"}==merge_dictionary({1:"varun",2:"arun"},{2:"charan",3:"karun"})

def test_sum_of_all_elements_in_dictionary():
    assert 30 == sum_all_items_in_dictionary({"varun":15,'arun':10,"karun":5})

def test_multiply_all_the_items_in_dictionary():
    assert 750 == multiply_all_the_items_in_dictionary({"varun": 15, 'arun': 10, "karun": 5})

def test_remove_key_from_dictionary():
    assert {1:"Mani",2:"Teja"} == remove_key_from_dictionary({1:"Mani",2:"Teja",3:"srikanth"},3)
    assert {2: "Teja", 3: "srikanth"} == remove_key_from_dictionary({1: "Mani", 2: "Teja", 3: "srikanth"}, 1)
    assert "key not found" == remove_key_from_dictionary({1: "Mani", 2: "Teja", 3: "srikanth"}, 4)

def test_map_two_lists_into_dictionary():
    assert {1: 'mani', 2: 'teja', 3: 'srikanth'} == map_two_lists_into_dictionary([1,2,3],["mani", "teja","srikanth"])

def test_sort_dictionary_by_key():
    assert {21:"varun", 22:"ajay"} == sort_dictionary_by_key({22:"ajay",21:"varun"})

def test_min_and_max_in_dictionary():
    assert ("varun","ajay") == max_and_min_in_dictionary({"ajay": 19, "varun": 21})

def test_dictionary_from_object_fields():
    assert {"name":"mani","age":21} == dictionary_from_object_fields()

def test_remove_duplicates_in_dictionary():
    assert {"ajay":22,"varun":23} == remove_duplicates_from_dictionary({"ajay":22,"varun":21,"varun":23})

def test_dictionary_is_empty_or_not():
    assert True ==dictionary_is_empty_or_not({})
