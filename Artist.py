from DB import DB

class Artists:
    class Artist:
        def __init__(self, artist):
            self.id = artist[0]
            self.name = artist[1]
            self.date_of_birth = artist[2]
            self.band_id = artist[3]


        def get_artist(self,artist):
            self.id = artist[0]
            self.name = artist[1]
            self.date_of_birth = artist[2]
            self.band_id = artist[3]

        def __str__(self):
            value = "artist_ID: %i, " % self.id
            value += "name: %s, " % self.name
            value += "date_of_birth: %s, " % self.date_of_birth
            value += "band_id: %s, " % self.band_id
            return value

    artists = []
    db = DB.get_instance()

    @classmethod
    def get_artist(cls):
        cls.artists = []
        artists = cls.db.select_all("artist")
        for artist in artists:
            cls.artists.append(cls.Artist(artist))

    @classmethod
    def view_artists(cls):
        for artist in cls.artists:
            print(artist)

    @classmethod
    def create_artist(cls, *data):
        cls.db.add_artist(*data)
        cls.get_artist()

    @classmethod
    def delete_artist(cls, id):
        cls.db.delete_artist(id)
        cls.get_artist()

