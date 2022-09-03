# ambisleep


# current playlist
# 
# pi@raspberrypi:~/ambisleep/mp3 $ mpc playlist
# /home/pi/Music/RelaxingWaterfall.mp3
# /home/pi/ambisleep/mp3/Dark Ambient Melodies-LptTKfrHSi4.mp3
# /home/pi/ambisleep/mp3/relaxingpiano.mp3
# /home/pi/ambisleep/mp3/rainsounds.mp3
# /home/pi/ambisleep/mp3/rollingwaves.mp3
# /home/pi/ambisleep/mp3/brownnoise.mp3
# /home/pi/ambisleep/mp3/azure.mp3
# /home/pi/ambisleep/mp3/gothiclitanies.mp3
# /home/pi/ambisleep/mp3/litanysanguine.mp3

from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
from subprocess import Popen

def stop_player():
    Popen(["mpc", "stop"])

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
photo6 = PhotoImage(file = r"../pics/brownnoise.png") 
photo7 = PhotoImage(file = r"../pics/azure.png") 
photo8 = PhotoImage(file = r"../pics/gothiclitanies.png") 
photo9 = PhotoImage(file = r"../pics/litanysanguine.png") 

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

#brownnoise
b6 = ttk.Button(mainframe, text="Brown Noise", image=photo6, command= lambda: start_player('6'))
b6.grid(column=2, row=3, sticky=W, ipadx=17, ipady=24)

#azure
b7 = ttk.Button(mainframe, text="G a t e w a y - Azure", image=photo7, command= lambda: start_player('7'))
b7.grid(column=3, row=1, sticky=W, ipadx=17, ipady=24)

#gothiclitanies
b8 = ttk.Button(mainframe, text="Gothic Litanies", image=photo8, command= lambda: start_player('8'))
b8.grid(column=3, row=2, sticky=W, ipadx=17, ipady=24)

#litanysanguine
b9 = ttk.Button(mainframe, text="Litany for Sanguinius", image=photo9, command= lambda: start_player('9'))
b9.grid(column=3, row=3, sticky=W, ipadx=17, ipady=24)

#STOP
b10 = Button(mainframe, text="Stop", command=stop_player, bg="red")
b10.grid(column=4, row=1, sticky=W, ipadx=27, ipady=55)


for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

root.mainloop()