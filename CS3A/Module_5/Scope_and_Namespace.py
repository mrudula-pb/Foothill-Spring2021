def my_func():
    global a  # here we are telling that a = 7 should be in global scope
    print(f'value of a in my_func: {a}')  # UnboundLocalError: local variable 'a' referenced before assignment
    a = 12  # a= a+1 will work too
    print(f'value of a in my_func: {a}')


a = 7
print(f'value of a at module level: {a}')
my_func()
print(f'value of a at module level after my_func: {a}')

# intention is to alter a at the global namespace
