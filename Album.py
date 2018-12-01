from DB import DB

class Albums:
    class Album:
        def __init__(self, album):
            self.get_album(album)

        def get_album(self, album):
            self.id = album[0]
            self.title = album[1]
            self.number_of_songs = album[2]
            self.band_id = album[3]
            self.artist_id = album[4]

        def __str__(self):
            value = "album_ID: %i, " % self.id
            value += "title: %s, " % self.title
            value += "number of songs: %s, " % self.number_of_songs
            value += "band_id: %s, " % self.band_id
            value += "artist_id: %s, " % self.artist_id
            return value


    albums = []
    db = DB.get_instance()

    @classmethod
    def get_albums(cls):
        cls.albums = []
        albums = cls.db.select_all("album")
        for album in albums:
            cls.albums.append(cls.Album(album))

    @classmethod
    def create_album(cls,*data):
         cls.db.add_album(*data)
         cls.get_albums()

    @classmethod
    def view_albums(cls):
        for album in cls.albums:
            print(album)

    @classmethod
    def delete_albums(cls,id):
        cls.db.delete_album(id)
        cls.get_albums()

