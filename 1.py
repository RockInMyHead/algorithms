import numpy as np

def sort_algorithm(arr):
    return sorted(arr)

def main_sort():
    arr = [5, 2, 9, 1, 5, 6]
    sorted_arr = sort_algorithm(arr)
    print("Отсортированный массив:", sorted_arr)

if __name__ == "__main__":
    main_sort()

print("Change")
