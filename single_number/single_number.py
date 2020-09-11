'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # set empty arr of dups
    dups = []
    # loop through the array
    for i in range(len(arr) - 1):
    # find all repeated elements and set to a new arr
        for j in range(len(arr) - 1):
            if arr[i] == arr[j] and arr[i] in dups:
                dups.append(arr[i])
    # return single element
        return arr



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")