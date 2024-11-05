# Assignment: Build a Playlist Manager

## Objective

In this assignment, you will create a **Playlist Manager** in Python using classes and Object-Oriented Programming (OOP) principles. This Playlist Manager will use a **linked list** to manage songs in a playlist, allowing users to add, remove, and rearrange songs. You’ll also add extra features, like shuffling songs and finding songs by genre.

## Requirements

### 1. Song Class (Node)

Create a `Song` class to represent each song in the playlist.

- **Attributes**:

  - `title` (str): The title of the song.
  - `artist` (str): The artist of the song.
  - `duration` (int): The duration of the song in seconds.
  - `genre` (str): The genre of the song.

- **Methods**:
  - `display_info()`: Prints the title, artist, and duration of the song.
  - `get_duration()`: Returns the duration of the song in seconds.

### 2. Playlist Class (Linked List)

Create a `Playlist` class to represent the linked list of songs.

- **Methods**:
  - `add_song(song)`: Adds a new `Song` object to the end of the playlist.
  - `remove_song(title)`: Removes the song with the specified title from the playlist.
  - `find_song(title)`: Finds and returns the `Song` object with the given title, if it exists.
  - `display_playlist()`: Prints all songs in the playlist in order.
  - `total_duration()`: Returns the total duration of all songs in the playlist.
  - `shuffle()`: Randomizes the order of songs in the playlist (without using a built-in shuffle function).

### 3. Advanced Features

For additional practice, try implementing some of these advanced features:

- **Sorting**: Add a method to sort the playlist by `duration`, `title`, or `artist`.
- **Genre Filter**: Add a method that filters songs by genre, returning a new playlist with songs of a specified genre.
- **Save/Load Playlist**: Implement methods to save the playlist to a file and load it back into the program.

### Example Usage

Here’s an example of how the `Playlist` and `Song` classes might be used:

```python
# Create songs
song1 = Song("Imagine", "John Lennon", 183, "Rock")
song2 = Song("Bohemian Rhapsody", "Queen", 354, "Rock")
song3 = Song("Shape of You", "Ed Sheeran", 263, "Pop")
song4 = Song("Billie Jean", "Michael Jackson", 294, "Pop")
song5 = Song("Smells Like Teen Spirit", "Nirvana", 301, "Rock")
song6 = Song("Rolling in the Deep", "Adele", 228, "Soul")
song7 = Song("Hallelujah", "Leonard Cohen", 339, "Folk")
song8 = Song("Hotel California", "Eagles", 390, "Rock")
song9 = Song("Stairway to Heaven", "Led Zeppelin", 482, "Rock")
song10 = Song("Someone Like You", "Adele", 285, "Pop")
song11 = Song("Let It Be", "The Beatles", 243, "Rock")
song12 = Song("Perfect", "Ed Sheeran", 263, "Pop")
song13 = Song("Hey Jude", "The Beatles", 431, "Rock")
song14 = Song("Shake It Off", "Taylor Swift", 242, "Pop")
song15 = Song("Take On Me", "A-ha", 225, "Pop")
song16 = Song("Sweet Child O' Mine", "Guns N' Roses", 356, "Rock")
song17 = Song("Livin' on a Prayer", "Bon Jovi", 248, "Rock")
song18 = Song("Eye of the Tiger", "Survivor", 245, "Rock")
song19 = Song("Wonderwall", "Oasis", 258, "Rock")
song20 = Song("Back in Black", "AC/DC", 255, "Rock")

# Create playlist and add songs
my_playlist = Playlist()
my_playlist.add_song(song1)
my_playlist.add_song(song2)
my_playlist.add_song(song3)
my_playlist.add_song(song4)
my_playlist.add_song(song5)
my_playlist.add_song(song6)
my_playlist.add_song(song7)
my_playlist.add_song(song8)
my_playlist.add_song(song9)
my_playlist.add_song(song10)
my_playlist.add_song(song11)
my_playlist.add_song(song12)
my_playlist.add_song(song13)
my_playlist.add_song(song14)
my_playlist.add_song(song15)
my_playlist.add_song(song16)
my_playlist.add_song(song17)
my_playlist.add_song(song18)
my_playlist.add_song(song19)
my_playlist.add_song(song20)

# Display playlist and total duration
my_playlist.display_playlist()
print("Total Duration:", my_playlist.total_duration())

# Remove a song and shuffle playlist
my_playlist.remove_song("Imagine")
my_playlist.shuffle()
my_playlist.display_playlist()
```
