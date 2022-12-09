# Music player in python
# add multiple music
# play list
# link
# search on yt
# play song
# gui for player
from pygame import mixer
mixer.init()
# --------------------------Path of your music
mixer.music.load("audio/Shree 420 - Pyar Hua Ikrar Hua Hai Pyar Se - Manna Dey - Lata Mangeshkar.mp3")
mixer.music.set_volume(0.5)
mixer.music.play()

while True:
    print("Press 'p' to pause")
    print("Press 'r' to resume")
    print("Press 'v' set volume")
    print("Press 'e' to exit")
    print("Press 'l' for lyrics ")

    ch = input("['p','r','v','e','l']>>>")

    if ch == "p":
        mixer.music.pause()
    elif ch == "r":
        mixer.music.unpause()
    elif ch == "v":
        v = float(input("Enter volume(0 to 1): "))
        mixer.music.set_volume(v)
    elif ch == "e":
        mixer.music.stop()
        break
    elif ch == "l":
        print("Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Kaho ki apani\n"
          "Preet ka geet ka\n"
          "Badalega kabhi\n"
          "Tum bhi kaho is\n"
          "Raah ka meet naa\n"
          "Badalega kabhi\n"
          "Pyaar jo tuta pyaar\n"
          "Jo chuta chand naa\n"
          "Chamakega kabhi\n"
          "Aahaa haa aahaa haa aa\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Raato daso dishaao se\n"
          "Kahegi apani kahaiyaan\n"
          "Prit hamaare pyaar ki\n"
          "Doharaaegi jawaniya\n"
          "Mai na rahugi tum na rahoge\n"
          "Phir bhi rahegi nishaaniyaan\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Kehata hai dil rasta mushkil\n"
          "Maalum nahi hai kaha manzil\n"
          "Pyaar hua iqaraar hua hai\n"
          "Pyaar se phir kyo darta hai dil.")
