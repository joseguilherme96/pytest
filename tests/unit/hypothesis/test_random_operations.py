from src.random_operations import find_largest_smallest_item,sort_array,reverse_string,complex_string_operation
from hypothesis import given, strategies as st
from hypothesis import assume as hypothesis_assume
from pytest import raises

def test_find_largest_smallest_item():

    assert find_largest_smallest_item([4,2,1,6]) == (6,1)

@given(st.lists(st.integers(),min_size=1, max_size=25))
def test_find_largest_smallest_item_hypothesis(input_list):

    assert find_largest_smallest_item(input_list) == (max(input_list),min(input_list))

def test_sort_array():

    data = [
        {"name": "José Guilherme", "age":22},
        {"name": "Gilberto", "age": 21},
        {"name": "Willian", "age": 24},
        {"name": "Layra", "age": 23}
    ]

    assert sort_array(data,"age") == [
        {"name": "Willian", "age": 24},
        {"name": "Layra", "age": 23},
        {"name": "José Guilherme", "age":22},
        {"name": "Gilberto", "age": 21}
        
    ]

@given( st.lists( st.fixed_dictionaries({"name":st.text(),"age":st.integers()})))
def test_sort_array_hypothesis(input_list):

    if len(input_list) == 0:

        with raises(ValueError):

            sort_array(input_list, "age")
            print("lista vazia")

    hypothesis_assume(len(input_list) > 0)
    assert sort_array(input_list,"age") == sorted(input_list,key=lambda x: x["age"], reverse=True)

@given(st.lists( st.fixed_dictionaries({"name":st.text(),"age":st.integers()})),st.booleans())
def test_sort_array_reverse_hypothesis(input_list,reverse):

    if len(input_list) == 0:

        with raises(ValueError):

            sort_array(input_list, "age", reverse)

    hypothesis_assume(len(input_list) > 0)
    assert sort_array(input_list,"age",reverse) == sorted(input_list,key=lambda x: x["age"], reverse=reverse)

def test_reverse_string():

    assert reverse_string("hello") == "olleh"

@given(st.text())
def test_reverse_string_hypothesis(input_string):

    assert reverse_string(input_string) == input_string[::-1]

def test_complex_string_operation():

    assert complex_string_operation(" Hello World ") == "HLLWRLD"

@given(st.text())
def test_complex_string_operation_with_hypothesis(input_string):

    assert complex_string_operation(input_string) == input_string.strip().replace(" ","").upper().replace("A","").replace("E","").replace("I","").replace("O","").replace("U","")

    