from tkinter import *
import os,logging

dirname = os.path.dirname(__file__)
with open(dirname+'/resources/config') as f :
    text = f.read()
    beginning = text.find('\n',text.find('<display>'))
    end = text.find('</display>')
    config = text[beginning:end]
    exec(config)

def label(strg) :
    if NAMES == 'full' :
        return strg
    if NAMES == 'initial' :
        return strg[0]
    if NAMES == 'name' :
        return strg.split(' (')[0]
    if NAMES == 'ZIP' :
        return strg.split(' (')[1][:-1]

class Map:#Graphic interface
    def __init__(self,canvas,minc,maxc):
        self.canvas = canvas
        self.canvas.pack()
        corners,img = self.choosemap(minc,maxc)#Coord of the corners ((maxong,minlat),(minlong,maxlat)) of the map and the corresponding picture
        logging.debug(str((corners,corners[0][0])))
        self.img = PhotoImage(file=dirname+f'{os.sep}resources{os.sep}{img}')
        self.imgh,self.imgw = self.img.height(),self.img.width()#Size of the picture
        #Displaying the map
        self.canvas.config(height=self.imgh, width=self.imgw)
        self.id = self.canvas.create_image(self.imgw//2,self.imgh//2,image=self.img)
        #Scale of the map
        self.latscale = self.imgw/(corners[1][1]-corners[0][1])
        self.longscale = self.imgh/(corners[0][0]-corners[1][0])
        self.minlong,self.minlat = corners[1][0],corners[0][1]

    def choosemap(self,minc,maxc) :#To choose the best map, given the places
        logging.debug(str((minc,maxc)))
        with open(dirname+f'{os.sep}resources{os.sep}dimmap.txt') as f :
            mapindex = eval(f.read())
        included = lambda corners : minc[0]>=corners[1][0] and minc[1]>=corners[0][1] and maxc[0]<=corners[0][0] and maxc[1]<=corners[1][1]
        #Best map among those which contain all the points
        possible = [key for key in mapindex.keys() if included(key)]
        logging.debug("Possible maps: "+str(possible))
        logging.debug('Area: '+str([(item[1][0]-item[0][0])*(item[1][1]-item[0][1]) for item in possible]))
        bestmap = min(possible,key = lambda item : (item[0][0]-item[1][0])*(item[1][1]-item[0][1]))
        return bestmap,mapindex[bestmap]

    def plot (self,long,lat,label) :#To plot a point
        #Calculating the coords on the picture
        plong,plat = self.imgh-self.longscale*(long - self.minlong), self.latscale*(lat - self.minlat)
        #Displaying the place among with its nam
        ov = self.canvas.create_oval(plat-1,plong-1,plat+1,plong+1)
        lbl = self.canvas.create_text(plat,plong+5,text=label)
        return ov,lbl

    def colorise (self, node, color):#To change the color of a point
        for elem in node :
            self.canvas.itemconfig(elem,fill=color)

    def highlight(node) :
        coords = self.canvas.coords(node[0])
        ov = self.canvas.create_oval(coords[0]-3,coords[1]-3,coords[2]+3,coords[3]+3)
        return ov

class Population:#The class of the nodes (population is a list of couples)
    def __init__(self,population,names) :
        self.pop = [(coord[0],coord[1],names[k]) for k,coord in enumerate(population)]
        #The most extreme coords
        self.min = (min(self.pop,key = lambda item : item[0])[0],min(self.pop,key = lambda item : item[1])[1])
        self.max = (max(self.pop,key = lambda item : item[0])[0],max(self.pop,key = lambda item : item[1])[1])
        logging.debug(str((self.pop,self.min)))
        
class Main:
    def __init__(self,population,names):
        self.root = Tk()
        self.pop = Population(population,names)
        self.map = Map(Canvas(self.root),self.pop.min,self.pop.max)
        self.root.update()

    def dispool(self,pools):
        self.pop.pools = [[self.pop.pop[k] for k in pool] for pool in pools]
        for k,pool in enumerate(self.pop.pools):
            color = COLORS[k*765//len(pools)]
            for node in pool:
                self.map.colorise(self.map.plot(node[0],node[1],label(node[2])),color)

logging.basicConfig(filename=dirname+'/resources/display.log', level=logging.DEBUG)
