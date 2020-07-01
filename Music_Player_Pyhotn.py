from playsound import playsound
import glob
def music_player(path):
    for song in glob.glob(path):
        print("Enjoy Your Song"+song)
        playsound(song)
music_player("C:/Users/psitm/OneDrive/Desktop/*.mp3")
        
