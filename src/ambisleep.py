from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from subprocess import Popen

def stop_player():
    Popen(["mpc", "stop"])

# def start_player():
#     Popen(["mpc", "play"])

def start_player(tracknumber):
    print('playing track ', tracknumber)
    Popen(["mpc", "play", tracknumber])

root = ThemedTk(theme='equilux')
root.title("Ambisleep")
root.attributes('-fullscreen',True)

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Create a photoimage object to use the image
photo = PhotoImage(file = r"../pics/relaxingwaterfalls.png")
photo2 = PhotoImage(file = r"../pics/darkambientmelodies.png")
photo3 = PhotoImage(file = r"../pics/relaxingpiano.png") 
photo4 = PhotoImage(file = r"../pics/rainsounds.png") 
photo5 = PhotoImage(file = r"../pics/rollingwaves.png") 

### Buttons

#relaxing waterfall
b1 = ttk.Button(mainframe, text="Relaxing waterfall", image=photo, command= lambda: start_player('1'))
b1.grid(column=1, row=1, sticky=W, ipadx=17, ipady=24)

#dark ambient melodies
b2 = ttk.Button(mainframe, text="Dark Ambient Melodies", image=photo2, command= lambda: start_player('2'))
b2.grid(column=1, row=2, sticky=W, ipadx=17, ipady=24)

#relaxing piano
b3 = ttk.Button(mainframe, text="Relaxing Piano", image=photo3, command= lambda: start_player('3'))
b3.grid(column=1, row=3, sticky=W, ipadx=17, ipady=24)

#rainsounds
b4 = ttk.Button(mainframe, text="Rain Sounds", image=photo4, command= lambda: start_player('4'))
b4.grid(column=2, row=1, sticky=W, ipadx=17, ipady=24)

#rollingwaves
b5 = ttk.Button(mainframe, text="Rolling Waves", image=photo5, command= lambda: start_player('5'))
b5.grid(column=2, row=2, sticky=W, ipadx=17, ipady=24)

#STOP
b6 = ttk.Button(mainframe, text="Stop", command=stop_player)
b6.grid(column=3, row=1, sticky=W, ipadx=17, ipady=24)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()