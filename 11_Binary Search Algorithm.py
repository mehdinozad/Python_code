'''
Binary Search
-------------------------------------------------------------
'''

def binary_search(a_list, an_item):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid_point = (first + last) // 2
        if a_list[mid_point] == an_item:
            return True
        else:
            if an_item < a_list[mid_point]:
                last = mid_point - 1
            else:
                first = mid_point + 1
    return False


def binary_search_rec(a_list, first, last, an_item):
    if first<=last:
        mid = (last + first) // 2

        if a_list[mid] == an_item:
            return True
        elif an_item<a_list[mid]:
            return binary_search_rec(a_list, first, mid - 1, an_item)
        else:
            return binary_search_rec(a_list, mid + 1, last, an_item)

    else:
        return False

if __name__ == '__main__':
    list_length=int(input("Enter length of sorted list for serach: "))
    a_list=[]
    for i in range (list_length):
        a_list.append(int(input(f"number{i+1}:")))
    print(a_list)
    x=int(input("Enter key for search:"))
    #a_list = [1, 4, 7, 10, 14, 19, 102, 2575, 10000]
    #x=4
    print('Binary Search:', binary_search(a_list, x))
    print('Binary Search Recursive:',binary_search_rec(a_list, 0, len(a_list) - 1,x ))
