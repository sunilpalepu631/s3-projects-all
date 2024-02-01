def sum_values(*args):
    return sum(args)

# result = sum_values(1,3,4,6,2,3)
# print(result)  # Output: 15

# *args , args should be a list or tuple

# def print_person_info(name, age, city):
#     print(f"Name: {name}, Age: {age}, City: {city}")

# person_info = ("Alice", 30, "Wonderland")
# print_person_info(*person_info)



def calculate_total(*args, initial_value=0):
    
    return initial_value+ sum(args)

result = calculate_total(2,1,34,45,2,1,initial_value=10)
print(result)


def print_info(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name='Alice', age=30, city='Wonderland')


def print_person_info(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

person_data = {'age': 30,'name': 'Alice',  'city': 'Wonderland'} # packed dict

print_person_info(**person_data)       #unpacking dict using **




print_person_info(name='sunil',age=23,city='kandukur')
