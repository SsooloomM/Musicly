from DB import DB
import Database_creation
db = DB.get_instance()

db.add_playlist("playlist1", "description 1")
db.add_playlist("playlist2", "description 2")
db.add_playlist("playlist3", "description 3")
db.add_playlist("playlist4", "description 4")


db.add_band("band1")
db.add_band("band2")

db.add_song("song1", "2010", "Anime", "bla bla bla", 3)
db.add_song("song2", "1015", "sad", "bl", 15)
db.add_song("song3", "1980", "Anime", "Enti ay kalam", 535)


db.add_artist("artist1" ,"1197","band id 1")
db.add_artist("artist2" ,"11978","band id 2")
db.add_artist("artist3" ,"11979","band id 3")

db.add_album("album title1" , 5, 1, 2)