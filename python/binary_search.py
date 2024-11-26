# repeatedly divides search interval in half until target value is found or determined to be absent

def binary_search(arr, target):
  """ performs binary search on a sorted array"""
  left = 0
  right = len(arr) - 1
  while left <= right:
    mid = (left + right) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      left = mid + 1
    else:
      right = mid - 1
  return -1

# example usage
my_array = [2, 3, 4, 10, 40]
target = 10

result = binary_search(my_array, target)
if result != -1:
  print("element is present at index", str(result))
else:
  print("element is not present in array")
