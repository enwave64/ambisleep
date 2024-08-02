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
print("playlist: " , playlist)


# PHOTO stuff

#grab a list a of photos in the pics folder
photofiles = Popen(["ls", "../pics/"], stdout=PIPE).communicate()[0]
photofiles = photofiles.decode().split()

print("photofiles: " , photofiles)

#### temp hack for minimal mode:
playlist = {3: 'rainsounds', 1: 'relaxingwaterfall'}
photofiles = ['relaxingwaterfalls.png', 'rainsounds.png']

#create a dictionary of PhotoImage objects, key is filename
photos = {}
for file in photofiles:
    photos[file] = PhotoImage(file = f"../pics/{file}")


# Track buttons. Current assumption is a 3 x 3 grid of nine track selections.
# ROWS = 3
# COLS = 3
ROWS = 1
COLS = 2
row = 1
col = 1

for index, track in playlist.items():
    print(f'Creating button for track {index} : {track}')
    photo = False

    # try to match the photo to the trackname. Current assumption is the track and img names are almost identical. 
    # This can be refined to be "smarter"
    for pf in photofiles:
        result = re.search(track,pf)
        if(result):
            photo = photos[pf]

    #if we found a photo, create the button with the image
    if photo != False:
        button = ttk.Button(mainframe, text=track, image=photo, command= lambda num=index: start_player(f"{num}"))
    #otherwise just use the text
    else:
        button = ttk.Button(mainframe, text=track, command= lambda num=index: start_player(f"{num}"))
    # button.grid(column=col, row=row, sticky=W, ipadx=17, ipady=24)
    button.grid(column=col, row=row, sticky=W, ipadx=44, ipady=260)
    #do the grid rows & columns thing
    row = row + 1
    if row > ROWS:
        row = 1
        col = col + 1

# STOP button
stop_button = Button(mainframe, text="Stop", command=stop_player, bg="red")
stop_button.grid(column=4, row=1, sticky=W, ipadx=130, ipady=290)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

#ensure we're always looping a single track
mpc.mpc_setup()

root.mainloop()