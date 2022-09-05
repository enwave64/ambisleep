# ambisleep

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from mpc import start_player, stop_player
import mpc
from subprocess import Popen, PIPE
import re

root = ThemedTk(theme='equilux')
root.title("Ambisleep")
root.attributes('-fullscreen',True)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

playlist = mpc.construct_playlist()


# PHOTO stuff

#grab a list a of photos in the pics folder
photofiles = Popen(["ls", "../pics/"], stdout=PIPE).communicate()[0]
photofiles = photofiles.decode().split()

#create a dictionary of PhotoImage objects, key is filename
photos = {}
for file in photofiles:
    photos[file] = PhotoImage(file = f"../pics/{file}")


# Track buttons
ROWS = 3
COLS = 3
row = 1
col = 1
for index, track in enumerate(playlist):
    photo = False

    # try to match the photo to the trackname. Current assumption is the track and img names are almost identical. 
    # This can be refined to be "smarter"
    for pf in photofiles:
        result = re.search(track,pf)
        if(result):
            photo = photos[pf]

    #if we found a photo, create the button with the image
    if photo != False:
        button = ttk.Button(mainframe, text=track, image=photo, command= lambda: start_player(index))
    #otherwise just use the text
    else:
        button = ttk.Button(mainframe, text=track, command= lambda: start_player(index))
    button.grid(column=col, row=row, sticky=W, ipadx=17, ipady=24)
    #do the grid rows & columns thing
    row = row + 1
    if row > ROWS:
        row = 1
        col = col + 1

# STOP button
stop_button = Button(mainframe, text="Stop", command=stop_player, bg="red")
stop_button.grid(column=4, row=1, sticky=W, ipadx=27, ipady=55)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#ensure we're always looping a single track
mpc.mpc_setup()

root.mainloop()