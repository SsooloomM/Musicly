class Songs:
    class Song:
        def __init__(self, song):
            self.get_song(song)

        def get_song(self, song):
            self.id = song[0]
            self.name = song[1]
            self.release_data = song[2]
            self.genres = song[3]
            self.lyrics = song[4]
            self.length = song[5]
            self.album_id = song[6]

        def __str__(self):
            value = "song_ID: %i, " % self.id
            value += "name: %s, " % self.name
            value += "release_data: %s, " % self.release_data
            value += "genres: %s, " % self.genres
            value += "lyrics: %s, " % self.lyrics
            value += "length: %f." % self.length
            return value

    
    songs = []
    
    @classmethod
    def get_songs(cls, db):
        cls.songs = []
        songs = db.select_all("song")
        for song in songs:
            cls.songs.append(cls.Song(song))
    
    @classmethod
    def view_songs(cls):
        for song in cls.songs:
            print(song)