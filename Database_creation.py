from DB import DB

# Delete all tables 

db = DB.get_instance()

tables = ["playlist_songs", "artist_songs", "song", "artist", "album", "playlist", "band"]

for i in tables:
    db.drop_table(i)



''' Database Tables '''

# playlist

query = """
CREATE TABLE IF NOT EXISTS `playlist`
(
 `playlist_id` INTEGER  PRIMARY KEY ,
 `name`        text     NOT NULL ,
 `description` text     NOT NULL
);
"""

db.create_table(query)

# Brand

query = """
CREATE TABLE `band`
(
 `band_id` INTEGER  PRIMARY KEY ,
 `name`    text NOT NULL
);
"""
db.create_table(query)

# artist 

query = """
CREATE TABLE `artist`
(
 `artist_id`     INTEGER  PRIMARY KEY ,
 `name`          text NOT NULL ,
 `date_of_birth` date NOT NULL ,
 `band_id`       int ,
FOREIGN KEY (`band_id`) REFERENCES `band` (`band_id`)
);
"""

db.create_table(query)

# album

query = """
CREATE TABLE `album`
(
 `album_id`        INTEGER  PRIMARY KEY ,
 `title`           text NOT NULL ,
 `number_of_songs` int NOT NULL ,
 `band_id`         int ,
 `artist_id`       int ,
FOREIGN KEY (`band_id`) REFERENCES `band` (`band_id`)
);
"""

db.create_table(query)

# song

query = """
CREATE TABLE `song`
(
 `song_id`      INTEGER  PRIMARY KEY ,
 `name`         text NOT NULL ,
 `release_data` date NOT NULL ,
 `genres`       text NOT NULL ,
 `lyrics`       text NOT NULL ,
 `length`       float NOT NULL ,
 `album_id`     int ,
FOREIGN KEY (`album_id`) REFERENCES `album` (`album_id`)
);
"""

db.create_table(query)

# playlist_song
# relation between playlist and song is many to many

query = """
CREATE TABLE `playlist_songs`
(
 `playlist_song_id` INTEGER  PRIMARY KEY ,
 `playlist_id`      int NOT NULL ,
 `song_id`          int NOT NULL ,
FOREIGN KEY (`playlist_id`) REFERENCES `playlist` (`playlist_id`),
FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);
"""

db.create_table(query)

# artist_songs
# relation between atrist and song is many to many

query = """
CREATE TABLE `artist_songs`
(
 `artist_songs` INTEGER  PRIMARY KEY ,
 `artist_id`    int NOT NULL ,
 `song_id`      int NOT NULL ,
FOREIGN KEY (`artist_id`) REFERENCES `artist` (`artist_id`),
FOREIGN KEY (`song_id`) REFERENCES `song` (`song_id`)
);
"""

db.create_table(query)


