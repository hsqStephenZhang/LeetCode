def mergesort(lis):
    if len(lis) <= 1:
        return lis
    mid = len(lis) // 2
    left = mergesort(lis[:mid])
    right = mergesort(lis[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


if __name__ == '__main__':
    a = [1, 7, 6, 4, 1, 4, 3, 2]
    print(mergesort(a))
