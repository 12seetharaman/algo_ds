'''
Move all zeroes to end of array

Input :  arr[] = {1, 2, 0, 4, 3, 0, 5, 0};
Output : arr[] = {1, 2, 4, 3, 5, 0, 0};

Input : arr[]  = {1, 2, 0, 0, 0, 3, 6};
Output : arr[] = {1, 2, 3, 6, 0, 0, 0};
'''

def zero_to_end(arr: list) -> list:
    """Get array and move all zero to end of it.
    Args:
        arr (list): input array
    Returns:
        list: output array
    """

    result_list = []
    zeros_count = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            result_list.append(arr[i])
        else:
            zeros_count += 1
    result_list.extend([0] * zeros_count)

    return result_list

if __name__ == "__main__":
    arr = [1, 2, 0, 4, 3, 0, 5, 0]
    output = zero_to_end(arr)
    print(output)