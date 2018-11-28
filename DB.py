import sqlite3

class DB:
    __instance = None


    @staticmethod
    def get_instance():
        if DB.__instance == None:
            return DB()
        return DB.__instance

    def __init__(self):
        if DB.__instance != None:
            raise Exception("This is a Singlton class, use get_instance() instead.")
        DB.__instance = self
        self.conn = sqlite3.connect('Musicly.db')

    def create_table(self, query):
        self.conn.execute(query)

    def drop_table(self, table_name):
        query = "DROP TABLE IF EXISTS `" + table_name + "`;"
        self.conn.execute(query)

    def add_playlist(self, *data):
        query = "INSERT INTO playlist (name, description) VALUES(?, ?)"
        self.conn.execute(query, data)
        self.conn.commit()
    
    def delete_playlist(self , id):
        query = "DELETE FROM playlist WHERE playlist_id = %i"%(id)
        self.conn.execute(query)
        self.conn.commit()

    
    def add_artist(self, *data):
        query = "INSERT INTO artist (name, date_of_birth, band_id) VALUES(?, ?, ?)"
        self.conn.execute(query, data)
        self.conn.commit()

    def add_band(self, *data):
        query = "INSERT INTO band (name) VALUES(?)"
        self.conn.execute(query, data)
        self.conn.commit()
    
    def add_song(self, *data):
        query = "INSERT INTO song (name, release_data, genres, lyrics, length) VALUES(?, ?, ?, ?, ?)"
        self.conn.execute(query, data)
        self.conn.commit()

    def select_all(self, table_name):
        query = "SELECT * FROM %s" % table_name
        cursor = self.conn.execute(query)
        return cursor


    def __del__(self):
        self.conn.close()