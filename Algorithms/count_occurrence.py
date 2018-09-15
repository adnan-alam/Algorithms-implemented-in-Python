def binary_search(arr, item, search_first):
  low = 0
  high = len(arr)-1
  result = -1
  while (low <= high):
    mid = (low + high)//2

    if item == arr[mid]:
      result = mid
      if search_first:
        high = mid - 1
      else:
        low = mid + 1
    elif (item < arr[mid]):
      high = mid - 1
    else:
      low = mid + 1
  return result


def count_occurrence():
  arr = [1, 2, 2, 3, 3, 3, 3, 5, 6, 8]
  item = 3
  search_first = True
  first_index = binary_search(arr, item, search_first)
  if first_index == -1:
    print("Count of {} is 0".format(item))
  else:
    search_first = False
    last_index = binary_search(arr, item, search_first)
    count = last_index - first_index + 1
    print("Count of {} is {}".format(item,count))

count_occurrence()
