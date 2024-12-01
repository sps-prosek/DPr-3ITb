import random
import time


def custom_sort(arr, reverse=False):
    """
    Seřadí pole vzestupně nebo sestupně.

    Parametry:
    arr (list): Seznam k seřazení.
    reverse (bool): Pokud True, seřadí seznam sestupně. Výchozí hodnota je False.

    Vrací:
    list: Seřazený seznam.
    """
    # --- Zde přidejte svůj kód ---
    sorted_arr = sorted(arr, reverse=reverse)  # smažte tento řádek
    # ---------------------------
    return sorted_arr


def test_sort_function():
    """
    Testuje funkci custom_sort s různými testovacími případy a porovnává její výkon
    s vestavěnou funkcí sorted v Pythonu.
    """
    # Definice testovacích případů jako n-tice (velikost_pole, minimální_hodnota, maximální_hodnota)
    test_cases = [
        (int(1e3), 0, 100),
        (int(1e4), -100, 100),
        (int(1e5), 0, 1000),
        (int(1e6), -1000, 1000),
    ]

    for size, min_val, max_val in test_cases:
        # Generování náhodného pole pro aktuální testovací případ
        arr = [random.randint(min_val, max_val) for _ in range(size)]

        # Test vzestupného řazení
        start_time = time.time()
        custom_sorted = custom_sort(arr.copy())
        custom_time = (time.time() - start_time) * 1000  # Převod na milisekundy

        start_time = time.time()
        builtin_sorted = sorted(arr.copy())
        builtin_time = (time.time() - start_time) * 1000  # Převod na milisekundy

        if custom_sorted == builtin_sorted:
            print(f"Test vzestupného řazení úspěšný pro velikost pole {size}.")
            print(f"Čas vlastního řazení: {custom_time:.6f} ms")
            print(f"Čas vestavěného řazení: {builtin_time:.6f} ms\n")
        else:
            print(f"Test vzestupného řazení selhal pro velikost pole {size}.")
            return

        # Test sestupného řazení
        start_time = time.time()
        custom_sorted = custom_sort(arr.copy(), reverse=True)
        custom_time = (time.time() - start_time) * 1000  # Převod na milisekundy

        start_time = time.time()
        builtin_sorted = sorted(arr.copy(), reverse=True)
        builtin_time = (time.time() - start_time) * 1000  # Převod na milisekundy

        if custom_sorted == builtin_sorted:
            print(f"Test sestupného řazení úspěšný pro velikost pole {size}.")
            print(f"Čas vlastního řazení: {custom_time:.6f} ms")
            print(f"Čas vestavěného řazení: {builtin_time:.6f} ms\n")
        else:
            print(f"Test sestupného řazení selhal pro velikost pole {size}.")
            return

    print("Všechny testy úspěšně dokončeny.")


if __name__ == "__main__":
    test_sort_function()
