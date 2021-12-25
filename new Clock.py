import time
from tkinter import *

root = Tk()

root.grometry("359*150+0+0")

root.configure(background="black")
root.resizable(0,0)

root.overrideredirect(1)

def start():
    text = time.strftime("")