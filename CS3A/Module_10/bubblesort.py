

def bubble_sort(ret_list: list): #sort_list
    # ret_list = sort_list # in case you want to copy to new list
    sort_completed = False
    while not sort_completed:
        print(f"---> {ret_list}")
        sort_completed = True
        for i in range(len(ret_list)-1):
            if ret_list[i] > ret_list[i + 1]:
                ret_list[i], ret_list[i + 1]  = ret_list[i + 1], ret_list[i]
                sort_completed = False



bubble_list = ['spot', 'rover', 'fido', 'princess', 'fifi', 'rex', 'astro']
bubble_sort(bubble_list)
print(bubble_list)