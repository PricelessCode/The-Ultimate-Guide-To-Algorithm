def build_max_heap(arr, n):
    last_leaf = (n - 1 - 1) // 2 # n - 1 for the last index of the array and others are the formula for getting the parent's index
    for i in range(last_leaf, -1, -1):
        max_heapify(arr, n, i)

# Note: Heapify is used when you have built a heap already and you need to keep the property by changing the subtree. (Just Heapifying a random array once(at the root) does not give you a heap)
# Sift Down method
def max_heapify(arr, n, i):
    largest = i
    left_index = 2 * i + 1
    right_index = 2 * i + 2

    if left_index < n and arr[left_index] > arr[i]:
        largest = left_index

    if right_index < n and arr[right_index] > arr[largest]:
        largest = right_index

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# Sift Up method --> Only for inserting node
def max_heapify_up(arr, n, i):
    parent_index = (i - 1) // 2
    
    if parent_index >= 0 and arr[parent_index] < arr[i]:
        arr[parent_index], arr[i] = arr[i], arr[parent_index]
        max_heapify_up(arr, n, parent_index)


def delete_root(arr, n):
    arr[0] = arr[n - 1] # Replace the root with the last node
    del arr[n - 1] # Delete the last Node
    n = n - 1 # Reduction in size
    max_heapify(arr, n, 0) # Heapify the root again!

def insert_node(arr, n, value):
    n = n + 1 
    arr += [value] # Insert the new Node
    max_heapify_up(arr, n, n - 1)
    

if __name__ == "__main__":
    arr = [7, 3, 1, 3, 5, 6, 2,7, 8,]
    build_max_heap(arr, len(arr))
    print(arr)

    print("-----Inserting Node-----")
    insert_node(arr, len(arr), 10)
    print(arr)

    insert_node(arr, len(arr), 7)
    print(arr)

    delete_root(arr, len(arr))
    print(arr)

    delete_root(arr, len(arr))
    print(arr)

    # print(extractRoot(arr, len(arr)))
    # print(arr)



