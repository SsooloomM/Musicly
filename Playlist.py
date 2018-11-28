from DB import DB

class Playlists:
    class Playlist:
        def __init__(self, playlist):
            self.id = playlist[0]
            self.name = playlist[1]
            self.description = playlist[2]

        def get_playlist(self, playlist):
            self.id = playlist[0]
            self.name = playlist[1]
            self.description = playlist[2]
        
        def __str__(self):
            return "playlist_ID: %i, name: %s, description: %s" % (self.id, self.name, self.description)

    
    playlists = []
    db = DB.get_instance()

    @classmethod
    def get_playlists(cls):
        cls.playlists = []
        playlists = cls.db.select_all("playlist")
        for playlist in playlists:
            cls.playlists.append(cls.Playlist(playlist))
    
    @classmethod
    def view_playlists(cls):
        for playlist in cls.playlists:
            print(playlist)

    @classmethod
    def create_playlist(cls, *data):
        cls.db.add_playlist(*data)
        cls.get_playlists()

    @classmethod
    def delete_playlist(cls, id):
        cls.db.delete_playlist(id)
        cls.get_playlists()
        
