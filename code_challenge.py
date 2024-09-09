#Takes two numbers as input and returns their sum.
def add_numbers(num1, num2):
    print("adding numbers")
    return num1 + num2

print(add_numbers(7, 9))

#Checks if a given number is even.
def is_even(number):
    print("checking if number is even")
    return number % 2 == 0

print(is_even(5))

#Reverses the input string.
def reverse_string(text):
    print("reversing string")
    return text[::-1]

print(reverse_string("Denis"))


#Counts the number of vowels in the input string.
def count_vowels(text):
    print("counting vowels")
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(count_vowels("Denis"))


#Calculates the factorial of a given none negative number.
def calculate_factorial(n):
        
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0 or n == 1:
        return 1
    return n * calculate_factorial(n - 1)
print("calculating factorial")
print(calculate_factorial(5))

#Decorator function
def decorator_func(func):
    # A decorator that prints a message before calling the decorated function.
    def wrapper(*args, **kwargs):
        print("Decorator Applied")
        return func(*args, **kwargs)
    return wrapper

#Apply decorator
@decorator_func

def apply_decorator(func):
    # Applies the decorator 'decorator_func' to the input function.
    return decorator_func(func)


print(apply_decorator(calculate_factorial))


#Sorts a list of tuples containing (name, age) by age in ascending order.
def sort_by_age(people):
    print("sorting by age")
    return sorted(people, key=lambda person: person[1])

print(sort_by_age([('Tom', 45), ('Jane', 35), ('Bob', 67)]))

#Merges two dictionaries. If they have common keys, sums their values.
def merge_dicts(dict1, dict2):
    print("merging dictionaries")
    merged = dict1.copy()  # Start with dict1's keys and values
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum values for common keys
        else:
            merged[key] = value  # Add new key
    return merged

print(merge_dicts({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))


#A class representing a car.
class Car:

    #Initialize the car with make, model, and year.   
    
    def __init__(self, make, model, year):
      
        self.make = make
        self.model = model
        self.year = year
    
    #Display information about the car.
    def display_info(self):
        
        print(f"Car Information: {self.year} {self.make} {self.model}")

my_car = Car("Subaru", "Impreza", 2006)
my_car.display_info()
