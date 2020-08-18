my_stack = ['google.co.za', 'money.co.za', 'cars.com', 'fb.com']
my_history = []
def add_to_stack(my_history):
    """
    >>> add_to_stack(['google.co.za', 'money.co.za', 'cars.com', 'fb.com'])
    ['google.co.za', 'money.co.za', 'cars.com', 'fb.com']
    """
    for h in my_stack:
        my_history.append(h)
    return my_history
def remove_from_stack(my_history):
    """
    >>> remove_from_stack(['google.co.za', 'money.co.za', 'cars.com', 'fb.com'])
    ['google.co.za', 'money.co.za', 'cars.com']
    """
    my_history.pop()  # We remove the last element in our stack by using the pop function.
    return my_history()

my_stack.pop()
print(my_stack) #removing a string in the list

my_stack.append('Isntagram.com')  # adding the string in the list
print("The Content of my_stack list is:")
print(my_stack)