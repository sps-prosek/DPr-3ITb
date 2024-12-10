import random
import time


def custom_sort(arr, reverse=False):
    """
    Sorts an array in ascending or descending order.

    Parameters:
    arr (list): The list to be sorted.
    reverse (bool): If True, sorts the list in descending order. Defaults to False.

    Returns:
    list: The sorted list.
    """
    # --- Add your code here ---
    sorted_arr = arr.copy()
    for n in range(len(sorted_arr) - 1, 0, -1):
        swapped = False
        for i in range(n):
            if reverse:
                if sorted_arr[i] < sorted_arr[i + 1]:
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    swapped = True
            else:
                if sorted_arr[i] > sorted_arr[i + 1]:
                    sorted_arr[i], sorted_arr[i + 1] = sorted_arr[i + 1], sorted_arr[i]
                    swapped = True
        if not swapped:
            break
    # ---------------------------
    return sorted_arr


def test_sort_function():
    """
    Tests the custom_sort function with various test cases and compares its performance
    with Python's built-in sorted function.
    """
    # Define test cases as tuples of (array_size, min_value, max_value)
    test_cases = [
        (int(1e1), 0, 100),
        (int(1e2), -100, 100),
        (int(1e3), 0, 1000),
        (int(1e4), -1000, 1000),
    ]

    for size, min_val, max_val in test_cases:
        # Generate a random array for the current test case
        arr = [random.randint(min_val, max_val) for _ in range(size)]

        # Test sorting in ascending order
        start_time = time.time()
        custom_sorted = custom_sort(arr.copy())
        custom_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        start_time = time.time()
        builtin_sorted = sorted(arr.copy())
        builtin_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        if custom_sorted == builtin_sorted:
            print(f"Ascending test passed for array size {size}.")
            print(f"Custom sort time: {custom_time:.6f} ms")
            print(f"Built-in sort time: {builtin_time:.6f} ms\n")
        else:
            print(f"Ascending test failed for array size {size}.")
            return

        # Test sorting in descending order
        start_time = time.time()
        custom_sorted = custom_sort(arr.copy(), reverse=True)
        custom_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        start_time = time.time()
        builtin_sorted = sorted(arr.copy(), reverse=True)
        builtin_time = (time.time() - start_time) * 1000  # Convert to milliseconds

        if custom_sorted == builtin_sorted:
            print(f"Descending test passed for array size {size}.")
            print(f"Custom sort time: {custom_time:.6f} ms")
            print(f"Built-in sort time: {builtin_time:.6f} ms\n")
        else:
            print(f"Descending test failed for array size {size}.")
            return

    print("All tests passed successfully.")


if __name__ == "__main__":
    test_sort_function()
