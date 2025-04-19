from pypresence import Presence
import tkinter
from tkinter import ttk
import sv_ttk
import time

print("Welcome to OmniRPC!")

client_id = 1362902413387890889 # Replace with json config or anything better than a line in the code later :P
presence = Presence(client_id)
presence.connect()

presencekwargs = {}

def start():    
    if stateset.get():
        presencekwargs["state"] = stateset.get()
    if detailset.get():
        presencekwargs["details"] = detailset.get()
    
    presence.update(
        large_image="minecraft_1_", 
        start=1306448978,
        **presencekwargs,
    )
    print("Presence Updated")
    deactbut.config(state="normal")

def stop(): 
    time.sleep(2)
    print(presence.clear())
    print("Presence Cleared")
    deactbut.config(state="disabled")

def close():
    presence.clear()
    root.destroy()

def unfocus(event):
    if event.widget != detailset and event.widget != stateset:
        root.focus_set()  

root = tkinter.Tk()
root.title("OmniRPC")
root.geometry("800x600+100+50")
root.minsize(800, 600)
root.bind("<Button-1>", unfocus)
root.protocol("WM_DELETE_WINDOW", close)

title = ttk.Label(root, text="OmniRPC", font=("Tahoma", 24, "bold"))
title.place(x=30, y=20)

actbut = ttk.Button(root, text="Start!", command=start)
actbut.place(x=30, y=80)

deactbut = ttk.Button(root, text="Stop!", command=stop, state="disabled")
deactbut.place(x=110, y=80)

detailset = ttk.Entry()
detailset.place(x=555, y=80)
detaillab = ttk.Label(root, text="Detail")
detaillab.place(x=495, y=88)

stateset = ttk.Entry()
stateset.place(x=555, y=130)
statelab = ttk.Label(root, text="State")
statelab.place(x=495, y=138)

sv_ttk.set_theme("dark")
root.mainloop()
