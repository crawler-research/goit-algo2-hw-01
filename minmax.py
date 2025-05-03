def find_min_max(arr):
    if len(arr) == 1:
        return arr[0], arr[0]
    
    if len(arr) == 2:
        min_val = arr[0] if arr[0] < arr[1] else arr[1]
        max_val = arr[0] if arr[0] > arr[1] else arr[1]
        return min_val, max_val
    
    mid = len(arr) // 2
    left_min_max = find_min_max(arr[:mid])
    right_min_max = find_min_max(arr[mid:])
    
    overall_min = left_min_max[0] if left_min_max[0] < right_min_max[0] else right_min_max[0]
    overall_max = left_min_max[1] if left_min_max[1] > right_min_max[1] else right_min_max[1]
    
    return overall_min, overall_max

if __name__ == "__main__":
    array = [3, 5, 1, 2, 4, 8, 7]
    result = find_min_max(array)
    print(f"Мінімум: {result[0]}, Максимум: {result[1]}")