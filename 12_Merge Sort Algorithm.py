'''
Merge Sort
-------------------------------------------------------------
'''


def merge_sort(a_list):
    print("Dividing ", a_list)

    if len(a_list) > 1:
        mid_point = len(a_list) // 2
        left_half = a_list[:mid_point]
        right_half = a_list[mid_point:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                a_list[k] = left_half[i]
                i += 1
            else:
                a_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            a_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            a_list[k] = right_half[j]
            j += 1
            k += 1

    print("Merging ", a_list)


if __name__ == '__main__':
    list_length=int(input("Enter length of list for seraching: "))
    a_list=[]
    for i in range (list_length):
        a_list.append(int(input(f"number{i+1}:")))
    print(a_list)
   # a_list = [45, 7, 85, 24, 60, 25, 38, 63, 1]
    merge_sort(a_list)
    print(a_list)