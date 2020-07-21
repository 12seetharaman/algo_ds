"""
Given an array of size n and multiple values around which we need to left rotate the array.
How to quickly print multiple left rotations?

Input : arr[] = {1, 3, 5, 7, 9}
        k1 = 1
        k2 = 3
        k3 = 4
        k4 = 6
Output : 3 5 7 9 1
         7 9 1 3 5
         9 1 3 5 7
         3 5 7 9 1

"""

def rotate_array(arr, count):
    pointer = count % len(arr)
    result = []
    for i in range(len(arr)):
        result.append(arr[(pointer + i) % len(arr)])
    return result

if __name__ == "__main__":
    num_array = [1, 3, 5, 7, 9]
    rotation_num = int(input())
    output = rotate_array(num_array, rotation_num)
    print(output)