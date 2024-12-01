# Python Opakovací Úloha: Řadící algoritmus

## Cíl

Implementujte řadící algoritmus, který dokáže seřadit pole čísel podle zadaného vzoru (od nejmenšího po největší nebo obráceně).

## Pokyny

1. **Generování pole**: Vytvořte pole s náhodnými čísly.
2. **Řadící algoritmus**: Implementujte řadící algoritmus podle vlastního výběru (např. bubble sort, quicksort atd.) nebo vymyslete vlastní.
3. **Směr řazení**: Váš algoritmus by měl umět řadit pole vzestupně i sestupně.
4. **Implementace**: Napište své řešení přímo do funkce `custom_sort` v souboru `sort_validator.py`.
5. **Validace**: Spusťte skript `sort_validator.py` pro ověření správnosti vašeho řešení.

## Implementace řešení

1. **Otevřete soubor `sort_validator.py`**
2. **Najděte funkci `custom_sort`**:

```python
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
```

3. **Implementujte váš řadící algoritmus**: 
   - Smažte řádek `sorted_arr = sorted(arr, reverse=reverse)`
   - Napište vlastní implementaci řazení
   - Dbejte na správné zpracování parametru `reverse`

4. **Spusťte validaci**:
   - Spusťte soubor `sort_validator.py`
   - Skript otestuje vaše řešení na různě velkých polích
   - Pro každý test zobrazí:
     - Zda test prošel
     - Čas vašeho řešení
     - Čas vestavěného řazení pro porovnání

## Testovací případy

Validační skript testuje vaše řešení na následujících případech:
1. Pole velikosti 1 000 prvků (rozsah 0-100)
2. Pole velikosti 10 000 prvků (rozsah -100 až 100)
3. Pole velikosti 100 000 prvků (rozsah 0-1000)
4. Pole velikosti 1 000 000 prvků (rozsah -1000 až 1000)

Pro každou velikost pole se testuje:
- Vzestupné řazení (`reverse=False`)
- Sestupné řazení (`reverse=True`)

## Poznámky

- Ujistěte se, že váš kód je dobře okomentovaný a dodržuje Python best practices
- Nepoužívejte vestavěné řadící funkce Pythonu (`sort`, `sorted`)
- Nepoužívejte AI nástroje a snažte se nehledat hotové řešení

## Užitečné zdroje

### Oficiální dokumentace
- [Python dokumentace](https://docs.python.org/3/)
    - [Built-in Functions](https://docs.python.org/3/library/functions.html)
    - [random — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
    - [Python dokumentace - seznamy](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

### Best Practices
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python Docstring Conventions](https://peps.python.org/pep-0257/)

Hodně štěstí!