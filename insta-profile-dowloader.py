from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image, ImageTk
import io
def finduser():
    try:
        L = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(L.context,userinput.get())
        getprof = urlopen(profile.get_profile_pic_url())
        data = getprof.read()
        getprof.close()
        profilepic = Image.open(io.BytesIO(data))
        pic = ImageTk.PhotoImage(profilepic)
        piclabel.config(image=pic)
        piclabel.image = pic
        piclabel.pack()
    except:
        piclabel.config(text='User Not Found.')
        piclabel.pack()
    # print(profile.followers)
    # print(profile.followees)
    # print(profile.is_private())
    # print(profile.is_verified())
    # print(profile.biography)
    # print(profile.get_posts())
    # for posts in profile.get_posts():
    #     print(posts.likes)
    #     print(posts.caption)
window = Tk()
window.title('Instagram Profile Picture Downloader')
window.geometry('600x400')
window.minsize(400,200)
label = Label(window,text='Tell me the Instagram username:')
label.pack()
userinput = Entry(window,width = 30)
userinput.pack()

btn1 = Button(window,text='show picture',relief='solid',command=finduser)
btn1.pack()
piclabel = Label(window)
window.mainloop()