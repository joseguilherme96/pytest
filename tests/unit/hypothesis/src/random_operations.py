def find_largest_smallest_item(input_array:list) -> tuple:

    if len(input_array) == 0:

        raise ValueError
    

    largest = input_array[0]
    smallest = input_array[0]


    for i in range(0, len(input_array)):

        if input_array[i] > largest:

            largest = input_array[i]

        if input_array[i] < smallest:

            smallest = input_array[i]

    return largest, smallest

def sort_array(input_array: list, sort_key: str, reverse : bool = True) -> list:

    if len(input_array) == 0:

        raise ValueError
    
    if sort_key not in input_array[0]:

        raise KeyError
    
    if not isinstance(input_array[0][sort_key],int):

        raise TypeError
    
    sorted_data = sorted(input_array, key=lambda x: x[sort_key],reverse=reverse)

    return sorted_data

def reverse_string(input_string):

    return input_string[::-1]

def complex_string_operation(input_string: str) -> str:

    input_string = input_string.strip().replace(" ","")

    input_string = input_string.upper()

    vowels = ["A","E","I","O","U"]

    for x in input_string:

        if x in vowels:

            input_string = input_string.replace(x,"")

    return input_string