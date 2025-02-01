import os
os.add_dll_directory(r'C:/Program Files/VideoLAN/VLC')
import vlc

songs= ["C:\songs\Bad Boy - Tungevaag Raaban_128-(DJMaza).mp3" ,
          ("C:\songs\Blow.mp3"),
          ("C:\songs\Childhood(Mr-Jatt1.com).mp3"),
          ("C:\songs\Closer (1).mp3"),
          ("C:\songs\\faded.mp3"),
          ("C:\songs\Grateful_320(PagalWorld).mp3"),
          ("C:\songs\Let Her Go x Husn-(DJPunjab).mp3"),
          ("C:\songs\Masakali 2.0 Tulsi Kumar 320 Kbps.mp3"),
          ("C:\songs\\Nightcore+Apollo+Lyrics.mp3"),
          ("C:\songs\On-My-Way.mp3")
          ] 
like_songs = []
like_songs_name=[]
def con_play_song():
    
     i=0
     for songss in songs: 
        p = vlc.MediaPlayer(songss)
        p.play()    
        print("Now playing:", songnames[i])
        inp = input("Press enter for next song or 'l' to save this song ro press q to exit: ")
        p.stop()
        if inp == 'q' or inp == 'Q':   
           break 
        elif inp == 'l' or inp =='L':
                like_songs.append(songss)
                like_songs_name.append(songnames[i])
                print("Song saved.")
        i +=1       
        #   like_songs=[i]= songs[i]
                     

songnames=["bad boy","blow","childhood","closer","faded","gratefull","let her go x husn","masakali",
               "nightcode","on my way" ]

def liked():
    i = 0
    while i < len(like_songs):
        p = vlc.MediaPlayer(like_songs[i])
        p.play()
        print("song name =", like_songs_name[i])
        inp = input("Press Enter for your next favorite song or 'd' to delete the favorite song: ")
        p.stop()
        if inp == 'd' or inp =='D':
            del like_songs[i]
            del like_songs_name[i]
            print("song deleted.")
        else:
          i += 1


def user_choose():
    i = 0
    for n in songnames:
        print(i, "=", songnames[i])
        i += 1
    num= int(input("enter the song number="))
    if num>len(songs) or num <0:
       print("please enter the number 0 to 9 only")
    elif num<=len(songs) and num >=0:
        p = vlc.MediaPlayer(songs[num])
        print("the song which you chose is",songnames[num])
        p.play()
        input("Press Enter to stop playback.")
        p.stop()
    else:
        print("Invalid song number")

def liked_songss():
   i=0
   while i< len(like_songs_name):
      print(like_songs_name[i])
      i+=1
      
print(" cilck 1 => to play the song continuosly one after another ")
print("         =>    press l to like the song")
print("         =>    press q to exit while playing song")
print(" click 2 => to see what all songs have you liked")
print(" click 3 => to play the song which you liked ")
print("         =>    press d to delet the song")
print(" click 4 => and select your song to play")
print(" click 5 => to exit ")
choise=0
while choise != 5: 
   choise = int(input("select your choise =>"))
   
   if choise == 1:
    con_play_song() 
   elif choise == 2:
    liked_songss()
   elif choise == 3:
    liked()   
   elif choise == 4:
    user_choose()   
   elif choise == 5:
    print("Exiting...")   
   else:
    print("Invalid choice. Please select again.")
