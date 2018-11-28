from os import system
from DB import DB
import options
from Playlist import Playlists
from Songs import Songs

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
            pass
        
        elif choice == 2:
            playlist_name = input("Enter playlist name: ")
            description = input("Enter description: ")
            Playlists.create_playlist(playlist_name, description)

        elif choice == 3:
            playlist_id = input("Enter playlist id: ")
            Playlists.delete_playlist(playlist_id)



def songs():
    choice = 1
    Songs.get_songs(db)
    while(choice != 0):
        system('cls')
        print(options.start)
        print(options.songs['topic'])
        Songs.view_songs()
        print(options.songs['options'])
        choice = int(input("What you would like to do: "))

        if choice == 1:
            pass
        
        elif choice == 2:
            pass

        elif choice == 3:
            pass






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
        elif choice == 4:
            songs()
        else:
            print("Choose valid number.\n")

if __name__ == "__main__":
    # execute only if run as a script
    main()