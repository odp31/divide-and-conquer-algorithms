def merge_sort(arr):
  "" sorts array using merge sort""
  if len(arr) <= 1:
    return arr
  mid = len(arr) // 2
  left_half = arr[:mid]
  right_half = arr[mid:]

  left_half = merge_sort(left_half)
  right_half = merge_sort(right_half)

  return merge(left_half, right_half)

def merge(left, right):
  merged_array = []
  left_index = 0
  right_index = 0

  while left_index < len(left) and right_index < len(right):
    if left[left_index] <= right[right_index]:
      merged_array.append(left[left_index])
      left_index += 1
    else:
      merged_array.append(right[right_index])
      right_index += 1
  merged_array += left[left_index:]
  merged_array += right[right_index:]
  return merged_array 

# example usage
my_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = merge_sort(my_array)
print(sorted_array)
  
