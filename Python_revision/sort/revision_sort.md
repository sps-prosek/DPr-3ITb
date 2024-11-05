# Python Revision Assignment: Sorting Algorithm

## Objective

Implement a sorting algorithm that can sort an array of numbers by a specified pattern (from lowest to highest or reverse).

## Instructions

1. **Generate an Array**: Create an array with random numbers.
2. **Sorting Algorithm**: Implement a sorting algorithm of your choice (e.g., bubble sort, quicksort, etc.) or come up with your own.
3. **Sorting Order**: Your algorithm should be able to sort the array in both ascending and descending order.
4. **Validation**: Verify the correctness of your solution by comparing it with Python's built-in `sort` function. Use provided test script (`sort_validator.py`) to validate your solution on larger sample.

## Steps

1. **Generate Random Array**:

   - Use Python's `random` module to generate an array of random numbers.

   ```python
   import random
   array = [random.randint(0, 100) for _ in range(10)]
   ```

2. **Implement Sorting Algorithm**:

   - Choose a sorting algorithm and implement it. For example, a simple bubble sort:

   ```python
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
        sorted_arr = sorted(arr, reverse=reverse)  # comment this line
        # ---------------------------
        return sorted_arr
   ```

3. **Sort the Array**:

   - Sort the array in ascending order:

   ```python
   sorted_array = custom_sort(array)
   print("Sorted Array (Ascending):", sorted_array)
   ```

   - Sort the array in descending order:

   ```python
   sorted_array_desc = custom_sort(array, reverse=True)
   print("Sorted Array (Descending):", sorted_array_desc)
   ```

4. **Validate with Built-in Sort**:

   - Use Python's built-in `sort` function to validate your results:

   ```python
   builtin_sorted = sorted(array)
   print("Built-in Sorted Array (Ascending):", builtin_sorted)

   builtin_sorted_desc = sorted(array, reverse=True)
   print("Built-in Sorted Array (Descending):", builtin_sorted_desc)
   ```

5. **Validate your solution with provided validation script**:
   - Copy your function into validation script (`sort_validator.py`) and run the script.
   - The validation script will test your solution on larger sample and show if your code works or not (it also shows time statistics).
   - In order for the validation script to work properly the function must have same inputs as shown above.

## Notes

- Ensure your code is well-commented and follows Python best practices.
- You can use any sorting algorithm you are comfortable with or invent your own.
- Don't use AI tools and try not to search for finished solution. This revision is meant for your practice.
- Best solution might get bonus grade.

Good luck!
