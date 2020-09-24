from tkinter import *
import os

class Map:
    def __init__(self,canvas):
        self.canvas = canvas
        self.canvas.pack()
        self.img = PhotoImage(f'.{os.sep}resources{os.sep}frmap.gif')
        self.id = self.canvas.create_image(0,0,image=self.img)
        self.scale = 1
        self.minx,self.miny = 0,0

    def plot (self,x,y,color,label) :
        px,py = scale*x - self.minx, scale*y - self.miny
        self.canvas.create_oval(px-1,py-1,px+1,py+1,fill=color)
        self.canvas.create_text(px+2,py,text=label)

class Main:
    def __init__(self):
        self.root = Tk()
        self.map = Map(Canvas(self.root))
        self.root.update()
