import random


class Song:
    __title: str
    __artist: str
    __duration: int
    __genre: str
    next_song = None

    def __init__(self, title: str, artist: str, duration: int, genre: str) -> None:
        self.__title = title
        self.__artist = artist
        self.__duration = duration
        self.__genre = genre

    def __str__(self) -> str:  # display_info()
        return f"{self.__title} by {self.__artist} ({self.__duration} sec) [{self.__genre}]"

    def get_duration(self) -> int:
        return self.__duration

    def get_title(self) -> str:
        return self.__title

    def get_artist(self) -> str:
        return self.__artist

    def get_genre(self) -> str:
        return self.__genre


class Playlist:
    __head = None
    __tail = None
    __current_song = None
    __len = 0

    def __init__(self) -> None:
        pass

    def add_song(self, song: Song) -> None:
        if self.__head is None:
            self.__head = song
            self.__tail = song
        else:
            self.__tail.next_song = song
            self.__tail = song
        self.__len += 1

    def remove_song(self, title: str) -> None:
        current = self.__head
        previous = None
        while current is not None:
            if current.get_title() == title:
                if previous is not None:
                    previous.next_song = current.next_song
                else:
                    self.__head = current.next_song
                self.__len -= 1
                return
            previous = current
            current = current.next_song

    def get_list(self) -> list:
        songs = []
        current = self.__head
        while current is not None:
            songs.append(current)
            current = current.next_song
        return songs

    def find_song(self, title: str):
        current = self.__head
        while current is not None:
            if current.__title == title:
                return current
            current = current.next_song
        return None

    def display_playlist(self) -> None:
        print("-" * 50)
        current = self.__head
        while current is not None:
            print(current)
            current = current.next_song
        print("-" * 50)

    def total_duration(self) -> int:
        total = 0
        current = self.__head
        while current is not None:
            total += current.get_duration()
            current = current.next_song
        return total

    def shuffle(self) -> None:
        songs = self.get_list()
        random.shuffle(songs)
        self.__head = songs[0]
        current = self.__head
        for i in range(1, len(songs)):
            current.next_song = songs[i]
            current = current.next_song
        self.__tail = current
        self.__tail.next_song = None

    def sort_by_duration(self) -> None:
        songs = self.get_list()
        songs.sort(key=lambda x: x.get_duration())
        self.__head = songs[0]
        current = self.__head
        for i in range(1, len(songs)):
            current.next_song = songs[i]
            current = current.next_song
        self.__tail = current
        self.__tail.next_song = None

    def get_tail(self):
        return self.__tail

    def get_head(self):
        return self.__head


def filter_by_genre(playlist: Playlist, genre: str) -> Playlist:
    new_playlist = Playlist()
    current = playlist.get_head()
    while current is not None:
        if current.get_genre() == genre:
            new_playlist.add_song(current)
        current = current.next_song


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
