def pivot_place(list1, first, last):

    pivot = list1[first]

    left = first + 1

    right = last

    while True:

        while left <= right and list1[left] <= pivot:
            left = left + 1

        while left <= right and list1[right] >= pivot:
            right = right - 1

        if right < left:
            break

        else:
            list1[left], list1[right] = list1[right], list1[left]

    list1[first], list1[right] = list1[right], list1[first]

    return right


def quick_sort(list1, first, last):

    if first < last:
        
        p = pivot_place(list1, first, last)

        quick_sort(list1, first, p - 1)

        quick_sort(list1, p + 1, last)


list1 = [22, 12, 34, 133, 12]

quick_sort(list1, 0, len(list1) - 1)
print(list1)
