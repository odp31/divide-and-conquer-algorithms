# highly efficient sorting algorithm that follows divide and conquer
# selects a pivot elemetn and partitions the array into two subarrays: elements < pivot and elements > pivot

def quick_sort(arr):
  if len(arr) <= 1:
    return arr
  pivot = arr[0]
  left = []
  right = []
  for num in arr[1:]:
    if num < pivot:
      left.append(num)
    else:
      right.append(num)
  left = quick_sort(left)
  right = quick_sort(right)
  return left + [pivot] + right

# example usage
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quick_sort(my_array)
print(sorted_array) 
