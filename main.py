from os import system
from DB import DB
import options
from Playlist import Playlists
from Songs import Songs
from  Artist import Artists
from  Album import  Albums
db = DB.get_instance()

def playlists():
    choice = 1
    Playlists.get_playlists()
    while(choice != 0):
        system('cls')
        print(options.start)
        print(options.playlists['topic'])
        Playlists.view_playlists()
        print(options.playlists['options'])
        choice = int(input("What you would like to do: "))

        if choice == 1:
          # Playlists.view_playlists()
           pass
        
        elif choice == 2:
            playlist_name = input("Enter playlist name: ")
            description = input("Enter description: ")
            Playlists.create_playlist(playlist_name, description)

        elif choice == 3:
            playlist_id = int(input("Enter playlist id: "))
            Playlists.delete_playlist(playlist_id)


def songs():
    choice = 1
    Songs.get_songs()
    while(choice != 0):
        system('cls')
        print(options.start)
        print(options.songs['topic'])
        Songs.view_songs()
        print(options.songs['options'])
        choice = int(input("What you would like to do: "))

        if choice == 1: #view song
            Songs.view_songs()
        
        elif choice == 2: #add song

            song_name = input("Enter song name: ")
            release_data =int(input("Enter release date: "))
            genres =  input("Enter genres: ")
            lyrics = input("Enter lyrics: ")
            length = int(input("Enter length of the song: "))
            #album_id = int(input("Enter album id: "))
            Songs.add_song(song_name,release_data,genres,lyrics,length)


        elif choice == 3: #delete song
            song_id = int(input("Enter song id: "))
            Songs.delete_song(song_id)

def artists():
    choice = 1
    Artists.get_artist()
    while(choice != 0):
        system('cls')
        print(options.start)
        print(options.artists['topic'])
        Artists.view_artists()
        print(options.artists['options'])
        choice = int(input("What you would like to do: "))

        if choice == 1: #view artist
            Artists.view_artists()

        elif choice == 2: #add artist
            artist_name = input("Enter artist name: ")
            date_of_birth = input("Enter date of birth: ")
            band_id = input("Enter band id: ")
            Artists.create_artist(artist_name,date_of_birth,band_id)

        elif choice == 3: #delete artist
            artist_id = int(input("Enter artist id: "))
            Artists.delete_artist(artist_id)

def albums():
    choice = 1
    Albums.get_albums()
    while(choice != 0):
        system('cls')
        print(options.start)
        print(options.artists['topic'])
        Albums.view_albums()
        print(options.albums['options'])
        choice = int(input("What you would like to do: "))

        if choice == 1: #pass
            Albums.view_albums()

        elif choice == 2: #add album
            title = input("Enter album title: ")
            number_of_songs = int(input("Enter number of songs: "))
            band_id = int(input("Enter band id: "))
            artist_id = int(input("Enter artist id: "))
            Albums.create_album(title,number_of_songs,band_id,artist_id)

        elif choice ==3:  #delete album
            album_id = int(input("Enter album id: "))
            Albums.delete_albums(album_id)




def main():
    while(True):
        system("cls")
        print(options.start)
        print(options.main)
        choice = int(input("What you would like to do: "))
    
        if choice == 0:
            system("cls")
            print("**** Thank you for using Musicly ****")
            break
        elif choice == 1:
            playlists()

        elif choice == 2:
            albums()

        elif choice == 3:
            artists()

        elif choice == 4:
            songs()
        else:
            print("Choose valid number.\n")

if __name__ == "__main__":
    # execute only if run as a script
    main()