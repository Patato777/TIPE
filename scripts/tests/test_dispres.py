from scripts.display_results import *

f = open(os.path.dirname(__file__)+'/resources/Liste_pos_Essonne_py.txt')
cities = eval(f.read())
f.close()
main = Main(cities)
city = cities[9]
n=main.map.plot(city[0],city[1],'foo')
print(main.map.canvas.coords(n[0]))
main.map.highlight(n)

main.root.mainloop()
