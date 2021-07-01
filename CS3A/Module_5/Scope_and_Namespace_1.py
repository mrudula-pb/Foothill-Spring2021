def my_func():
    def my_nested_func():
        global a
        a = 13 # here a is global and is assigned value 13
        print(f'value of a in my_nested-func: {a}') # a = 13
    # global a # here we are telling that a = 7 should be in global scope
    a = 12 # here a is local and a brand new a is being created
    print(f'value of a in my_func: {a}') # a = 12
    my_nested_func()
    print(f'value of a in my_func after call to my_nested_func: {a}') # a = 12


a = 7
print(f'value of a at module level: {a}')
my_func()
print(f'value of a at module level after my_func: {a}')