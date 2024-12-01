# Zadání: Správce playlistů

## Cíl

V tomto zadání vytvoříte **Správce playlistů** v Pythonu s využitím tříd a principů Objektově Orientovaného Programování (OOP). Tento Správce playlistů umožní uživatelům přidávat, odebírat a přeuspořádávat skladby, a také nabídne další funkce jako je náhodné přehrávání skladeb a vyhledávání skladeb podle žánru.

## Požadavky

### 1. Třída Song

Vytvořte třídu `Song` reprezentující každou skladbu v playlistu.

- **Atributy**:
  - `title` (str): Název skladby
  - `artist` (str): Interpret skladby
  - `duration` (int): Délka skladby v sekundách
  - `genre` (str): Žánr skladby

- **Metody**:
  - `display_info()`: Vypíše název, interpreta a délku skladby
  - `get_duration()`: Vrátí délku skladby v sekundách

### 2. Třída Playlist

Vytvořte třídu `Playlist` pro správu kolekcí skladeb. Můžete použít libovolnou vhodnou datovou strukturu pro ukládání skladeb (např. list, dictionary).

- **Metody**:
  - `add_song(song)`: Přidá nový objekt `Song` do playlistu
  - `remove_song(title)`: Odstraní skladbu se zadaným názvem z playlistu
  - `find_song(title)`: Najde a vrátí objekt `Song` se zadaným názvem, pokud existuje
  - `display_playlist()`: Vypíše všechny skladby v playlistu
  - `total_duration()`: Vrátí celkovou délku všech skladeb v playlistu
  - `shuffle()`: Náhodně zamíchá pořadí skladeb v playlistu (můžete použít `random.shuffle()`)

### 3. Persistence dat

Implementujte ukládání a načítání playlistu do/z souboru. Můžete použít libovolný formát a knihovnu pro práci s daty:
- JSON (knihovna `json`)
- YAML (knihovna `yaml`)
- CSV (knihovna `csv`)
- Vlastní textový formát

Požadované metody:
- `save_to_file(filename)`: Uloží aktuální playlist do souboru
- `load_from_file(filename)`: Načte playlist ze souboru

### 4. Pokročilé funkce (volitelné)

Pro další praxi můžete implementovat některé z těchto pokročilých funkcí:

- **Třídění**: Přidejte metody pro řazení playlistu podle různých kritérií:
  - Podle délky skladby
  - Podle názvu skladby
  - Podle interpreta
  
- **Filtrování**: 
  - Filtrování podle žánru
  - Filtrování podle délky skladby (např. kratší než 3 minuty)
  - Filtrování podle interpreta

- **Statistiky playlistu**:
  - Celkový počet skladeb
  - Průměrná délka skladby
  - Nejčastější žánr
  - Nejčastější interpret
  - Nejdelší a nejkratší skladba

### Příklad použití

```python
# Vytvoření skladeb
song1 = Song("Imagine", "John Lennon", 183, "Rock")
song2 = Song("Bohemian Rhapsody", "Queen", 354, "Rock")
song3 = Song("Shape of You", "Ed Sheeran", 263, "Pop")

# Vytvoření playlistu a přidání skladeb
my_playlist = Playlist()
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)

# Zobrazení playlistu a celkové délky
my_playlist.display_playlist()
print("Celková délka:", my_playlist.total_duration())

# Uložení playlistu do souboru
my_playlist.save_to_file("my_playlist.json")

# Načtení playlistu ze souboru
loaded_playlist = Playlist()
loaded_playlist.load_from_file("my_playlist.json")

# Zamíchání playlistu
my_playlist.shuffle()
my_playlist.display_playlist()
```

## Doporučení pro implementaci

1. **Ukládání dat**:
   - Zvolte vhodný formát pro ukládání dat (JSON je doporučený pro začátek)
   - Ošetřete chybové stavy při práci se soubory
   - Validujte data při načítání ze souboru

2. **Práce s daty**:
   - Implementujte vhodné metody pro validaci vstupních dat
   - Ošetřete hraničí případy (prázdný playlist, neexistující skladba)
   - Použijte vhodné datové typy pro ukládání hodnot

3. **Kód**:
   - Používejte vhodné názvy proměnných a metod
   - Přidejte komentáře k složitějším částem kódu
   - Dodržujte standardní konvence Pythonu (PEP 8)

## Užitečné zdroje

### Oficiální dokumentace
- [Python dokumentace](https://docs.python.org/3/)
    - [Built-in Functions](https://docs.python.org/3/library/functions.html)
    - [random — Generate pseudo-random numbers](https://docs.python.org/3/library/random.html)
    - [json — JSON encoder and decoder](https://docs.python.org/3/library/json.html)
    - [csv — CSV File Reading and Writing](https://docs.python.org/3/library/csv.html)

### Práce s daty
- [Working with JSON data in Python](https://realpython.com/python-json/)
- [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)
- [PyYAML Documentation](https://pyyaml.org/wiki/PyYAMLDocumentation)

### OOP v Pythonu
- [Python Classes Documentation](https://docs.python.org/3/tutorial/classes.html)
- [Real Python - Object-Oriented Programming in Python](https://realpython.com/python3-object-oriented-programming/)
- [Python OOP Tutorial](https://www.programiz.com/python-programming/object-oriented-programming)

### Best Practices
- [PEP 8 - Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)
- [Python Docstring Conventions](https://peps.python.org/pep-0257/)
