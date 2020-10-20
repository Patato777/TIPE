from tkinter import *
import os,logging

class Map:
    def __init__(self,canvas,minc,maxc):
        self.canvas = canvas
        self.canvas.pack()
        corners,img = self.choosemap(minc,maxc)
        logging.debug(str((corners,corners[0][0])))
        self.img = PhotoImage(file=f'.{os.sep}resources{os.sep}{img}')
        self.imgh,self.imgw = self.img.height(),self.img.width()
        self.canvas.config(height=self.imgh, width=self.imgw)
        self.id = self.canvas.create_image(self.imgw//2,self.imgh//2,image=self.img)
        self.scale = self.img.width()/(corners[0][0]-corners[1][0])
        self.minlong,self.minlat = corners[1][0],corners[0][1]

    def choosemap(self,minc,maxc) :
        logging.debug(str((minc,maxc)))
        with open(f'.{os.sep}resources{os.sep}dimmap.txt') as f :
            mapindex = eval(f.read())
        included = lambda corners : minc[0]>corners[1][0] and minc[1]>corners[0][1] and maxc[0]<corners[0][0] and maxc[1]<corners[1][1]
        possible = [key for key in mapindex.keys() if included(key)]
        bestmap = min(possible,key = lambda item : (item[1][0]-item[0][0])*(item[1][1]-item[0][1]))
        return bestmap,mapindex[bestmap]

    def plot (self,long,lat,label) :
        plong,plat = self.imgh-self.scale*(long - self.minlong), self.scale*(lat - self.minlat)
        #TODO: Correct plat
        ov = self.canvas.create_oval(plat-1,plong-1,plat+1,plong+1)
        lbl = self.canvas.create_text(plat,plong+5,text=label)
        return ov,lbl

    def colorise (self, node, color):
        for elem in node :
            self.canvas.itemconfig(elem,fill=color)

class Population:
    def __init__(self,population) :
        self.pop = population
        self.min = (min(self.pop,key = lambda item : item[0])[0],min(self.pop,key = lambda item : item[1])[1])
        self.max = (max(self.pop,key = lambda item : item[0])[0],max(self.pop,key = lambda item : item[1])[1])
        logging.debug(str((self.pop,self.min)))
        
class Main:
    def __init__(self,population):
        self.root = Tk()
        self.pop = Population(population)
        self.map = Map(Canvas(self.root),self.pop.min,self.pop.max)
        self.root.update()

logging.basicConfig(filename='resources/display.log', level=logging.DEBUG)
""">>> main = Main	([(50,0),(45,5)])
[(50, 0), (45, 5)] (45, 0)
(45, 0) (50, 5)
>>> main.map.plot(50,0,'foo')
(2, 3)
>>> main.map.canvas.coords(2)
[-3599.4087922449867, 4.713, -3597.4087922449867, 6.713]"""
